# Creating a Multikey Index in MongoDB

## Overview
A multikey index is an index on an array field. When you index a field that contains an array, MongoDB creates separate index entries for every element in the array. This allows efficient queries on array elements.

## Why Use Multikey Indexes?
- **Query Array Elements**: Efficiently search for documents containing specific array values
- **Match Any Element**: Find documents where any array element matches a condition
- **Array Operations**: Support queries with `$in`, `$all`, `$elemMatch`, etc.
- **Automatic Creation**: MongoDB automatically creates multikey indexes when you index array fields

## Basic Syntax

### Creating a Multikey Index
```javascript
// MongoDB automatically creates a multikey index if the field contains arrays
db.collection.createIndex({ arrayField: 1 })
```

### Examples

#### 1. Simple Array Index
```javascript
// Sample documents
db.products.insertMany([
  { name: "Laptop", tags: ["electronics", "computers", "portable"] },
  { name: "Desk", tags: ["furniture", "office"] },
  { name: "Mouse", tags: ["electronics", "accessories"] }
])

// Create multikey index on 'tags' array
db.products.createIndex({ tags: 1 })

// Query using the index
db.products.find({ tags: "electronics" })
// Returns: Laptop and Mouse
```

#### 2. Array of Numbers
```javascript
// Sample documents with numeric arrays
db.scores.insertMany([
  { student: "Alice", grades: [85, 92, 88] },
  { student: "Bob", grades: [78, 85, 90] },
  { student: "Charlie", grades: [95, 98, 100] }
])

// Create index on grades array
db.scores.createIndex({ grades: 1 })

// Find students with a specific grade
db.scores.find({ grades: 90 })
// Returns: Bob and Charlie
```

#### 3. Array of Embedded Documents
```javascript
// Sample documents with array of objects
db.inventory.insertMany([
  {
    item: "Notebook",
    locations: [
      { warehouse: "A", qty: 100 },
      { warehouse: "B", qty: 50 }
    ]
  },
  {
    item: "Pen",
    locations: [
      { warehouse: "B", qty: 200 },
      { warehouse: "C", qty: 75 }
    ]
  }
])

// Create index on embedded field within array
db.inventory.createIndex({ "locations.warehouse": 1 })

// Query using the index
db.inventory.find({ "locations.warehouse": "B" })
// Returns: Both Notebook and Pen
```

## How Multikey Indexes Work

When you create an index on an array field:

```javascript
// Document
{
  _id: 1,
  name: "Product A",
  tags: ["electronics", "sale", "new"]
}

// After creating index on 'tags'
db.products.createIndex({ tags: 1 })

// MongoDB creates index entries:
// "electronics" -> document 1
// "sale" -> document 1
// "new" -> document 1
```

## Multikey Index Limitations

### 1. Cannot Index Multiple Arrays in Compound Index
```javascript
// ❌ INVALID - Cannot have two array fields in compound index
db.collection.createIndex({ arrayField1: 1, arrayField2: 1 })
// Error: cannot index parallel arrays

// ✅ VALID - One array field, one scalar field
db.collection.createIndex({ arrayField: 1, scalarField: 1 })
```

### 2. Example of Parallel Arrays Restriction
```javascript
// These documents would cause an error if indexed
db.invalid.insertOne({
  tags: ["a", "b"],      // array
  categories: ["x", "y"]  // array
})

// This will fail:
db.invalid.createIndex({ tags: 1, categories: 1 })
// Error: cannot index parallel arrays [tags] [categories]

// This is OK:
db.valid.insertOne({
  tags: ["a", "b"],      // array
  name: "Product"         // scalar
})

db.valid.createIndex({ tags: 1, name: 1 }) // ✅ Works fine
```

## Compound Multikey Indexes

You can create compound indexes with one array field and one or more scalar fields:

```javascript
// Sample data
db.blog.insertMany([
  {
    title: "MongoDB Guide",
    tags: ["database", "nosql", "tutorial"],
    author: "Alice",
    published: true
  },
  {
    title: "Node.js Basics",
    tags: ["javascript", "backend", "tutorial"],
    author: "Bob",
    published: true
  }
])

// Create compound index: array field + scalar field
db.blog.createIndex({ tags: 1, published: 1 })

// Efficient query using both fields
db.blog.find({ tags: "tutorial", published: true })
```

## Query Patterns with Multikey Indexes

