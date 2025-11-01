# 🧩 QUERYING ON ARRAY ELEMENTS IN MONGODB

MongoDB allows you to query documents based on **array field contents** — whether you’re matching single values, multiple values, or specific array positions.

---

## 📘 1. Match Documents Containing a Specific Value

### 👉 Example

```js
// Find users who have "coding" in their hobbies array
db.users.find({ hobbies: "coding" })
```

### 🧠 Notes

* Matches if **any element** in the array equals `"coding"`.
* No special operator is needed for simple value matching.

---

## 📘 2. Match Documents Containing Multiple Values (All Must Match)

### 👉 Example

```js
// Find users who have BOTH "coding" and "reading" in their hobbies
db.users.find({ hobbies: { $all: ["coding", "reading"] } })
```

### 🧠 Notes

* `$all` works like a **logical AND** for array elements.
* Order of array elements does **not** matter.

---

## 📘 3. Match Array Elements Using Comparison Operators

### 👉 Example

```js
// Find documents where any score is greater than 80
db.students.find({ scores: { $gt: 80 } })
```

### 🧠 Notes

* The condition applies to **each element** of the array.
* If **any element** matches, the document is returned.

---

## 📘 4. Match Array Elements at a Specific Index

### 👉 Example

```js
// Find users where the first element in 'hobbies' is 'coding'
db.users.find({ "hobbies.0": "coding" })
```

### 🧠 Notes

* Array indexes start at **0**.
* This matches based on **exact position** in the array.

---

## 📘 5. Query for Exact Array Match

### 👉 Example

```js
// Find users whose hobbies array exactly matches this order and content
db.users.find({ hobbies: ["coding", "reading", "gaming"] })
```

### 🧠 Notes

* Matches only if the **entire array** is identical in **length, order, and values**.

---

## 📘 6. `$elemMatch` — Match Specific Conditions Within a Single Array Element

### 👉 Example

```js
// Each scores array element is an object with { subject, score }
// Find students with at least one score object where both subject = "Math" and score >= 90
db.students.find({
  scores: { $elemMatch: { subject: "Math", score: { $gte: 90 } } }
})
```

### 🧠 Notes

* `$elemMatch` ensures **both conditions apply to the same array element**.
* Without `$elemMatch`, MongoDB may match values from **different elements**.

---

## 📘 7. `$size` — Match Arrays by Length

### 👉 Example

```js
// Find users with exactly 3 hobbies
db.users.find({ hobbies: { $size: 3 } })
```

### 🧠 Notes

* `$size` matches **only arrays** with the given number of elements.
* It cannot be combined with comparison operators like `$gt` or `$lt` (use `$expr` workaround for that).

---

## 📘 8. `$in` — Match Any of Multiple Values in an Array

### 👉 Example

```js
// Find users whose hobbies include either "reading" or "gaming"
db.users.find({ hobbies: { $in: ["reading", "gaming"] } })
```

### 🧠 Notes

* Returns documents where **any** array element matches one of the listed values.
* Similar to `$or` for array contents.

---

## ✅ Summary Table

| Operator             | Description                                            | Example                                                                |
| -------------------- | ------------------------------------------------------ | ---------------------------------------------------------------------- |
| *(none)*             | Match array containing a value                         | `{ hobbies: "coding" }`                                                |
| `$all`               | Match array containing **all** specified values        | `{ hobbies: { $all: ["coding", "reading"] } }`                         |
| `$gt`, `$lt`, etc.   | Compare array elements                                 | `{ scores: { $gt: 80 } }`                                              |
| `$elemMatch`         | Match multiple conditions within **one** array element | `{ scores: { $elemMatch: { subject: "Math", score: { $gte: 90 } } } }` |
| `$size`              | Match array by **number of elements**                  | `{ hobbies: { $size: 3 } }`                                            |
| `$in`                | Match if **any** array element matches                 | `{ hobbies: { $in: ["reading", "gaming"] } }`                          |
| `"arrayField.index"` | Match element at position                              | `{ "hobbies.0": "coding" }`                                            |
