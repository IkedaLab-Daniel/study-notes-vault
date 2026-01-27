# MongoDB CRUD Operations: Insert and Find

## Insert Operations

### insertOne()
Inserts a single document into a collection.

**Syntax:**
```javascript
db.collection.insertOne(
   <document>,
   {
      writeConcern: <document>
   }
)
```

**Example:**
```javascript
db.users.insertOne({
   name: "Alice Johnson",
   email: "alice@example.com",
   age: 28,
   city: "Boston",
   hobbies: ["reading", "hiking"],
   createdAt: new Date()
})
```

**Return Value:**
```javascript
{
   "acknowledged": true,
   "insertedId": ObjectId("507f1f77bcf86cd799439011")
}
```

**Key Points:**
- Returns the `_id` of the inserted document
- If `_id` is not provided, MongoDB generates one automatically
- Fails if document with same `_id` already exists
- Single atomic operation

---

### insertMany()
Inserts multiple documents into a collection in a single operation.

**Syntax:**
```javascript
db.collection.insertMany(
   [ <document1>, <document2>, ... ],
   {
      writeConcern: <document>,
      ordered: <boolean>
   }
)
```

**Example:**
```javascript
db.products.insertMany([
   {
      name: "Laptop",
      price: 999.99,
      category: "electronics",
      inStock: true
   },
   {
      name: "Mouse",
      price: 19.99,
      category: "electronics",
      inStock: true
   },
   {
      name: "Desk Chair",
      price: 149.99,
      category: "furniture",
      inStock: false
   }
])
```

**Return Value:**
```javascript
{
   "acknowledged": true,
   "insertedIds": [
      ObjectId("507f191e810c19729de860ea"),
      ObjectId("507f191e810c19729de860eb"),
      ObjectId("507f191e810c19729de860ec")
   ]
}
```

**Ordered vs Unordered Inserts:**
```javascript
// Ordered (default) - stops on first error
db.collection.insertMany([doc1, doc2, doc3], { ordered: true })

// Unordered - continues inserting even if some fail
db.collection.insertMany([doc1, doc2, doc3], { ordered: false })
```

**Key Points:**
- More efficient than multiple `insertOne()` calls
- Default is ordered insertion (stops on first error)
- Set `ordered: false` to continue on errors
- Returns array of inserted `_id` values
- Maximum 100,000 documents per operation

---

## Find Operations

### findOne()
Returns a single document that matches the query criteria.

**Syntax:**
```javascript
db.collection.findOne(
   <query>,
   <projection>
)
```

**Basic Example:**
```javascript
db.users.findOne({ name: "Alice Johnson" })
```

**With Projection:**
```javascript
// Include only specific fields
db.users.findOne(
   { email: "alice@example.com" },
   { name: 1, email: 1, age: 1 }
)

// Exclude specific fields
db.users.findOne(
   { email: "alice@example.com" },
   { password: 0, ssn: 0 }
)
```

**Key Points:**
- Returns first matching document (or null if no match)
- Uses natural order unless index is used
- Projection controls which fields are returned
- `_id` is always returned unless explicitly excluded: `{ _id: 0 }`

---

### find()
Returns a cursor to all documents that match the query criteria.

**Syntax:**
```javascript
db.collection.find(
   <query>,
   <projection>
)
```

**Basic Examples:**
```javascript
// Find all documents
db.products.find()

// Find with filter
db.products.find({ category: "electronics" })

// Find with projection
db.products.find(
   { category: "electronics" },
   { name: 1, price: 1 }
)
```

**Cursor Methods:**
```javascript
// Limit results
db.products.find().limit(10)

// Skip documents
db.products.find().skip(20)

// Sort results
db.products.find().sort({ price: -1 })  // -1 descending, 1 ascending

// Count documents
db.products.find({ category: "electronics" }).count()

// Chain methods
db.products.find({ inStock: true })
   .sort({ price: 1 })
   .limit(5)
   .skip(10)
```

**Convert Cursor to Array:**
```javascript
db.products.find({ category: "electronics" }).toArray()
```

**Iterate Through Cursor:**
```javascript
var cursor = db.products.find();
while (cursor.hasNext()) {
   printjson(cursor.next());
}

// Or using forEach
db.products.find().forEach(function(doc) {
   print(doc.name);
});
```

**Key Points:**
- Returns a cursor, not the actual documents
- Cursor is iterable and has various methods
- Use `.toArray()` to get all results at once
- Cursors timeout after 10 minutes of inactivity
- First batch of results is returned immediately

