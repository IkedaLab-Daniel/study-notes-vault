# Relational to Document Model
## MongoDB Data Modeling for Relational Developers

### From Relational Schemas to Document Models

* In relational databases, data modeling relies on **tables, rows, columns, and strict schemas** defined upfront.
* Schema changes often require **costly migrations**.
* Data is typically **normalized** (third normal form), meaning each entity exists in only one place and relationships are managed with **primary and foreign keys**.
* Example: a bookstore app needs separate tables for **books, authors, reviews, and users**, connected through joins.

### MongoDB’s Different Design Philosophy

* MongoDB uses a **document model**, where data is stored as **JSON-like documents** inside **collections**.
* A **document** is similar to a row.
* A **collection** is similar to a table.
* Each document has a unique `_id`, comparable to a primary key.
* Fields are key–value pairs, like columns.

Instead of designing around normalization first, MongoDB encourages you to:

> **Design based on workload and query patterns.**

### Golden Rule of MongoDB

* **Data that is accessed together should be stored together.**

This often means embedding related data instead of spreading it across many collections.

### Core MongoDB Modeling Features

#### Polymorphism

* Documents in the same collection can have **different structures**.
* Example: print books and ebooks can coexist in one `books` collection without forcing unused fields to be null.
* This avoids rigid schemas and makes adapting to new requirements easier.

#### Arrays

* Fields can contain arrays (including arrays of documents).
* Example: genres stored as an array of strings.
* This enables natural representation of one-to-many relationships directly inside a document.

#### Embedded Documents

* Related data (like reviews) can be stored inside a parent document (like a book).
* This allows complex queries—such as finding books reviewed by a specific user—to be done in **a single operation**, without expensive joins.

### Query Simplicity and Performance

* Embedded data enables fast, natural queries.
* The same operation in SQL would require **multiple joins across several tables**.
* MongoDB returns structured results that closely match application objects.

### Normalization Is Still Possible

* MongoDB also supports **referencing** documents (similar to foreign keys).
* You can simulate joins using `$lookup`.
* You’re free to:

  * Embed data
  * Reference data
  * Or use a hybrid approach

The choice depends entirely on your application’s access patterns.

### Schema Validation

* Although MongoDB is flexible, it supports **database-level schema validation**.
* You can enforce rules and constraints similar to relational databases.
* Validation works with polymorphic collections and embedded documents.

### Key Takeaways

* MongoDB stores data as **documents (JSON-like objects)**.
* Documents live in **collections**.
* Schemas are **flexible**, enabling polymorphism.
* MongoDB supports **arrays and embedded documents**.
* You can both embed and normalize data as needed.
* Schema validation is available for stricter consistency.
* Most important principle:

> **Store together what you query together.**

With a small mindset shift from table-first to query-first design, relational developers can fully leverage MongoDB’s document model for simpler queries, better performance, and more adaptable schemas.

