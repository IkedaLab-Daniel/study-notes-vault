# Schema Design Patterns and Anti-patterns

## MongoDB Inheritance Pattern (Polymorphic Documents)

### What the Inheritance Pattern Is

* The **inheritance pattern** lets you store different but related document types in the **same collection**.
* It’s built on **polymorphism**, meaning documents in one collection can have **different shapes**.
* A **parent concept** defines shared fields, while **child variants** add their own specific fields.
* A discriminator field (commonly called `productType`) identifies each document’s shape.

Use this pattern when:

* Your entities have **more similarities than differences**
* You frequently **query them together**
* You want to avoid splitting them across multiple collections

### Bookstore Example

All books (ebooks, audiobooks, printed books) share fields like:

* title
* author(s)
* genres
* price
* publisher

Each type also has unique fields:

* **Ebook**: download URL, supported formats
* **Audiobook**: narrator, duration, chapter timings
* **Printed book**: stock level, delivery time

A `productType` field (ebook / audiobook / printed) tells applications how to interpret each document.

Result:

* One **books** collection
* Multiple **document shapes**
* Shared fields + type-specific fields
* Queries can fetch *all books at once* while still supporting media-specific logic

This follows MongoDB’s golden rule:

> **Data that is accessed together should be stored together.**

### Why This Matters

* Avoids unnecessary collections and joins
* Keeps related data together
* Makes querying simpler and faster
* Adapts easily as new product types appear

### Applying the Pattern to Existing Data (Aggregation Framework)

Real systems often start messy. MongoDB’s **aggregation framework** lets you refactor existing collections to follow the inheritance pattern.

Typical steps:

#### First pipeline

* Add `productType` (initially set to `"unspecified"`)
* Add `productId`
* Normalize shared fields:

  * Merge fields like `details` / `desc` → `description`
  * Rename `author` → `authors`
  * Convert `authors` from string to array

#### Second pipeline (and others like it)

* Detect document type based on existing fields:

  * `lengthMinutes` → audiobook
  * `pages` → printed book
  * `eformats` → ebook
* Update `productType` accordingly

After running these pipelines:

* Documents have consistent shared fields
* Each document is tagged with the correct `productType`
* Polymorphic structure is fully applied

### Key Takeaways

* The **inheritance pattern** stores related but different documents in one collection.
* A **type field** (like `productType`) identifies each document’s shape.
* Shared fields live at the top level; unique fields live per subtype.
* MongoDB’s **aggregation framework** can retrofit this pattern onto existing data.
* This approach simplifies queries, improves performance, and supports evolving schemas.

### Code Summary: Inheritance Pattern
To apply the Inheritance Pattern to documents in a collection, you can use the aggregation framework.

This first example updates all book documents with a new “product type” field to identify the shape of the ebook, printed book, and audiobook documents. The pipeline also adds a product_id field for all documents and makes shared attributes more consistent. It does this by changing desc and details fields to description and by converting the author field to an array. Finally, it replaces the existing documents in the same collection.
```js
var apply_inheritance_pattern_to_books_pipeline = [
  {
    $project: {
      _id: "$_id",
      product_id: "$product_id",
      product_type: {
        $ifNull: ["$product_type", "Unspecified"],
      },
      description: {
        $ifNull: [
          "$desc",
          "$description",
          "$details",
          "Unspecified",
        ],
      },
      authors: {
        $ifNull: [
          "$authors",
          ["$author"],
          "Unspecified",
        ],
      },
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
]

db.books.aggregate(apply_inheritance_pattern_to_books_pipeline)
```
### The next pipeline changes all documents with a product type of “unspecified” with a minute length greater than zero to “audiobook” and saves them to the collection.
```js
var cleanup_audiobook_entries_in_book_pipeline = [
  {
    $match: {
      $and: [{ product_type: "Unspecified" }, { length_minutes: { $gte: 0 } }],
    },
  },
  {
    $set: { product_type: "audiobook" },
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

db.books.aggregate(cleanup_audiobook_entries_in_book_pipeline);
Finally, we ran the following command to find one of the updated documents in order to view the changes.

db.books.find({ _id: 3 })
[
  {
    _id: 3,
    product_id: 54538756,
    product_type: 'audiobook',
    description: 'The complete book of MongoDB by its employees',
    authors: [ 'Eoin Brazil' ],
    publisher: "O'Reilly",
    language: 'English',
    narrator: 'Eoin Brazil',
    length_minutes: 1200
  }
]
```

## MongoDB Computed Pattern (Precomputing for Performance)

### What the Computed Pattern Is

