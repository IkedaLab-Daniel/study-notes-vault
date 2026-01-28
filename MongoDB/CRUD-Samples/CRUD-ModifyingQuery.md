# MongoDB CRUD Operations: Modifying Query Results - Cheatsheet

## Overview
This cheatsheet covers methods to modify and control query results in MongoDB:
- **Sorting** - Order results
- **Limiting** - Control number of results
- **Projection** - Select specific fields
- **Counting** - Count matching documents

---

## 1. Sorting Results - `cursor.sort()`

### Syntax
```javascript
db.collection.find(<query>).sort(<sort document>)
```

### Sort Order
- `1` - Ascending order
- `-1` - Descending order

### Examples

#### Sort by single field (ascending)
```javascript
db.movies.find().sort({ title: 1 })
```

#### Sort by single field (descending)
```javascript
db.movies.find().sort({ year: -1 })
```

#### Sort by multiple fields
```javascript
// Sort by year (descending), then by title (ascending)
db.movies.find().sort({ year: -1, title: 1 })
```

#### Sort with query filter
```javascript
db.sales.find({ status: "completed" }).sort({ amount: -1 })
```

### Common Use Cases
- Get latest items: `sort({ createdAt: -1 })`
- Alphabetical ordering: `sort({ name: 1 })`
- Price ordering: `sort({ price: 1 })` or `sort({ price: -1 })`

---

## 2. Limiting Results - `cursor.limit()`

### Syntax
```javascript
db.collection.find(<query>).limit(<number>)
```

### Examples

#### Limit to first 10 documents
```javascript
db.products.find().limit(10)
```

#### Top 5 highest prices
```javascript
db.products.find().sort({ price: -1 }).limit(5)
```

#### Pagination pattern (skip + limit)
```javascript
// Page 1: First 20 items
db.articles.find().limit(20)

// Page 2: Next 20 items
db.articles.find().skip(20).limit(20)

// Page 3: Next 20 items
db.articles.find().skip(40).limit(20)
```

#### Limit with query filter
```javascript
db.users.find({ active: true }).sort({ lastLogin: -1 }).limit(100)
```

### Common Use Cases
- Top N results: `sort().limit(N)`
- Pagination: `skip(offset).limit(pageSize)`
- Sample data: `limit(1)` or `limit(5)`

---

## 3. Projection - Selecting Fields

### Syntax
```javascript
db.collection.find(<query>, <projection>)
```

### Projection Values
- `1` or `true` - Include field
- `0` or `false` - Exclude field
- Cannot mix inclusion and exclusion (except for `_id`)

### Examples

#### Include specific fields
```javascript
// Only return title and year fields (plus _id by default)
db.movies.find({}, { title: 1, year: 1 })
```

#### Exclude _id field
```javascript
// Return title and year, but exclude _id
db.movies.find({}, { title: 1, year: 1, _id: 0 })
```

#### Exclude specific fields
```javascript
// Return all fields except password and email
db.users.find({}, { password: 0, email: 0 })
```

#### Projection with query filter
```javascript
db.products.find(
  { category: "electronics" },
  { name: 1, price: 1, brand: 1, _id: 0 }
)
```

#### Nested field projection
```javascript
db.users.find(
  {},
  { "name": 1, "address.city": 1, "address.country": 1 }
)
```

#### Array element projection with $slice
```javascript
// Get only first 3 comments
db.posts.find({}, { title: 1, comments: { $slice: 3 } })

// Get last 5 comments
db.posts.find({}, { title: 1, comments: { $slice: -5 } })

// Skip 2, return next 3
db.posts.find({}, { title: 1, comments: { $slice: [2, 3] } })
```

### Common Use Cases
- API responses: Select only needed fields
- Performance: Reduce network transfer
- Security: Exclude sensitive fields like passwords
- Lists: `{ name: 1, _id: 0 }` for simple name lists

---

## 4. Counting Documents - `countDocuments()`

### Syntax
```javascript
db.collection.countDocuments(<query>, <options>)
```

### Examples

