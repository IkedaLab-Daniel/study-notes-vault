# 🛠️ UPDATING DOCUMENTS IN MONGODB

## 📘 1. `updateOne()` — Update a Single Document

### 👉 Syntax

```js
db.collection.updateOne(filter, update, options)
```

### 🔹 Parameters

* **filter** → criteria to find the document
* **update** → defines what changes to apply (uses update operators like `$set`)
* **options (optional)** → `{ upsert: true }` to insert if no match

### 🧩 Examples

```js
// Update one user's age
db.users.updateOne(
  { name: "Lester" },
  { $set: { age: 20 } }
)

// Add a new field if not existing
db.users.updateOne(
  { name: "Lester" },
  { $set: { email: "lester@example.com" } }
)

// Increment a numeric field
db.users.updateOne(
  { name: "Lester" },
  { $inc: { loginCount: 1 } }
)

// Add element to array
db.users.updateOne(
  { name: "Lester" },
  { $push: { hobbies: "coding" } }
)
```

---

## 📘 2. `updateMany()` — Update Multiple Documents

### 👉 Syntax

```js
db.collection.updateMany(filter, update, options)
```

### 🧩 Examples

```js
// Set all users under 18 as "minor"
db.users.updateMany(
  { age: { $lt: 18 } },
  { $set: { status: "minor" } }
)

// Increment all ages by 1
db.users.updateMany({}, { $inc: { age: 1 } })

// Push a tag to all documents with a certain role
db.users.updateMany(
  { role: "admin" },
  { $push: { tags: "trusted" } }
)
```

---

## ⚙️ 3. Common Update Operators

| Operator  | Description                              | Example                               |
| --------- | ---------------------------------------- | ------------------------------------- |
| `$set`    | Sets a field to a value                  | `{ $set: { name: "Tetey" } }`         |
| `$unset`  | Removes a field                          | `{ $unset: { oldField: "" } }`        |
| `$inc`    | Increments numeric value                 | `{ $inc: { score: 10 } }`             |
| `$mul`    | Multiplies numeric value                 | `{ $mul: { price: 1.1 } }`            |
| `$rename` | Renames a field                          | `{ $rename: { oldName: "newName" } }` |
| `$min`    | Updates if value is less than current    | `{ $min: { age: 18 } }`               |
| `$max`    | Updates if value is greater than current | `{ $max: { age: 30 } }`               |

---

## 📦 4. Array Update Operators

| Operator    | Description                      | Example                                               |
| ----------- | -------------------------------- | ----------------------------------------------------- |
| `$push`     | Add element to array             | `{ $push: { hobbies: "reading" } }`                   |
| `$addToSet` | Add only if not already in array | `{ $addToSet: { hobbies: "coding" } }`                |
| `$pull`     | Remove matching element          | `{ $pull: { hobbies: "sleeping" } }`                  |
| `$pop`      | Remove first or last element     | `{ $pop: { hobbies: 1 } }` *(1 = last, -1 = first)*   |
| `$each`     | Push multiple values             | `{ $push: { tags: { $each: ["new", "verified"] } } }` |

---

## 🧠 5. Upsert (Update or Insert)

If no document matches the filter, you can create one automatically with `{ upsert: true }`.

```js
db.users.updateOne(
  { username: "newUser" },
  { $set: { age: 18, role: "guest" } },
  { upsert: true }
)
```

✅ This will insert a new document if `"newUser"` doesn’t exist.

---

## 🧮 6. Check Results (Output Example)

MongoDB returns an object summarizing the update operation:

```js
{
  acknowledged: true,
  matchedCount: 1,
  modifiedCount: 1,
  upsertedId: null
}
```

---

## ✅ Summary

| Action             | Method         | Description                        |
| ------------------ | -------------- | ---------------------------------- |
| Update One         | `updateOne()`  | Modify the first matching document |
| Update Many        | `updateMany()` | Modify all matching documents      |
| Set value          | `$set`         | Assigns a new field value          |
| Remove field       | `$unset`       | Deletes a field                    |
| Increment number   | `$inc`         | Adds/subtracts from a number       |
| Push to array      | `$push`        | Adds new element(s)                |
| Add unique element | `$addToSet`    | Adds only if not already present   |