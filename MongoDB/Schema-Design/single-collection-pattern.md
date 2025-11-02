# 🧱 SCHEMA DESIGN PATTERN: SINGLE COLLECTION PATTERN

The **Single Collection Pattern** is a schema design strategy where **multiple types of related data** are stored within **one MongoDB collection**, instead of using separate collections for each entity type.

It’s commonly used when documents share similar structure, are queried together, or belong to the same logical context (e.g., an app event log or e-commerce transactions).

---

## 📘 1. Concept Overview

Instead of this (SQL-style normalization):

```js
// Separate collections
db.customers.find()
db.orders.find()
db.payments.find()
```

You might use **one unified collection**:

```js
db.events.find()
```

Where each document represents an **event type**, like:

```js
{
  type: "customer",
  name: "Alice",
  email: "alice@email.com"
}

{
  type: "order",
  customer_id: "C123",
  items: ["Dog Food", "Leash"],
  total: 550
}

{
  type: "payment",
  customer_id: "C123",
  method: "GCash",
  amount: 550
}
```

---

## 📘 2. Why Use the Single Collection Pattern?

### ✅ Advantages

* **Simplifies querying** when data is frequently accessed together
  → e.g., all user-related activities (signup, order, payment)
* **Easier indexing** when documents share common fields
* **Better performance** for analytics and event sourcing
* **Schema flexibility** — allows different document shapes

### ⚠️ Disadvantages

* Schema validation is more complex (must handle multiple shapes)
* Index size may grow quickly if many field types are mixed
* Harder to enforce strict structure for each entity type

---

## 📘 3. Common Use Cases

| Use Case              | Description                                                       |
| --------------------- | ----------------------------------------------------------------- |
| 🧾 **Event Logging**  | Store various log types (login, update, delete) in one collection |
| 🛒 **E-Commerce**     | Store order, shipment, and payment events together                |
| 📱 **Activity Feeds** | Store posts, likes, and comments in one “activities” collection   |
| 🧩 **IoT Systems**    | Different sensor readings stored as one “events” stream           |

---

## 📘 4. Querying Example

```js
// Find only customer-related documents
db.events.find({ type: "customer" })

// Find all events related to a specific customer
db.events.find({ customer_id: "C123" })

// Find all orders with total over 500
db.events.find({ type: "order", total: { $gt: 500 } })
```

---

## 📘 5. Indexing Example

To improve performance:

```js
db.events.createIndex({ type: 1 })
db.events.createIndex({ customer_id: 1 })
```

Indexes make it efficient to query documents of specific types or related to one entity.

---

## 📘 6. Design Tips

* Always include a **type discriminator field** (e.g., `"type": "customer"`)
* Keep **shared fields consistent** (e.g., `timestamp`, `customer_id`)
* Use **validation rules** or **schema mapping in the application layer**
* For analytics-heavy workloads, consider a **time-based partition key** (e.g., month, date)

---

## 📘 7. Example Visualization

| `_id` | `type`     | `customer_id` | `details` / `data`                        |
| ----- | ---------- | ------------- | ----------------------------------------- |
| 1     | "customer" | C123          | `{ name: "Alice", email: "a@email.com" }` |
| 2     | "order"    | C123          | `{ total: 550, items: [...] }`            |
| 3     | "payment"  | C123          | `{ method: "GCash", amount: 550 }`        |

---

## ✅ Summary

| Concept            | Description                                           |
| ------------------ | ----------------------------------------------------- |
| 📦 **What it is**  | A single collection storing multiple entity types     |
| 🧭 **When to use** | When entities share context and are queried together  |
| ⚙️ **Key field**   | `type` field to differentiate document kinds          |
| ⚡ **Goal**         | Reduce joins and simplify event-style data management |