The **computed pattern** improves performance by **precomputing expensive values when data changes** (on write or on schedule) instead of recalculating them every time users read data.

This avoids repeated calculations and is especially important at scale (for example, millions or billions of reviews).

In short:

> **Compute once, read many.**

### Mathematical Computations (Example: Average Star Rating)

Problem:
Calculating a book’s average rating on every page view would require scanning many review documents repeatedly.

Solution:
Store the computed values directly in the **book document**.

Add a `rating` subdocument:

* `reviewCount` – total number of reviews
* `average` – current average star rating

When a new review arrives:

1. Multiply the old average by the old review count
2. Add the new star rating
3. Increment the review count
4. Divide by the new total review count
5. Store the updated values back in the book document

Result:

* Ratings are updated **only when a review is written**
* Product pages read **one document**
* No repeated aggregation over the reviews collection

Much faster and more scalable.

### Roll-Up Operations (Aggregating Groups of Data)

Roll-ups summarize many documents into higher-level views, such as:

* hourly → daily → monthly
* per-book → per-product-type

Example requirement:

Stakeholders want, per product type:

* Total number of books
* Average number of authors

Instead of computing this on every request:

* Run an aggregation pipeline on a schedule (for example, daily)
* Store the results in summary documents

Typical pipeline steps:

1. **Group** by `productType`
2. **$sum** to count books
3. **$size** to count authors per book
4. **$avg** to compute average authors per product type

This produces compact summary documents for audiobooks, ebooks, and printed books.

This approach is ideal when:

* Writes are frequent
* Slightly stale data is acceptable
* Reports don’t need real-time precision

### Key Takeaways

* The **computed pattern** shifts work from reads to writes (or scheduled jobs).
* It stores precomputed results for fast access.
* Two common forms:

  * **Mathematical computations** (like averages, totals)
  * **Roll-ups** (grouped summaries over time or categories)
* This pattern dramatically improves performance and scalability by eliminating repeated calculations during reads.

### Code Summary: Computed Pattern
In this example, we implemented a roll-up operation which results in a summary document for each book type. The summary document includes the number of books and average number of authors for each product type.

The $sum operator increments the count of books for each type. The $size operator gets the number of authors in the authors array which is then averaged for the type using the $avg operator.
```js
var roll_up_product_type_and_number_of_authors_pipeline = [
  {
    $group: {
      _id: "$product_type",
      count: {
        $sum: 1,
      },
      averageNumberOfAuthors: {
        $avg: {
          $size: "$authors",
        },
      },
    },
  },
]
```
Finally, we run the aggregation by using the aggregate method on the books collection, passing in the roll up pipeline as an argument.
```js
db.books.aggregate(roll_up_product_type_and_number_of_authors_pipeline)
The resulting documents look like this:

[
  { _id: 'audiobook', count: 1, averageNumberOfAuthors: 1 },
  { _id: 'ebook', count: 1, averageNumberOfAuthors: 3 },
  { _id: 'book', count: 1, averageNumberOfAuthors: 3 }
]
```

## Extended Reference Pattern

### Code Summary: Extended Reference Pattern
The following pipeline creates an extended reference by updating all documents in the reviews collection to include relevant product information from the books collection using the $lookup stage.

```js
var reshape_review_docs_pipeline = [
  {
    $lookup: {
      from: "books",
      localField: "product_id",
      foreignField: "product_id",
      as: "product_info",
    },
  },
  {
    $unwind: {
      path: "$product_info",
      includeArrayIndex: "string",
      preserveNullAndEmptyArrays: false,
    },
  },
  {
    $project: {
      _id: "$_id",
      "product.product_id": "$product_id",
      "product.product_type":
        "$product_info.product_type",
      "product.title": "$product_info.title",
      "review.user_id": "$user_id",
      "review.reviewTitle": "$reviewTitle",
      "review.reviewBody": "$reviewBody",
      "review.date": "$date",
      "review.stars": "$stars",
    },
  },
  {
    $merge: {
      into: "reviews",
      on: "_id",
      whenMatched: "replace",
      whenNotMatched: "discard",
    },
  },
]

db.reviews.aggregate(reshape_review_docs_pipeline)
```

Once our new document with the extended reference is formed we use the $merge stage to merge the output into the existing reviews collection.
```js
...
 {
    $merge: {
      into: "reviews",
      on: "_id",
      whenMatched: "replace",
      whenNotMatched: "discard",
    },
  },

...
Finally, we run the aggregation pipeline by invoking the aggregate method on the reviews collection, passing in the pipeline variable.

db.reviews.aggregate(reshape_review_docs_pipeline)
```

