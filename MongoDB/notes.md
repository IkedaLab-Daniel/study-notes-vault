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
