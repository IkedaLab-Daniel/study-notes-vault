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
