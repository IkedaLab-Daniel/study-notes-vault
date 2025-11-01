# 🔗 LOGICAL OPERATORS IN MONGODB

Logical operators are used to **combine or invert query conditions**.
They are most commonly used inside the `find()` query to match documents based on **multiple criteria**.

---

## ⚙️ 1. `$and` — Logical AND

Matches documents that **satisfy all** the given conditions.

### 👉 Syntax

```js
{ $and: [ { condition1 }, { condition2 }, ... ] }
```

### 🧩 Examples

```js
// Find users aged between 18 and 30
db.users.find({
  $and: [
    { age: { $gte: 18 } },
    { age: { $lte: 30 } }
  ]
})

// Equivalent shorthand (no $and needed when using different fields)
db.users.find({ age: { $gte: 18, $lte: 30 } })
```

### 🧠 Notes

* `$and` explicitly combines multiple conditions.
* Useful when conditions use the **same field multiple times** (e.g., range checks).

---

## ⚙️ 2. `$or` — Logical OR

Matches documents that **satisfy at least one** of the conditions.

### 👉 Syntax

```js
{ $or: [ { condition1 }, { condition2 }, ... ] }
```

### 🧩 Examples

```js
// Find users whose name is "Lester" OR "Tetey"
db.users.find({
  $or: [
    { name: "Lester" },
    { name: "Tetey" }
  ]
})

// Find users younger than 18 OR with status "minor"
db.users.find({
  $or: [
    { age: { $lt: 18 } },
    { status: "minor" }
  ]
})
```

### 🧠 Notes

* Returns all documents that match **any** condition in the array.
* Combine with `$and` for more complex queries.

---

## ⚙️ 3. `$not` — Logical NOT

Inverts the effect of a query expression.
Returns documents **that do not match** the condition.

### 👉 Syntax

```js
{ field: { $not: { operator } } }
```

### 🧩 Examples

```js
// Find users NOT older than 18
db.users.find({ age: { $not: { $gt: 18 } } })

// Find users whose name does NOT start with "L"
db.users.find({ name: { $not: { $regex: "^L" } } })
```

### 🧠 Notes

* `$not` must be applied to **operators** like `$gt`, `$regex`, etc.
* It cannot stand alone as a top-level operator.

---

## ⚙️ 4. `$nor` — Logical NOR

Matches documents that **fail all** the given conditions.
(Think: “not this, and not that”)

### 👉 Syntax

```js
{ $nor: [ { condition1 }, { condition2 }, ... ] }
```

### 🧩 Examples

```js
// Find users who are NOT named "Lester" and NOT aged 18
db.users.find({
  $nor: [
    { name: "Lester" },
    { age: 18 }
  ]
})

// Find users who are neither "admin" nor "staff"
db.users.find({
  $nor: [
    { role: "admin" },
    { role: "staff" }
  ]
})
```

### 🧠 Notes

* `$nor` returns documents that **do not match any** of the listed conditions.
* Useful for **exclusions** and filtering out multiple unwanted matches.

---

## ✅ Summary Table

| Operator | Description         | Returns Documents That…          | Example                                                    |
| -------- | ------------------- | -------------------------------- | ---------------------------------------------------------- |
| `$and`   | All conditions true | Match **all** criteria           | `{ $and: [ { age: { $gt: 18 } }, { status: "active" } ] }` |
| `$or`    | Any condition true  | Match **at least one** criterion | `{ $or: [ { name: "Lester" }, { name: "Tetey" } ] }`       |
| `$not`   | Invert condition    | **Do not match** condition       | `{ age: { $not: { $gt: 18 } } }`                           |
| `$nor`   | None true           | Fail **all** listed conditions   | `{ $nor: [ { role: "admin" }, { role: "staff" } ] }`       |