### 1. Exact Match on Array Element
```javascript
db.products.find({ tags: "electronics" })
```

### 2. Using $in Operator
```javascript
db.products.find({ tags: { $in: ["electronics", "furniture"] } })
```

### 3. Using $all Operator
```javascript
// Find documents containing ALL specified values
db.products.find({ tags: { $all: ["electronics", "portable"] } })
```

### 4. Using $elemMatch
```javascript
// For arrays of embedded documents
db.inventory.find({
  locations: {
    $elemMatch: { warehouse: "B", qty: { $gt: 100 } }
  }
})
```

### 5. Range Queries on Array Elements
```javascript
db.scores.find({ grades: { $gte: 90 } })
// Returns documents where ANY grade is >= 90
```

## Practical Example: E-commerce System

```javascript
// Product catalog with tags
db.products.insertMany([
  {
    _id: 1,
    name: "Gaming Laptop",
    price: 1299,
    tags: ["electronics", "computers", "gaming", "high-performance"],
    categories: ["Electronics", "Computers"],
    inStock: true
  },
  {
    _id: 2,
    name: "Wireless Mouse",
    price: 29,
    tags: ["electronics", "accessories", "wireless"],
    categories: ["Electronics", "Accessories"],
    inStock: true
  },
  {
    _id: 3,
    name: "Office Desk",
    price: 299,
    tags: ["furniture", "office", "workspace"],
    categories: ["Furniture", "Office"],
    inStock: false
  }
])

// Create multikey index on tags
db.products.createIndex({ tags: 1 })

// Create compound multikey index
db.products.createIndex({ tags: 1, inStock: 1 })

// Query 1: Find all electronics in stock
db.products.find({ tags: "electronics", inStock: true })
// Returns: Gaming Laptop, Wireless Mouse

// Query 2: Find products with multiple tags
db.products.find({ tags: { $all: ["electronics", "wireless"] } })
// Returns: Wireless Mouse

// Query 3: Count products by tag
db.products.aggregate([
  { $unwind: "$tags" },
  { $group: { _id: "$tags", count: { $sum: 1 } } },
  { $sort: { count: -1 } }
])
```

## Index Bounds with Multikey Indexes

```javascript
// Check how MongoDB uses the index
db.products.find({ tags: "electronics" }).explain("executionStats")

// Output shows:
// - stage: "IXSCAN" (index scan)
// - indexName: "tags_1"
// - indexBounds: { tags: [["electronics", "electronics"]] }
```

## Multikey Index with Nested Arrays

```javascript
// Document with nested arrays
db.survey.insertOne({
  question: "Favorite colors?",
  responses: [
    { user: "Alice", answers: ["blue", "green"] },
    { user: "Bob", answers: ["red", "yellow"] }
  ]
})

// Create index on nested array field
db.survey.createIndex({ "responses.answers": 1 })

// Query
db.survey.find({ "responses.answers": "blue" })
```

## Performance Considerations

### Benefits:
- ✅ Efficient queries on array elements
- ✅ No need to query each element separately
- ✅ Supports complex array operations
- ✅ Automatic optimization for array queries

### Drawbacks:
- ❌ Larger index size (one entry per array element)
- ❌ Slower writes when arrays are large
- ❌ Cannot create compound indexes with multiple arrays
- ❌ Memory overhead for large arrays

### Size Impact Example:
```javascript
// Document with 3 tags
{ tags: ["a", "b", "c"] }
// Creates 3 index entries

// Document with 100 tags
{ tags: ["tag1", "tag2", ..., "tag100"] }
// Creates 100 index entries
```

## Best Practices

### 1. Limit Array Sizes
```javascript
// ❌ BAD: Very large arrays
{ tags: [...1000 tags...] }  // Creates 1000 index entries per document

// ✅ GOOD: Reasonable array sizes
{ tags: ["tag1", "tag2", "tag3"] }  // Creates 3 index entries per document
```

### 2. Use Compound Indexes Wisely
```javascript
// ✅ GOOD: Multikey + scalar fields
db.collection.createIndex({ arrayField: 1, scalarField1: 1, scalarField2: 1 })

// ❌ BAD: Multiple array fields
db.collection.createIndex({ arrayField1: 1, arrayField2: 1 })  // Error!
```

### 3. Consider Query Selectivity
```javascript
// High selectivity (good for indexing)
db.products.find({ tags: "rare-specific-tag" })  // Returns few documents

// Low selectivity (index less useful)
db.products.find({ tags: "common-tag" })  // Returns many documents
```

