# 🗑️ DELETING DOCUMENTS IN MONGODB

## 📘 1. `deleteOne()` — Delete a Single Document

### 👉 Syntax

```js
db.collection.deleteOne(filter)
```

### 🔹 Parameters

* **filter** → criteria that matches the document you want to delete

### 🧩 Examples

```js
// Delete one document where name is "Lester"
db.users.deleteOne({ name: "Lester" })

// Delete by ID
db.users.deleteOne({ _id: ObjectId("652b9a56f5c0a1234abcd678") })
```

### 🧠 Notes

* Only the **first matching document** is removed.
* If no document matches → nothing happens (no error).

---

## 📘 2. `deleteMany()` — Delete Multiple Documents

### 👉 Syntax

```js
db.collection.deleteMany(filter)
```

### 🧩 Examples

```js
// Delete all users with age below 18
db.users.deleteMany({ age: { $lt: 18 } })

// Delete all users with "guest" role
db.users.deleteMany({ role: "guest" })

// Delete all documents in a collection (⚠️ use carefully!)
db.users.deleteMany({})
```

### 🧠 Notes

* Deletes **all documents** that match the condition.
* Use `{}` as filter to remove *everything* in the collection.

---

## 🧾 3. Delete Result Object

MongoDB returns a summary object after each delete operation:

```js
{
  acknowledged: true,
  deletedCount: 3
}
```

### 🔹 Example

```js
const result = await db.users.deleteMany({ age: { $lt: 18 } })
console.log(result.deletedCount) // number of deleted documents
```

---

## ⚠️ 4. Dropping a Collection

To completely remove an entire collection (structure + data):

```js
db.users.drop()
```

✅ Returns `true` if the collection was successfully dropped.

---

## ✅ Summary

| Action          | Method           | Description                            |
| --------------- | ---------------- | -------------------------------------- |
| Delete One      | `deleteOne()`    | Removes the first matching document    |
| Delete Many     | `deleteMany()`   | Removes all matching documents         |
| Delete All      | `deleteMany({})` | Removes every document in a collection |
| Drop Collection | `drop()`         | Deletes the entire collection          |