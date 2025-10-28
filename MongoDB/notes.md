# Schema Desgin Patterns and Anti-Patterns

---

# 🧬 Inheritance Pattern in MongoDB

## 🧠 Concept Overview

* Humans naturally **group similar things**, and MongoDB’s **inheritance pattern** allows grouping similar documents with shared and unique fields.
* It’s based on **polymorphism**, meaning documents in one collection can have **different shapes/forms**.
* Use this pattern when documents have **more similarities than differences** and are often **accessed together**.

---

## 📚 Example: Bookstore App

We have different entities — **E-Books**, **Audiobooks**, and **Printed Books** — that share attributes like:

* `title`, `author`, `genres`, `price`, `publisher`

Each type also has **unique fields**:

* **E-Book:** `downloadURL`
* **Audiobook:** `narrator`, `duration`, `timeByChapter`
* **Printed Book:** `stockLevel`, `deliveryTime`

All entities include a **productType** field (`ebook`, `audiobook`, or `printedBook`) to help applications recognize each document’s structure.

> 💡 **Golden Rule:** Data that’s accessed together should be stored together — hence, all book types go in the same `books` collection.

---

## 🧩 Implementation & Design

* The inheritance pattern results in **polymorphic documents** within the same collection.
* Best to plan for it **during the design phase**, but it can be **applied later** using MongoDB’s **Aggregation Framework**.

---

## 🧮 Applying the Inheritance Pattern via Aggregation

### 🔹 First Pipeline

* Add fields:

  * `productType: "unspecified"`
  * `productID`
* Combine fields:

  * Merge `details` and `desc` → `description`
* Rename field:

  * `author` → `authors` (convert to array)
* Save updates to `Books` collection.

### 🔹 Second Pipeline

* Identify and update specific document types:

  * If `lengthMinutes ≥ 0` → `productType = "audiobook"`
  * Similar rules apply for `ebook` and `printedBook`.

After running both pipelines:

* Fields become standardized (`description`, `authors[]`).
* Each document has the correct `productType`.

---

## ✅ Key Takeaways

* **Inheritance Pattern** lets different but related entities coexist in one collection.
* **`productType`** identifies each document’s structure.
* **Aggregation Framework** can transform existing data to fit this model.
* Promotes **efficient querying** and **simplifies application logic**.

# 💻 Code Summary: Inheritance Pattern (MongoDB)

## 🧩 Step 1: Apply Inheritance Pattern to All Documents

**Goal:** Add `product_type`, `product_id`, and make shared fields consistent.

```js
var apply_inheritance_pattern_to_books_pipeline = [
  {
    $project: {
      _id: "$_id",
      product_id: "$product_id",
      product_type: { $ifNull: ["$product_type", "Unspecified"] },
      description: {
        $ifNull: ["$desc", "$description", "$details", "Unspecified"],
      },
      authors: { $ifNull: ["$authors", ["$author"], "Unspecified"] },
      publisher: "$publisher",
      language: "$language",
      pages: "$pages",
      catalogues: "$catalogues",
      eformats: "$eformats",
      isbn10: "$isbn10",
      isbn13: "$isbn13",
      narrator: "$narrator",
      length_minutes: "$length_minutes",
    },
  },
  {
    $merge: {
      into: "books",
      on: "_id",
      whenMatched: "replace",
      whenNotMatched: "discard",
    },
  },
];

db.books.aggregate(apply_inheritance_pattern_to_books_pipeline);
```

### 🔹 What It Does

* Adds a default `product_type: "Unspecified"`
* Merges `desc`, `description`, and `details` → **`description`**
* Converts `author` → **`authors[]`** (array format)
* Replaces all existing documents in `books` collection with updated structure

---

## 🧩 Step 2: Update Audiobook Entries

**Goal:** Set `product_type` to `"audiobook"` for documents with `length_minutes ≥ 0`.

```js
var cleanup_audiobook_entries_in_book_pipeline = [
  {
    $match: {
      $and: [{ product_type: "Unspecified" }, { length_minutes: { $gte: 0 } }],
    },
  },
  { $set: { product_type: "audiobook" } },
  {
    $merge: {
      into: "books",
      on: "_id",
      whenMatched: "replace",
      whenNotMatched: "discard",
    },
  },
];

db.books.aggregate(cleanup_audiobook_entries_in_book_pipeline);
```

### 🔹 What It Does

* Finds documents where:

  * `product_type` = `"Unspecified"`
  * `length_minutes ≥ 0`
* Updates their `product_type` to `"audiobook"`

---

## 🧩 Step 3: Verify Updated Document

```js
db.books.find({ _id: 3 })
```

### ✅ Example Output