### 4. Monitor Index Size
```javascript
// Check index size
db.products.stats()

// Output includes:
// - totalIndexSize: Total size of all indexes
// - indexSizes: Size of each individual index
```

## Common Use Cases

### 1. Tagging Systems
```javascript
// Blog posts, products, articles
db.articles.createIndex({ tags: 1 })
db.articles.find({ tags: "mongodb" })
```

### 2. Categories/Classifications
```javascript
// Multiple categories per item
db.items.createIndex({ categories: 1 })
db.items.find({ categories: "Electronics" })
```

### 3. User Permissions/Roles
```javascript
// Users with multiple roles
db.users.createIndex({ roles: 1 })
db.users.find({ roles: "admin" })
```

### 4. Location-Based Data
```javascript
// Stores in multiple cities
db.stores.createIndex({ cities: 1 })
db.stores.find({ cities: "New York" })
```

### 5. Skills/Attributes
```javascript
// Job candidates with multiple skills
db.candidates.createIndex({ skills: 1 })
db.candidates.find({ skills: { $all: ["JavaScript", "MongoDB"] } })
```

## Checking if Index is Multikey

```javascript
// Get index information
db.collection.getIndexes()

// Look for "multikey: true" in the output
// Or check after inserting array data
db.collection.stats().indexDetails
```

## Dropping Multikey Indexes

```javascript
// Drop by name
db.collection.dropIndex("tags_1")

// Drop by specification
db.collection.dropIndex({ tags: 1 })

// Drop all indexes except _id
db.collection.dropIndexes()
```

## Advanced Example: Social Media Posts

```javascript
// Social media posts with hashtags
db.posts.insertMany([
  {
    author: "Alice",
    content: "Learning MongoDB!",
    hashtags: ["mongodb", "database", "learning"],
    mentions: ["@bob", "@charlie"],
    likes: 150,
    createdAt: new Date("2026-01-15")
  },
  {
    author: "Bob",
    content: "Great tutorial on indexes",
    hashtags: ["mongodb", "tutorial", "performance"],
    mentions: ["@alice"],
    likes: 200,
    createdAt: new Date("2026-01-20")
  }
])

// Create multikey indexes
db.posts.createIndex({ hashtags: 1 })
db.posts.createIndex({ mentions: 1 })

// Create compound multikey index
db.posts.createIndex({ hashtags: 1, createdAt: -1 })

// Query 1: Find posts with specific hashtag
db.posts.find({ hashtags: "mongodb" })

// Query 2: Find recent posts with hashtag
db.posts.find({ hashtags: "mongodb" }).sort({ createdAt: -1 })

// Query 3: Find posts mentioning a user
db.posts.find({ mentions: "@alice" })

// Query 4: Aggregation - Top hashtags
db.posts.aggregate([
  { $unwind: "$hashtags" },
  { $group: { _id: "$hashtags", count: { $sum: 1 } } },
  { $sort: { count: -1 } },
  { $limit: 10 }
])
```

## Troubleshooting

### Error: Cannot Index Parallel Arrays
```javascript
// Problem
db.data.insertOne({
  array1: [1, 2, 3],
  array2: [4, 5, 6]
})

db.data.createIndex({ array1: 1, array2: 1 })
// Error: cannot index parallel arrays

// Solution 1: Index only one array
db.data.createIndex({ array1: 1 })

// Solution 2: Restructure your data
db.data.updateOne(
  { _id: 1 },
  { $set: { 
      array1: [1, 2, 3],
      singleValue: 4  // Convert to scalar if possible
  }}
)
```

### Large Index Size
```javascript
// Problem: Index too large
db.collection.stats().indexSizes
// tags_1: 500MB

// Solutions:
// 1. Limit array sizes in your application
// 2. Consider if all array elements need indexing
// 3. Use sparse indexes if arrays are optional
// 4. Archive old documents with large arrays
```

## Summary

Multikey indexes are essential for efficient array queries in MongoDB:
- Automatically created when indexing array fields
- Create one index entry per array element
- Support complex array operations
- Cannot have multiple array fields in compound indexes
- Monitor array sizes to control index size
- Ideal for tags, categories, permissions, and similar use cases

## Next Steps
- Learn about Compound Indexes
- Explore Text Indexes for full-text search
- Study Index Intersection
- Understand Geospatial Indexes for location data
