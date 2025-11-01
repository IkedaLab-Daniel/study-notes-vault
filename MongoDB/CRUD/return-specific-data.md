# 🎯 RETURNING SPECIFIC DATA FROM A QUERY (PROJECTION)

By default, MongoDB returns **all fields** in a document when you run a query.
To **control which fields are returned**, you can add a **projection document** as the **second argument** in the `.find()` method.

---

## 📘 1. Basic Syntax

```js
db.collection.find(<query>, <projection>)
```

* `<query>` → specifies which documents to match
* `<projection>` → specifies which fields to include (`1`) or exclude (`0`) in the result set

---

## 📘 2. Including Fields

### 👉 Syntax

```js
db.collection.find(<query>, { <field>: 1 })
```

### 🧩 Example

```js
// Return business_name, result, and _id fields for all restaurant inspections
db.inspections.find(
  { sector: "Restaurant - 818" },
  { business_name: 1, result: 1 }
)
```

### 🧠 Notes

* A field set to `1` means **include** this field.
* The `_id` field is **included by default**, even if not listed.
* You can mix inclusion for multiple fields in the same projection.

---

## 📘 3. Excluding Fields

### 👉 Syntax

```js
db.collection.find(<query>, { <field>: 0 })
```

### 🧩 Example

```js
// Return all inspections with result of "Pass" or "Warning", excluding date and zip code
db.inspections.find(
  { result: { $in: ["Pass", "Warning"] } },
  { date: 0, "address.zip": 0 }
)
```

### 🧠 Notes

* A field set to `0` means **exclude** this field.
* Cannot mix inclusion (`1`) and exclusion (`0`) in the same projection
  — except when excluding `_id`.

---

## 📘 4. Excluding the `_id` Field

By default, `_id` is always included in the query result.
You can remove it explicitly by setting `_id: 0`.

### 👉 Example

```js
// Return business_name and result fields only, exclude _id
db.inspections.find(
  { sector: "Restaurant - 818" },
  { business_name: 1, result: 1, _id: 0 }
)
```

---

## 📘 5. Projecting Embedded Fields

You can project **specific subfields** of embedded documents using **dot notation**.

### 👉 Example

```js
// Return only the street and city from the address subdocument
db.inspections.find(
  {},
  { "address.street": 1, "address.city": 1, _id: 0 }
)
```

### 🧠 Notes

* Dot notation works for **nested objects**.
* You can include only certain subfields while excluding others.

---

## 📘 6. Projection with Query Filters

Combine projections with query filters to get clean, filtered results.

### 👉 Example

```js
// Return account_id and limit for accounts with 'InvestmentStock' in products
db.accounts.find(
  { products: "InvestmentStock" },
  { account_id: 1, limit: 1, _id: 0 }
)
```

---

## 📘 7. Projection in Aggregation (`$project`)

In aggregation pipelines, use `$project` to shape the returned documents.

### 👉 Example

```js
db.accounts.aggregate([
  { $match: { products: "InvestmentStock" } },
  { $project: { _id: 0, account_id: 1, limit: 1 } }
])
```

### 🧠 Notes

* `$project` serves the same role as projection in `.find()`.
* You can also create **computed fields** (e.g., `$add`, `$concat`, etc.) inside `$project`.

---

## ✅ Summary Table

| Projection Type        | Syntax Example               | Description                         |
| ---------------------- | ---------------------------- | ----------------------------------- |
| Include fields         | `{ field: 1 }`               | Show only specified fields          |
| Exclude fields         | `{ field: 0 }`               | Hide specified fields               |
| Exclude `_id`          | `{ _id: 0 }`                 | Hide MongoDB’s default `_id` field  |
| Subfields              | `{ "nested.field": 1 }`      | Include only specific subfields     |
| Aggregation projection | `{ $project: { field: 1 } }` | Equivalent in aggregation pipelines |