---

## Comparison Operators

### $eq (Equal)
Matches values that are equal to a specified value.

```javascript
db.products.find({ price: { $eq: 99.99 } })
// Same as: db.products.find({ price: 99.99 })
```

---

### $gt (Greater Than)
Matches values that are greater than a specified value.

```javascript
db.products.find({ price: { $gt: 50 } })
// Finds products with price > 50
```

---

### $gte (Greater Than or Equal)
Matches values that are greater than or equal to a specified value.

```javascript
db.students.find({ score: { $gte: 90 } })
// Finds students with score >= 90
```

---

### $lt (Less Than)
Matches values that are less than a specified value.

```javascript
db.products.find({ quantity: { $lt: 10 } })
// Finds products with quantity < 10
```

---

### $lte (Less Than or Equal)
Matches values that are less than or equal to a specified value.

```javascript
db.products.find({ price: { $lte: 100 } })
// Finds products with price <= 100
```

---

### $ne (Not Equal)
Matches all values that are not equal to a specified value.

```javascript
db.products.find({ status: { $ne: "discontinued" } })
// Finds products where status is not "discontinued"
```

---

### $in
Matches any of the values specified in an array.

```javascript
db.products.find({ 
   category: { $in: ["electronics", "computers", "phones"] } 
})
// Finds products in any of these categories
```

---

### $nin (Not In)
Matches none of the values specified in an array.

```javascript
db.products.find({ 
   status: { $nin: ["discontinued", "out of stock"] } 
})
// Finds products not in these statuses
```

---

### Range Queries
Combine comparison operators for range queries.

```javascript
// Price between 10 and 100
db.products.find({ 
   price: { $gte: 10, $lte: 100 } 
})

// Age between 18 and 65
db.users.find({ 
   age: { $gt: 18, $lt: 65 } 
})
```

---

## Logical Operators

### $and
Joins query clauses with logical AND. All conditions must be true.

**Implicit AND:**
```javascript
// These are combined with AND automatically
db.products.find({ 
   category: "electronics",
   price: { $lt: 500 }
})
```

**Explicit $and:**
```javascript
db.products.find({
   $and: [
      { price: { $gte: 100 } },
      { price: { $lte: 500 } },
      { category: "electronics" }
   ]
})
```

**When to use explicit $and:**
- When using same field with different operators
```javascript
db.inventory.find({
   $and: [
      { price: { $ne: 1.99 } },
      { price: { $exists: true } }
   ]
})
```

---

### $or
Joins query clauses with logical OR. At least one condition must be true.

```javascript
db.products.find({
   $or: [
      { category: "electronics" },
      { category: "computers" }
   ]
})
```

**Complex OR queries:**
```javascript
db.products.find({
   $or: [
      { price: { $lt: 20 } },
      { sale: true }
   ]
})
```

**Combining AND and OR:**
```javascript
db.products.find({
   category: "electronics",
   $or: [
      { price: { $lt: 100 } },
      { onSale: true }
   ]
})
// Find electronics that are either cheap OR on sale
```

---

### $nor
Joins query clauses with logical NOR. All conditions must be false.

```javascript
db.products.find({
   $nor: [
      { price: { $lt: 10 } },
      { sale: true }
   ]
})
// Finds products where price is NOT less than 10 AND NOT on sale
```

---

### $not
Inverts the effect of a query expression.

```javascript
db.products.find({ 
   price: { $not: { $gt: 100 } } 
})
// Finds products where price is NOT greater than 100
// (includes documents without price field)
```

---

## Element Operators

### $exists
Matches documents that have the specified field.

```javascript
// Find documents with email field
db.users.find({ email: { $exists: true } })

// Find documents without email field
db.users.find({ email: { $exists: false } })
```

---

### $type
Selects documents where the field is of the specified BSON type.

```javascript
// Find where age is a number
db.users.find({ age: { $type: "number" } })

// Find where age is a string
db.users.find({ age: { $type: "string" } })

// Common types: "string", "number", "object", "array", "bool", "date", "null"
```

---

## Array Operators

### $all
Matches arrays that contain all specified elements.

```javascript
db.products.find({ 
   tags: { $all: ["electronics", "sale"] } 
})
// Array must contain both "electronics" AND "sale"
```

---

### $elemMatch
Matches documents that contain an array field with at least one element matching all criteria.

```javascript
db.students.find({
   scores: { 
      $elemMatch: { 
         type: "exam",
         score: { $gte: 90 }
      }
   }
})
```

---

