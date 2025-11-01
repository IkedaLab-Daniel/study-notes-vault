# 📊 SORTING & LIMITING QUERY RESULTS IN MONGODB

MongoDB provides several ways to **order and control** how many documents you get from queries.
This is especially useful for **pagination**, **ranking**, and **displaying top results**.

---

## 📘 1. Sorting with `.sort()`

### 👉 Syntax

```js
db.collection.find(query).sort({ field: order })
```

* `order`:

  * `1` = ascending (A → Z / smallest → largest)
  * `-1` = descending (Z → A / largest → smallest)

### 🧩 Example

```js
// Sort accounts by limit in descending order
db.accounts.find().sort({ limit: -1 })

// Sort by multiple fields: limit descending, then account_id ascending
db.accounts.find().sort({ limit: -1, account_id: 1 })
```

### 🧠 Notes

* Sorting happens **after filtering** (i.e., after `.find()` conditions).
* Can impact performance if field isn’t indexed.

---

## 📘 2. Limiting Results with `.limit()`

### 👉 Syntax

```js
db.collection.find(query).limit(number)
```

### 🧩 Example

```js
// Return only the first 3 accounts
db.accounts.find().limit(3)
```

### 🧠 Notes

* `.limit()` controls how many documents are **returned** (not stored).
* Commonly used for pagination.

---

## 📘 3. Combining `.sort()` and `.limit()`

### 👉 Example

```js
// Get top 5 accounts with the highest limit
db.accounts.find().sort({ limit: -1 }).limit(5)

// Get lowest 3 accounts by limit
db.accounts.find().sort({ limit: 1 }).limit(3)
```

### 🧠 Notes

* The order matters:
  `.sort()` should come **before** `.limit()` for accurate results.
* Works well for “Top N” queries.

---

## 📘 4. Skipping Documents with `.skip()`

### 👉 Example

```js
// Skip first 5 documents, then return the next 5
db.accounts.find().sort({ limit: -1 }).skip(5).limit(5)
```

### 🧠 Notes

* Often used for **pagination**:

  * Page 1 → `.skip(0).limit(5)`
  * Page 2 → `.skip(5).limit(5)`

---

## 📘 5. Sorting & Limiting in Aggregation Pipeline (`$cursor`)

When using the **aggregation framework**, you can apply sort and limit either:

* Using `$sort` and `$limit` stages
* Or using `$cursor.sort` and `$cursor.limit` for cursor-level control (less common)

---

### ✅ Example: `$sort` and `$limit` Stages

```js
db.accounts.aggregate([
  { $sort: { limit: -1 } },     // Sort by limit descending
  { $limit: 5 }                 // Take top 5 results
])
```

---

### ✅ Example: Using `$cursor` Options (MongoDB 4.4+)

```js
db.accounts.aggregate([], {
  cursor: {
    sort: { limit: -1 },
    limit: 5
  }
})
```

### 🧠 Notes

* `$cursor.sort` and `$cursor.limit` are **aggregation options**, not stages.
* They control how the **cursor** itself returns results (useful for driver-level control).
* Prefer `$sort` and `$limit` stages for clarity and portability.

---

## 📘 6. Real Example — Top 3 High-Limit Accounts

```js
db.accounts.aggregate([
  { $sort: { limit: -1 } },
  { $limit: 3 },
  { $project: { _id: 0, account_id: 1, limit: 1 } }
])
```

🧠 **Output (example):**

```json
[
  { "account_id": 470651, "limit": 25000 },
  { "account_id": 470656, "limit": 22000 },
  { "account_id": 470655, "limit": 18000 }
]
```

---

## ✅ Summary Table

| Operation                | Description                       | Example                           |
| ------------------------ | --------------------------------- | --------------------------------- |
| `.sort({ field: 1/-1 })` | Sort ascending or descending      | `.sort({ limit: -1 })`            |
| `.limit(n)`              | Limit number of results           | `.limit(5)`                       |
| `.skip(n)`               | Skip documents                    | `.skip(5)`                        |
| `$sort`                  | Aggregation sort stage            | `{ $sort: { limit: -1 } }`        |
| `$limit`                 | Aggregation limit stage           | `{ $limit: 5 }`                   |
| `$cursor.sort`           | Cursor-level sort in aggregation  | `cursor: { sort: { limit: -1 } }` |
| `$cursor.limit`          | Cursor-level limit in aggregation | `cursor: { limit: 5 }`            |