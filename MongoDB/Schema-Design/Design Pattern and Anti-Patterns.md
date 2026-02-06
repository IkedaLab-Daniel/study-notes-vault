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