#### Count all documents
```javascript
db.products.countDocuments()
// or
db.products.countDocuments({})
```

#### Count with filter
```javascript
db.orders.countDocuments({ status: "pending" })
```

#### Count with multiple conditions
```javascript
db.users.countDocuments({
  active: true,
  role: "admin"
})
```

#### Count with comparison operators
```javascript
db.products.countDocuments({ price: { $gte: 100 } })
```

#### Count with limit option
```javascript
db.logs.countDocuments({}, { limit: 1000 })
```

### Alternative: `estimatedDocumentCount()`
For total count without filters (faster but approximate):
```javascript
db.products.estimatedDocumentCount()
```

### Common Use Cases
- Total records: `countDocuments({})`
- Filter counts: `countDocuments({ status: "active" })`
- Pagination metadata: Get total before applying skip/limit
- Validation: Check if documents exist

---

## 5. Combining Methods (Method Chaining)

### Order of Operations
MongoDB optimizes the order internally, but recommended pattern:
1. `find()` - Query filter
2. `sort()` - Sort results
3. `skip()` - Skip documents
4. `limit()` - Limit results
5. `project()` or projection in find()

### Examples

#### Pagination with sorting
```javascript
db.articles.find()
  .sort({ publishedDate: -1 })
  .skip(20)
  .limit(10)
```

#### Complete query with all modifiers
```javascript
db.products.find(
  { category: "electronics", price: { $lt: 1000 } },
  { name: 1, price: 1, brand: 1, _id: 0 }
)
  .sort({ price: -1 })
  .limit(50)
```

#### Top performers with projection
```javascript
db.employees.find(
  { department: "Sales" },
  { name: 1, salesTotal: 1, _id: 0 }
)
  .sort({ salesTotal: -1 })
  .limit(10)
```

---

## 6. Practical Examples

### Example 1: Blog Posts - Latest 10
```javascript
db.posts.find(
  { published: true },
  { title: 1, excerpt: 1, author: 1, publishedDate: 1 }
)
  .sort({ publishedDate: -1 })
  .limit(10)
```

### Example 2: Product Catalog - Price Range
```javascript
db.products.find(
  { 
    category: "laptops",
    price: { $gte: 500, $lte: 1500 }
  },
  { name: 1, price: 1, specs: 1, _id: 0 }
)
  .sort({ price: 1 })
```

### Example 3: User Dashboard - Active Users
```javascript
db.users.find(
  { lastLogin: { $gte: new Date("2026-01-01") } },
  { username: 1, email: 1, lastLogin: 1 }
)
  .sort({ lastLogin: -1 })
  .limit(100)
```

### Example 4: Analytics - Count by Status
```javascript
const pending = db.orders.countDocuments({ status: "pending" })
const completed = db.orders.countDocuments({ status: "completed" })
const cancelled = db.orders.countDocuments({ status: "cancelled" })
```

---

## Quick Reference Table

| Method | Purpose | Syntax Example |
|--------|---------|----------------|
| `sort()` | Order results | `.sort({ field: 1 })` |
| `limit()` | Limit number of results | `.limit(10)` |
| `skip()` | Skip documents | `.skip(20)` |
| `projection` | Select fields | `find({}, { field: 1 })` |
| `countDocuments()` | Count matches | `countDocuments({ query })` |
| `estimatedDocumentCount()` | Fast total count | `estimatedDocumentCount()` |

---

## Best Practices

1. **Always use indexes** for sorted fields to improve performance
2. **Limit results** to avoid large data transfers
3. **Project only needed fields** to reduce bandwidth
4. **Use estimatedDocumentCount()** for total counts (no filter)
5. **Use countDocuments()** for filtered counts
6. **Combine skip/limit** for pagination
7. **Sort before limit** for top-N queries
8. **Create compound indexes** for multi-field sorts

---

## Performance Tips

- Index fields used in `sort()` to avoid in-memory sorting
- Use `limit()` with `sort()` to reduce processing
- Project fields early to reduce document size
- For large skip values, consider cursor-based pagination
- Use covered queries (index contains all projected fields)