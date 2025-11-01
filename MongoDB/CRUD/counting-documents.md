# 🔢 COUNTING DOCUMENTS IN A MONGODB COLLECTION

You can count how many documents exist in a collection — either **all documents** or only those that **match specific conditions**.
MongoDB provides the `countDocuments()` method for this purpose.

---

## 📘 1. Basic Syntax

```js
db.collection.countDocuments(<query>, <options>)
```

* `<query>` → filters which documents to count
* `<options>` → optional settings (e.g., limit, skip)

---

## 📘 2. Count All Documents in a Collection

### 👉 Example

```js
// Count all documents in the 'trips' collection
db.trips.countDocuments({})
```

### 🧠 Notes

* Passing an **empty query `{}`** counts *all* documents.
* Useful for checking the total size of a collection.

---

## 📘 3. Count Documents Matching a Query

### 👉 Example

```js
// Count trips longer than 120 minutes by subscribers
db.trips.countDocuments({
  tripduration: { $gt: 120 },
  usertype: "Subscriber"
})
```

### 🧠 Notes

* Combines **comparison** and **logical operators** just like `.find()`.
* Returns an integer count of matching documents.

---

## 📘 4. Counting with Conditions

### 🧩 Example

```js
// Count accounts that include 'InvestmentStock' in products
db.accounts.countDocuments({ products: "InvestmentStock" })
```

### 🧠 Notes

* Works with arrays — counts documents that contain at least one matching value.

---

## 📘 5. Counting with Options

### 👉 Example

```js
// Count only first 1000 documents that match
db.trips.countDocuments(
  { usertype: "Subscriber" },
  { limit: 1000 }
)
```

### 🧠 Notes

* `limit` and `skip` can control which subset of documents are counted.
* Useful for pagination or sampling.

---

## 📘 6. Alternative: Estimated Count (Faster)

If you just need an **approximate count of all documents** (without filtering), use:

```js
db.collection.estimatedDocumentCount()
```

### 🧠 Notes

* Much faster than `countDocuments()` since it doesn’t scan all documents.
* Returns an **estimated** total — not guaranteed to be exact during heavy writes.

---

## ✅ Summary Table

| Method                     | Description                            | Example                                               |
| -------------------------- | -------------------------------------- | ----------------------------------------------------- |
| `countDocuments()`         | Counts documents matching a query      | `db.trips.countDocuments({ usertype: "Subscriber" })` |
| `countDocuments({})`       | Counts all documents in the collection | `db.trips.countDocuments({})`                         |
| `estimatedDocumentCount()` | Fast estimate of total documents       | `db.trips.estimatedDocumentCount()`                   |
| With options               | Limit/skips count scope                | `db.trips.countDocuments({}, { limit: 1000 })`        |