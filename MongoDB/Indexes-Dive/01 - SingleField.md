# Creating a Single Field Index in MongoDB

## Overview
A single field index is an index on a single field of a document. MongoDB creates a single field index on the `_id` field by default, but you can create additional indexes to improve query performance.

## Why Use Single Field Indexes?
- **Faster Queries**: Indexes allow MongoDB to quickly locate documents without scanning every document in a collection
- **Efficient Sorting**: Indexes can be used to return sorted results without performing an in-memory sort
- **Improved Performance**: Reduces query execution time significantly for large collections

## Basic Syntax

### Creating an Index
```javascript
db.collection.createIndex({ fieldName: 1 })
```

- `1` indicates ascending order
- `-1` indicates descending order

### Examples

#### 1. Create an Ascending Index
```javascript
// Create an ascending index on the 'email' field
db.users.createIndex({ email: 1 })
```

#### 2. Create a Descending Index
```javascript
// Create a descending index on the 'createdAt' field
db.posts.createIndex({ createdAt: -1 })
```

#### 3. Create a Unique Index
```javascript
// Ensure the 'username' field has unique values
db.users.createIndex({ username: 1 }, { unique: true })
```

#### 4. Create a Sparse Index
```javascript
// Only index documents that have the specified field
db.users.createIndex({ phoneNumber: 1 }, { sparse: true })
```

## Index Options

### Common Options:
```javascript
db.collection.createIndex(
  { fieldName: 1 },
  {
    unique: false,        // Ensures uniqueness
    sparse: false,        // Only indexes documents with the field
    name: "customName",   // Custom index name
    background: true,     // Build index in background (older versions)
    expireAfterSeconds: 3600  // TTL index (for date fields)
  }
)
```

## Viewing Indexes

### List All Indexes
```javascript
db.collection.getIndexes()
```

### Check Index Usage
```javascript
db.collection.find({ email: "user@example.com" }).explain("executionStats")
```

## Dropping Indexes

### Drop a Specific Index
```javascript
// By index name
db.collection.dropIndex("email_1")

// By index specification
db.collection.dropIndex({ email: 1 })
```

### Drop All Indexes (except _id)
```javascript
db.collection.dropIndexes()
```

## Practical Example

```javascript
// Sample collection
db.products.insertMany([
  { name: "Laptop", category: "Electronics", price: 999, stock: 50 },
  { name: "Mouse", category: "Electronics", price: 25, stock: 200 },
  { name: "Desk", category: "Furniture", price: 299, stock: 30 }
])

// Create index on 'category' field
db.products.createIndex({ category: 1 })

// This query will use the index
db.products.find({ category: "Electronics" })

// Verify index usage
db.products.find({ category: "Electronics" }).explain("executionStats")
```

## Best Practices

1. **Index Selective Fields**: Create indexes on fields frequently used in queries
2. **Consider Query Patterns**: Analyze your most common queries before creating indexes
3. **Monitor Index Size**: Indexes consume disk space and memory
4. **Avoid Over-Indexing**: Too many indexes can slow down write operations
5. **Use Covered Queries**: Design queries that can be satisfied entirely by the index
6. **Index Cardinality**: Fields with high cardinality (many unique values) benefit most from indexes

## Performance Considerations

### When to Use Single Field Indexes:
- ✅ Queries filtering on a single field
- ✅ Sorting on a single field
- ✅ Range queries on numeric or date fields
- ✅ Equality matches on frequently queried fields

### When NOT to Use:
- ❌ Fields with very low cardinality (e.g., boolean fields in large collections)
- ❌ Fields that are rarely queried
- ❌ Small collections (< 1000 documents) where full scans are fast enough

## Index Direction Matters For:
- **Single Field Queries**: Direction doesn't matter for equality matches
- **Sorting**: Use the same direction as your sort order for optimal performance
- **Range Queries**: Direction can affect performance in some cases

## Example: Before and After Indexing

### Before Index
```javascript
db.orders.find({ customerId: "12345" }).explain("executionStats")
// Output shows: "COLLSCAN" (collection scan)
// executionTimeMillis: 250ms (for 1M documents)
```

### After Creating Index
```javascript
db.orders.createIndex({ customerId: 1 })

db.orders.find({ customerId: "12345" }).explain("executionStats")
// Output shows: "IXSCAN" (index scan)
// executionTimeMillis: 2ms
```

## TTL Indexes (Time To Live)

Special type of single field index that automatically removes documents after a certain time:

```javascript
// Create TTL index - documents expire 1 hour after 'createdAt'
db.sessions.createIndex(
  { createdAt: 1 },
  { expireAfterSeconds: 3600 }
)

// Insert a document
db.sessions.insertOne({
  userId: "user123",
  createdAt: new Date()
})
// This document will be automatically deleted after 1 hour
```

## Common Errors

### Error: Index Already Exists
```javascript
// If you try to create the same index twice
db.users.createIndex({ email: 1 })
db.users.createIndex({ email: 1 })
// Error: Index with name 'email_1' already exists
```

### Solution: Drop and Recreate or Use Different Name
```javascript
db.users.dropIndex("email_1")
db.users.createIndex({ email: 1 })
```

## Summary

Single field indexes are the foundation of MongoDB query optimization. They provide:
- Fast lookups for equality queries
- Efficient range scans
- Sorted result sets without in-memory sorting
- Foundation for compound indexes

Remember: Index creation is about balance - too few indexes slow queries, too many slow writes. Profile your application and create indexes based on actual query patterns.

## Next Steps
- Learn about Compound Indexes
- Understand Index Intersection
- Explore Multikey Indexes for Arrays
- Study Index Build Performance