## Unbounded Array Antipattern in MongoDB

### What Is an Unbounded Array?

An **unbounded array** is a document field that keeps growing without limit (for example, embedding all reviews inside a single book document).

This is dangerous because:

* Documents can exceed MongoDB’s **16 MB BSON size limit**
* Index performance degrades as arrays grow
* Large documents strain application memory and network resources

### Why It Happens

MongoDB encourages embedding data that’s accessed together, often using arrays.
But when the “many” side of a one-to-many relationship grows indefinitely (like reviews on a popular book), embedding everything becomes an antipattern.

### Rules of Thumb to Avoid Unbounded Arrays

* Only embed data that is **queried together**
* Arrays should **not grow without bounds**
* Avoid embedding **high-cardinality** data

### Fixing the Antipattern

Two schema patterns help control array growth:

### Extended Reference Pattern

* Move child documents (reviews) into their own collection
* Duplicate relevant parent data (book info) into each review
* Remove the reviews array from the book document

**Downsides in the bookstore case:**

* Heavy data duplication
* More complex queries
* Must fetch book info from reviews
* Poor fit when books remain the primary entity

### Subset Pattern (Best Fit for This Use Case)

* Store **all reviews** in a separate `reviews` collection
* Embed only a **small, frequently accessed subset** (for example, top 3 reviews) in the book document

Benefits:

* Eliminates unbounded arrays
* Keeps commonly used data together
* Avoids `$lookup` for the main book page
* Controls document size
* Accepts minor duplication for major performance gains

Since the bookstore only displays **three reviews** on the book page, embedding just those while storing the rest separately is the optimal design.

### Key Takeaways

* The unbounded array antipattern occurs when embedded arrays grow without limit
* It risks document size limits and hurts performance
* Avoid by:

  * Embedding only what’s queried together
  * Preventing unlimited array growth
  * Not embedding high-cardinality data
* Two main solutions:

  * **Extended Reference Pattern**
  * **Subset Pattern**
* Choose based on your application’s access patterns and business needs

The golden rule still applies:

> **Store together what you query together — but only in controlled amounts.**

## Bloated Documents Antipattern in MongoDB

### What Is the Bloated Documents Antipattern?

Bloated documents happen when **all related data is stored in a single document**, even when different parts of that data are accessed at different times.

This violates MongoDB’s practical rule:

> **Store together what is accessed together — not everything that’s related.**

Bloated documents increase average document size, which inflates the **working set** (frequently accessed data). When the working set no longer fits in memory, performance drops.

### Why This Hurts Performance

MongoDB (via WiredTiger) relies on an **internal cache** to keep frequently used documents and indexes in RAM.

* If the working set fits in cache → fast queries
* If it exceeds cache → disk reads → slow pages

In the bookstore example:

* Homepage randomly loads books → *all book documents become part of the working set*
* Average book document size ≈ 1.12 KB
* Hundreds of thousands of books → logical data size ≈ 500+ MB
* WiredTiger cache ≈ 512 MB

Once indexes and other data are included, the working set **exceeds memory**, causing homepage slowness.

### How to Detect the Problem

Estimate logical data size:

* Logical size = number of documents × average document size
* Use `db.collection.stats()` to get both values

If this approaches or exceeds WiredTiger cache, you likely have bloated documents.

### Two Possible Fixes

1. Add more RAM (costly)
2. Improve the data model (preferred)

### The Real Fix: Split by Access Pattern

Only a few fields are used on the homepage (for example: `title`, `author`).
Most fields are only needed on the details page.

So the solution is to **split the document**:

### Summary Collection

* Contains lightweight fields used frequently (title, author, etc.)
* Very small documents (~79 bytes)
* Fits easily in memory

### Details Collection

* Stores large, infrequently accessed fields
* Queried only when viewing book details

After splitting:

* Working set drops to ~35 MB
* Fits comfortably in cache
* Performance is restored

### Key Takeaways

* Bloated documents store data that is accessed separately in one document
* This increases working set size and degrades performance
* Diagnose by estimating logical data size vs cache size
* Fix by separating documents based on **access patterns**, not just relationships

### Golden Reminder

> **Design for how your application reads data — not just how entities relate.**

Splitting documents into “summary” and “details” is a powerful way to keep hot data small and fast.

###  Code Summary: Bloated Documents
To retrieve the number of documents in a collection using the stats() method in mongosh, use the following:
```js
db.collection.stats().count
```
To retrieve the average size of documents in a collection using the stats() method in mongosh, use the following:
```js
db.collection.stats().avgObjSize
```