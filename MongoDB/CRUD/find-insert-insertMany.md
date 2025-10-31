# 🗃️ MongoDB CRUD Quick Guide

## 📍 Basic Commands Overview

MongoDB provides several key methods for working with documents in a collection.
Here we focus on the most common:

* `find()` → Read documents
* `insertOne()` → Insert a single document
* `insertMany()` → Insert multiple documents

---

## 🔍 FIND — Retrieve Documents

### 👉 Syntax

```js
db.collection.find(query, projection)
```

### 🔹 Parameters

* **query** *(optional)* → filter criteria
* **projection** *(optional)* → specify which fields to include/exclude

### 🧩 Examples

```js
// Find all documents
db.users.find()

// Find users aged 18
db.users.find({ age: 18 })

// Find users aged above 20
db.users.find({ age: { $gt: 20 } })

// Find users with only name and age fields shown
db.users.find({}, { name: 1, age: 1, _id: 0 })

// Find one matching document
db.users.findOne({ username: "tetey" })
```

### 🧠 Notes

* Returns a **cursor** (use `.toArray()` in Node.js to convert to list)
* Use **comparison operators**:

  * `$gt` (greater than)
  * `$lt` (less than)
  * `$gte`, `$lte`
  * `$ne` (not equal)
  * `$in`, `$nin`

---

## ✏️ INSERTONE — Insert a Single Document

### 👉 Syntax

```js
db.collection.insertOne(document)
```

### 🧩 Example

```js
db.users.insertOne({
  name: "Lester",
  age: 19,
  email: "lester@example.com"
})
```

### 🧠 Notes

* Automatically adds an `_id` field if not specified.
* Returns:

  ```js
  { acknowledged: true, insertedId: ObjectId("...") }
  ```

---

## 🧾 INSERTMANY — Insert Multiple Documents

### 👉 Syntax

```js
db.collection.insertMany([doc1, doc2, ...])
```

### 🧩 Example

```js
db.users.insertMany([
  { name: "Tetey", age: 20 },
  { name: "Hermogino", age: 19 },
  { name: "Lester", age: 21 }
])
```

### 🧠 Notes

* Inserts all documents in one operation.
* Returns:

  ```js
  { acknowledged: true, insertedIds: { '0': ObjectId(...), '1': ObjectId(...), ... } }
  ```
* If one document fails (e.g., duplicate `_id`), the operation **stops** unless `{ ordered: false }` is set:

  ```js
  db.users.insertMany([...], { ordered: false })
  ```

---

## 🧮 Useful Tips

| Purpose                            | Command                                                        |
| ---------------------------------- | -------------------------------------------------------------- |
| Count documents                    | `db.collection.countDocuments(query)`                          |
| Limit results                      | `db.collection.find().limit(5)`                                |
| Sort results                       | `db.collection.find().sort({ age: 1 })` *(1 = asc, -1 = desc)* |
| Pretty-print results (Mongo shell) | `db.collection.find().pretty()`                                |

---

✅ **Summary**

| Action        | Method         | Description                 |
| ------------- | -------------- | --------------------------- |
| Read          | `find()`       | Retrieve multiple documents |
| Read (single) | `findOne()`    | Retrieve one document       |
| Create        | `insertOne()`  | Insert a single document    |
| Create (bulk) | `insertMany()` | Insert multiple documents   |