### $size
Matches arrays with the specified number of elements.

```javascript
db.products.find({ 
   tags: { $size: 3 } 
})
// Finds products with exactly 3 tags
```

---

## String Operators

### $regex
Provides regular expression capabilities for pattern matching.

```javascript
// Case-insensitive search
db.products.find({ 
   name: { $regex: /laptop/i } 
})

// Starts with
db.users.find({ 
   name: { $regex: /^A/ } 
})

// Contains
db.products.find({ 
   description: { $regex: /wireless/ } 
})

// With options
db.products.find({ 
   name: { $regex: "laptop", $options: "i" } 
})
```

---

## Projection Examples

### Include Fields
```javascript
// Only return name and price (and _id by default)
db.products.find({}, { name: 1, price: 1 })
```

---

### Exclude Fields
```javascript
// Return everything except password
db.users.find({}, { password: 0 })
```

---

### Exclude _id
```javascript
// Return name and email, but not _id
db.users.find({}, { name: 1, email: 1, _id: 0 })
```

---

### Array Slice
```javascript
// Get only first 3 comments
db.posts.find({}, { comments: { $slice: 3 } })

// Get last 3 comments
db.posts.find({}, { comments: { $slice: -3 } })

// Skip 2, return 5
db.posts.find({}, { comments: { $slice: [2, 5] } })
```

---

## Query Examples

### Find All Documents
```javascript
db.collection.find()
db.collection.find({})
```

---

### Find with Multiple Conditions
```javascript
db.products.find({
   category: "electronics",
   price: { $lt: 500 },
   inStock: true
})
```

---

### Complex Query Example
```javascript
db.orders.find({
   $and: [
      { 
         $or: [
            { status: "pending" },
            { status: "processing" }
         ]
      },
      { total: { $gte: 100 } },
      { 
         customer: { 
            $exists: true,
            $ne: null 
         } 
      }
   ]
}).sort({ createdAt: -1 }).limit(10)
```

---

### Nested Document Queries
```javascript
// Exact match of embedded document
db.users.find({ 
   address: { street: "123 Main St", city: "Boston" } 
})

// Query nested field (dot notation)
db.users.find({ "address.city": "Boston" })

// Query nested array element
db.users.find({ "hobbies.0": "reading" })  // First hobby is reading
```

---

## Best Practices

1. **Use Indexes** - Create indexes on frequently queried fields
   ```javascript
   db.products.createIndex({ category: 1, price: 1 })
   ```

2. **Use Projection** - Only retrieve fields you need
   ```javascript
   db.users.find({}, { name: 1, email: 1 })
   ```

3. **Limit Results** - Use `.limit()` when you don't need all matches
   ```javascript
   db.products.find({ category: "electronics" }).limit(20)
   ```

4. **Use $exists for Optional Fields**
   ```javascript
   db.users.find({ phone: { $exists: true } })
   ```

5. **Test Queries** - Use `.explain()` to analyze query performance
   ```javascript
   db.products.find({ category: "electronics" }).explain("executionStats")
   ```

6. **Specific Filters** - Make queries as specific as possible to use indexes

7. **Batch Inserts** - Use `insertMany()` instead of multiple `insertOne()` calls

8. **Validate Data** - Use schema validation for data integrity

---

## Common Query Patterns

### Pagination
```javascript
const pageSize = 20;
const pageNumber = 3;

db.products.find()
   .skip(pageSize * (pageNumber - 1))
   .limit(pageSize)
   .sort({ createdAt: -1 })
```

---

### Search by Multiple Fields
```javascript
db.users.find({
   $or: [
      { name: { $regex: searchTerm, $options: "i" } },
      { email: { $regex: searchTerm, $options: "i" } }
   ]
})
```

---

### Find Documents Created Today
```javascript
const today = new Date();
today.setHours(0, 0, 0, 0);

db.orders.find({
   createdAt: { $gte: today }
})
```

---

### Find Documents by Date Range
```javascript
db.orders.find({
   createdAt: {
      $gte: new Date("2026-01-01"),
      $lt: new Date("2026-02-01")
   }
})
```

---

## Performance Tips

1. **Create appropriate indexes** for your most common queries
2. **Use covered queries** where possible (all fields in index)
3. **Avoid regex without anchors** on large collections
4. **Use $in instead of multiple $or** conditions when possible
5. **Limit the number of documents scanned** with specific filters
6. **Monitor with .explain()** to understand query execution
7. **Use projection** to reduce data transfer
8. **Consider aggregation pipeline** for complex data transformations