```js
{
  _id: 3,
  product_id: 54538756,
  product_type: 'audiobook',
  description: 'The complete book of MongoDB by its employees',
  authors: ['Eoin Brazil'],
  publisher: "O'Reilly",
  language: 'English',
  narrator: 'Eoin Brazil',
  length_minutes: 1200
}
```

---

## 🧠 Summary

* **Aggregation Framework** used to transform documents.
* **Standardized structure:** unified `description`, array `authors`.
* **Dynamic typing:** identifies document shape via `product_type`.
* Enables **polymorphic storage** — eBooks, audiobooks, and printed books coexist in one collection.

# 📊 Code Summary: Computed Pattern (MongoDB)

## 🧩 Purpose

Implements a **roll-up aggregation** to create summary documents per `product_type`.
Each summary shows:

* Total number of books (`count`)
* Average number of authors per book (`averageNumberOfAuthors`)

---

## 🧠 Aggregation Pipeline

```js
var roll_up_product_type_and_number_of_authors_pipeline = [
  {
    $group: {
      _id: "$product_type",
      count: { $sum: 1 },
      averageNumberOfAuthors: { $avg: { $size: "$authors" } },
    },
  },
];

db.books.aggregate(roll_up_product_type_and_number_of_authors_pipeline);
```

### 🔹 Explanation

* **`$group`** — Groups documents by `product_type`.
* **`$sum: 1`** — Counts total books in each group.
* **`$size: "$authors"`** — Counts number of authors per document.
* **`$avg`** — Calculates average number of authors per book type.

---

## 📈 Example Output

```js
[
  { _id: 'audiobook', count: 1, averageNumberOfAuthors: 1 },
  { _id: 'ebook', count: 1, averageNumberOfAuthors: 3 },
  { _id: 'book', count: 1, averageNumberOfAuthors: 3 }
]
```

---

## 🧩 Summary

* **Computed Pattern** aggregates and summarizes data dynamically.
* Useful for analytics like totals, averages, and summaries.
* Reduces query complexity by precomputing common metrics.

✅ **Code Summary: Extended Reference Pattern**

This aggregation pipeline demonstrates how to **extend reference data** by embedding related product details (from the `books` collection) into documents in the `reviews` collection.

---

### **Step-by-Step Breakdown**

1. **$lookup – Join Data Across Collections**

   ```js
   {
     $lookup: {
       from: "books",
       localField: "product_id",
       foreignField: "product_id",
       as: "product_info",
     },
   }
   ```

   * Joins each `reviews` document with the matching `books` document based on `product_id`.
   * The matching book details are stored in a new array field called `product_info`.

---

2. **$unwind – Flatten the Joined Array**

   ```js
   {
     $unwind: {
       path: "$product_info",
       includeArrayIndex: "string",
       preserveNullAndEmptyArrays: false,
     },
   }
   ```

   * Converts the `product_info` array into individual documents.
   * Ensures each review has one corresponding book document (since `product_info` contains one element per match).

---

3. **$project – Reshape Document Structure**

   ```js
   {
     $project: {
       _id: "$_id",
       "product.product_id": "$product_id",
       "product.product_type": "$product_info.product_type",
       "product.title": "$product_info.title",
       "review.user_id": "$user_id",
       "review.reviewTitle": "$reviewTitle",
       "review.reviewBody": "$reviewBody",
       "review.date": "$date",
       "review.stars": "$stars",
     },
   }
   ```

   * Creates a **nested structure** separating product info and review details.
   * Produces a clean and logical layout:

     ```js
     {
       _id: ...,
       product: {
         product_id: ...,
         product_type: ...,
         title: ...
       },
       review: {
         user_id: ...,
         reviewTitle: ...,
         reviewBody: ...,
         date: ...,
         stars: ...
       }
     }
     ```

---

4. **$merge – Update the Original Collection**

   ```js
   {
     $merge: {
       into: "reviews",
       on: "_id",
       whenMatched: "replace",
       whenNotMatched: "discard",
     },
   }
   ```

   * Replaces the existing documents in the `reviews` collection with the newly reshaped versions.
   * Keeps document `_id` intact.
   * Prevents insertion of new documents that didn’t match any original (`whenNotMatched: "discard"`).

---

5. **Execution**

   ```js
   db.reviews.aggregate(reshape_review_docs_pipeline)
   ```

   * Runs the aggregation pipeline on the `reviews` collection.
   * Produces an updated `reviews` collection with **embedded product details**—creating an *extended reference* between collections.

---

### **Summary**

This pipeline performs a **denormalization** step — enriching review documents with book information, improving read performance at the cost of data redundancy.
It’s commonly used in analytics or when you want a single collection containing both product and review data.
