# 🔍 FINDING DOCUMENTS IN MONGODB

## 📘 1. `find()` — Retrieve Multiple Documents

### 👉 Syntax

```js
db.collection.find(query, projection)
```

### 🔹 Parameters

* **query (optional)** → filters which documents to return
* **projection (optional)** → selects which fields to include/exclude

### 🧩 Examples

```js
// Get all documents
db.users.find()

// Get users where age equals 18
db.users.find({ age: 18 })

// Get users older than 18
db.users.find({ age: { $gt: 18 } })

// Get users whose name is either "Lester" or "Tetey"
db.users.find({ name: { $in: ["Lester", "Tetey"] } })

// Get users where age is NOT 20
db.users.find({ age: { $ne: 20 } })

// Include only "name" and "age", exclude "_id"
db.users.find({}, { name: 1, age: 1, _id: 0 })
```

### 🧠 Notes

* Returns a **cursor** — in Mongo shell, it automatically prints results.
* In Node.js, use:

  ```js
  const users = await db.collection('users').find({}).toArray();
  ```
* Use `.limit()`, `.sort()`, and `.skip()` for pagination and ordering.

---

## 📘 2. `findOne()` — Retrieve a Single Document

### 👉 Syntax

```js
db.collection.findOne(query, projection)
```

### 🧩 Examples

```js
// Find one document where name is "Lester"
db.users.findOne({ name: "Lester" })

// Find one document with only selected fields
db.users.findOne({ name: "Lester" }, { name: 1, age: 1, _id: 0 })
```

### 🧠 Notes

* Returns **one object** (not a cursor).
* If no match found → returns `null`.

---

## 🧮 3. Query Operators

| Operator | Description      | Example                                                  |
| -------- | ---------------- | -------------------------------------------------------- |
| `$eq`    | equal to         | `{ age: { $eq: 18 } }`                                   |
| `$ne`    | not equal        | `{ age: { $ne: 18 } }`                                   |
| `$gt`    | greater than     | `{ age: { $gt: 18 } }`                                   |
| `$lt`    | less than        | `{ age: { $lt: 18 } }`                                   |
| `$gte`   | greater or equal | `{ age: { $gte: 18 } }`                                  |
| `$lte`   | less or equal    | `{ age: { $lte: 18 } }`                                  |
| `$in`    | in array         | `{ name: { $in: ["Tetey", "Lester"] } }`                 |
| `$nin`   | not in array     | `{ name: { $nin: ["Bot", "AI"] } }`                      |
| `$and`   | AND condition    | `{ $and: [{ age: { $gt: 18 } }, { age: { $lt: 30 } }] }` |
| `$or`    | OR condition     | `{ $or: [{ name: "Lester" }, { name: "Tetey" }] }`       |
| `$regex` | match pattern    | `{ name: { $regex: "^L", $options: "i" } }`              |

---

## 🧾 4. Useful Cursor Methods

| Method                | Description                          | Example                                          |
| --------------------- | ------------------------------------ | ------------------------------------------------ |
| `.limit(n)`           | Limits results                       | `db.users.find().limit(5)`                       |
| `.sort({ field: 1 })` | Sort ascending (1) / descending (-1) | `db.users.find().sort({ age: -1 })`              |
| `.skip(n)`            | Skip N documents                     | `db.users.find().skip(10)`                       |
| `.countDocuments()`   | Count matching docs                  | `db.users.countDocuments({ age: { $gte: 18 } })` |

---

✅ **Summary**

| Command                          | Returns               | Usage                             |
| -------------------------------- | --------------------- | --------------------------------- |
| `find()`                         | Cursor (many results) | For retrieving multiple documents |
| `findOne()`                      | Single document       | For retrieving one document       |
| `.limit()`, `.sort()`, `.skip()` | Cursor methods        | For controlling results           |