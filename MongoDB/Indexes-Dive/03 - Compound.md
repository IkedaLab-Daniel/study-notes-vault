# Creating a Compound Index in MongoDB

## Overview
A compound index is an index on multiple fields of a document. MongoDB supports compound indexes where a single index structure references multiple fields. The order of fields in a compound index matters significantly for query performance.

## Why Use Compound Indexes?
- **Multi-Field Queries**: Efficiently query on multiple fields simultaneously
- **Sort Optimization**: Support queries that sort on multiple fields
- **Covered Queries**: Return results entirely from the index without accessing documents
- **Query Flexibility**: Support queries on prefixes of the indexed fields
- **Performance**: Much faster than using multiple single-field indexes

## Basic Syntax

### Creating a Compound Index
```javascript
db.collection.createIndex({ field1: 1, field2: 1, field3: -1 })
```

- First field: Primary sort key
- Subsequent fields: Secondary sort keys
- `1` = ascending, `-1` = descending

## Field Order Matters!

The order of fields in a compound index is crucial:

```javascript
// These are DIFFERENT indexes:
db.users.createIndex({ age: 1, name: 1 })      // Index A
db.users.createIndex({ name: 1, age: 1 })      // Index B

// Index A is efficient for:
// - { age: 25 }
// - { age: 25, name: "Alice" }
// - { age: { $gt: 20 }, name: "Alice" }

// Index B is efficient for:
// - { name: "Alice" }
// - { name: "Alice", age: 25 }
// - { name: "Alice", age: { $gt: 20 } }
```

## ESR Rule (Equality, Sort, Range)

Order your compound index fields following the ESR rule for optimal performance:

1. **E**quality fields first
2. **S**ort fields second
3. **R**ange fields last

```javascript
// Query pattern:
db.orders.find({ 
  status: "pending",        // Equality
  customerId: "12345"       // Equality
}).sort({ 
  createdAt: -1             // Sort
})

// Optimal index following ESR:
db.orders.createIndex({ 
  status: 1,                // Equality
  customerId: 1,            // Equality
  createdAt: -1             // Sort
})
```

## Examples

### 1. Basic Compound Index
```javascript
// Sample data
db.employees.insertMany([
  { name: "Alice", department: "Engineering", salary: 80000 },
  { name: "Bob", department: "Engineering", salary: 75000 },
  { name: "Charlie", department: "Sales", salary: 60000 },
  { name: "Diana", department: "Sales", salary: 65000 }
])

// Create compound index
db.employees.createIndex({ department: 1, salary: -1 })

// Efficient queries:
db.employees.find({ department: "Engineering" })
db.employees.find({ department: "Engineering", salary: { $gt: 70000 } })
db.employees.find({ department: "Sales" }).sort({ salary: -1 })
```

### 2. Three-Field Compound Index
```javascript
// E-commerce orders
db.orders.insertMany([
  { 
    customerId: "c1", 
    status: "shipped", 
    orderDate: new Date("2026-01-15"),
    total: 150 
  },
  { 
    customerId: "c1", 
    status: "pending", 
    orderDate: new Date("2026-01-20"),
    total: 200 
  },
  { 
    customerId: "c2", 
    status: "shipped", 
    orderDate: new Date("2026-01-18"),
    total: 300 
  }
])

// Compound index for common query pattern
db.orders.createIndex({ 
  customerId: 1,      // Equality
  status: 1,          // Equality
  orderDate: -1       // Sort/Range
})

// Highly efficient queries:
db.orders.find({ customerId: "c1", status: "shipped" })
  .sort({ orderDate: -1 })

db.orders.find({ 
  customerId: "c1", 
  status: "pending",
  orderDate: { $gte: new Date("2026-01-01") }
})
```

### 3. Unique Compound Index
```javascript
// Ensure combination of fields is unique
db.users.createIndex(
  { email: 1, tenantId: 1 },
  { unique: true }
)

// Allows same email in different tenants
db.users.insertOne({ email: "user@example.com", tenantId: "tenant1" }) // ✅
db.users.insertOne({ email: "user@example.com", tenantId: "tenant2" }) // ✅
db.users.insertOne({ email: "user@example.com", tenantId: "tenant1" }) // ❌ Error!
```

## Index Prefixes

A compound index can support queries on any prefix of the index:

```javascript
// Compound index
db.collection.createIndex({ a: 1, b: 1, c: 1 })

// This index supports queries on:
// ✅ { a: value }
// ✅ { a: value, b: value }
// ✅ { a: value, b: value, c: value }

// Does NOT efficiently support:
// ❌ { b: value }
// ❌ { c: value }
// ❌ { b: value, c: value }
```

### Practical Example
```javascript
// Index on three fields
db.products.createIndex({ category: 1, brand: 1, price: 1 })

// Efficient queries (using index prefixes):
db.products.find({ category: "Electronics" })
db.products.find({ category: "Electronics", brand: "Samsung" })
db.products.find({ category: "Electronics", brand: "Samsung", price: { $lt: 500 } })

// Inefficient queries (not using prefixes):
db.products.find({ brand: "Samsung" })                    // ❌
db.products.find({ price: { $lt: 500 } })                 // ❌
db.products.find({ brand: "Samsung", price: { $lt: 500 } }) // ❌
```

## Sort Direction Matters

For sorting on multiple fields, index direction can be important:

```javascript
// Index with mixed directions
db.events.createIndex({ date: -1, priority: 1 })

// Efficient sorts:
db.events.find().sort({ date: -1, priority: 1 })   // ✅ Matches index
db.events.find().sort({ date: 1, priority: -1 })   // ✅ Reverse scan

// Inefficient sorts:
db.events.find().sort({ date: -1, priority: -1 })  // ❌ In-memory sort
db.events.find().sort({ date: 1, priority: 1 })    // ❌ In-memory sort
```

## Covered Queries

A covered query is one where all queried fields are in the index:

```javascript
// Compound index
db.users.createIndex({ username: 1, email: 1, age: 1 })

// Covered query - only returns indexed fields
db.users.find(
  { username: "alice" },
  { _id: 0, username: 1, email: 1, age: 1 }  // Projection
)

// Check if query is covered:
db.users.find(
  { username: "alice" },
  { _id: 0, username: 1, email: 1, age: 1 }
).explain("executionStats")

// Look for: "totalDocsExamined": 0
// This means no documents were fetched - only index used!
```

## Compound Index with Array Field

You can include one array field in a compound index:

```javascript
// One array field allowed
db.blog.createIndex({ 
  tags: 1,        // Array field (multikey)
  published: 1,   // Scalar field
  date: -1        // Scalar field
})

// Efficient queries:
db.blog.find({ tags: "mongodb", published: true })
  .sort({ date: -1 })

// Remember: Only ONE array field allowed
db.collection.createIndex({ 
  array1: 1,  // Array
  array2: 1   // Array - ERROR!
})
```

## Real-World Example: Social Media Platform

```javascript
// User posts collection
db.posts.insertMany([
  {
    userId: "u1",
    status: "published",
    category: "technology",
    createdAt: new Date("2026-01-20"),
    views: 1500,
    likes: 45,
    title: "MongoDB Indexing Guide"
  },
  {
    userId: "u1",
    status: "draft",
    category: "technology",
    createdAt: new Date("2026-01-25"),
    views: 0,
    likes: 0,
    title: "Upcoming Post"
  },
  {
    userId: "u2",
    status: "published",
    category: "lifestyle",
    createdAt: new Date("2026-01-22"),
    views: 2300,
    likes: 78,
    title: "Daily Routines"
  }
])

// Index 1: User's published posts by date
db.posts.createIndex({ 
  userId: 1,          // Equality - which user
  status: 1,          // Equality - published/draft
  createdAt: -1       // Sort - newest first
})

// Index 2: Category posts sorted by popularity
db.posts.createIndex({
  category: 1,        // Equality - which category
  status: 1,          // Equality - published only
  likes: -1,          // Sort - most liked first
  createdAt: -1       // Secondary sort
})

// Query 1: Get user's published posts
db.posts.find({ 
  userId: "u1", 
  status: "published" 
}).sort({ createdAt: -1 })

// Query 2: Top posts in category
db.posts.find({ 
  category: "technology", 
  status: "published" 
}).sort({ likes: -1, createdAt: -1 })

// Query 3: All user's posts (uses index prefix)
db.posts.find({ userId: "u1" }).sort({ createdAt: -1 })
```

## Performance Analysis

### Before Compound Index
```javascript
db.orders.find({ 
  customerId: "c123", 
  status: "pending" 
}).sort({ orderDate: -1 }).explain("executionStats")

// Results:
// - executionTimeMillis: 450ms
// - totalDocsExamined: 50000
// - stage: "COLLSCAN" (collection scan)
// - Used in-memory sort
```

### After Creating Compound Index
```javascript
db.orders.createIndex({ 
  customerId: 1, 
  status: 1, 
  orderDate: -1 
})

db.orders.find({ 
  customerId: "c123", 
  status: "pending" 
}).sort({ orderDate: -1 }).explain("executionStats")

// Results:
// - executionTimeMillis: 5ms
// - totalDocsExamined: 3
// - stage: "IXSCAN" (index scan)
// - No in-memory sort needed
```

## Index Intersection vs Compound Index

MongoDB can use multiple single-field indexes (index intersection), but compound indexes are more efficient:

```javascript
// Option 1: Two single-field indexes
db.products.createIndex({ category: 1 })
db.products.createIndex({ price: 1 })

// Option 2: One compound index (BETTER!)
db.products.createIndex({ category: 1, price: 1 })

// Query
db.products.find({ category: "Electronics", price: { $lt: 500 } })

// Option 1: May use index intersection (slower)
// Option 2: Uses compound index (faster, more efficient)
```

## Common Patterns

### 1. Time-Series Data
```javascript
// Sensor data
db.sensors.createIndex({ 
  sensorId: 1,        // Which sensor
  timestamp: -1       // When (newest first)
})

db.sensors.find({ 
  sensorId: "temp-01",
  timestamp: { $gte: new Date("2026-01-01") }
}).sort({ timestamp: -1 })
```

### 2. Multi-Tenant Applications
```javascript
// Multi-tenant data
db.data.createIndex({ 
  tenantId: 1,        // Which tenant
  userId: 1,          // Which user
  createdAt: -1       // When
})

db.data.find({ 
  tenantId: "tenant1", 
  userId: "user123" 
}).sort({ createdAt: -1 })
```

### 3. Geolocation with Filters
```javascript
// Stores with location and category
db.stores.createIndex({ 
  city: 1,            // Which city
  category: 1,        // What type
  rating: -1          // Best rated first
})

db.stores.find({ 
  city: "New York", 
  category: "Restaurant" 
}).sort({ rating: -1 })
```

### 4. User Activity Tracking
```javascript
// Activity logs
db.activities.createIndex({ 
  userId: 1,          // Which user
  type: 1,            // What activity
  timestamp: -1       // When (newest first)
})

db.activities.find({ 
  userId: "u123", 
  type: "login" 
}).sort({ timestamp: -1 })
```

## Avoiding Common Mistakes

### Mistake 1: Wrong Field Order
```javascript
// ❌ BAD: Range field first
db.orders.createIndex({ 
  orderDate: -1,      // Range field
  customerId: 1,      // Equality field
  status: 1           // Equality field
})

// ✅ GOOD: Equality fields first (ESR rule)
db.orders.createIndex({ 
  customerId: 1,      // Equality
  status: 1,          // Equality
  orderDate: -1       // Range
})
```

### Mistake 2: Too Many Fields
```javascript
// ❌ BAD: Index with too many fields (rarely all used)
db.collection.createIndex({ 
  field1: 1, 
  field2: 1, 
  field3: 1, 
  field4: 1, 
  field5: 1,
  field6: 1
})

// ✅ GOOD: Index based on actual query patterns (2-4 fields typical)
db.collection.createIndex({ field1: 1, field2: 1, field3: -1 })
```

### Mistake 3: Duplicate Functionality
```javascript
// ❌ BAD: Redundant indexes
db.users.createIndex({ email: 1 })
db.users.createIndex({ email: 1, name: 1 })  // Redundant for email-only queries

// ✅ GOOD: Keep compound index, remove single-field
db.users.dropIndex({ email: 1 })
db.users.createIndex({ email: 1, name: 1 })  // Supports both query types
```

### Mistake 4: Ignoring Sort Direction
```javascript
// Query pattern: Sort by date DESC, then priority ASC
db.tasks.find().sort({ date: -1, priority: 1 })

// ❌ BAD: Wrong directions
db.tasks.createIndex({ date: 1, priority: -1 })

// ✅ GOOD: Matching directions
db.tasks.createIndex({ date: -1, priority: 1 })
```

## Monitoring and Optimization

### Check Index Usage
```javascript
// View index usage statistics
db.orders.aggregate([
  { $indexStats: {} }
])

// Output shows:
// - accesses.ops: Number of times index was used
// - accesses.since: When tracking started
```

### Analyze Query Performance
```javascript
// Detailed execution stats
db.orders.find({ 
  customerId: "c123", 
  status: "pending" 
}).sort({ orderDate: -1 })
  .explain("executionStats")

// Look for:
// - executionTimeMillis: Query execution time
// - totalKeysExamined: Index entries scanned
// - totalDocsExamined: Documents examined
// - stage: "IXSCAN" (good) vs "COLLSCAN" (bad)
```

### Index Recommendations
```javascript
// Enable profiling to capture slow queries
db.setProfilingLevel(1, { slowms: 100 })

// View slow queries
db.system.profile.find({ millis: { $gt: 100 } }).sort({ ts: -1 })

// Analyze patterns and create appropriate indexes
```

## Best Practices

1. **Design Based on Query Patterns**: Analyze your most frequent queries first
2. **Follow ESR Rule**: Equality, Sort, Range for optimal performance
3. **Use Index Prefixes**: Design compound indexes to support multiple query patterns
4. **Limit Index Count**: Too many indexes slow down writes
5. **Monitor Performance**: Regularly check index usage with `$indexStats`
6. **Consider Cardinality**: Put high-cardinality fields first (more unique values)
7. **Test with Real Data**: Index performance varies with data distribution
8. **Use Covered Queries**: Include all queried fields in index when possible

## Cardinality Considerations

Field cardinality affects index efficiency:

```javascript
// High cardinality (good for first position)
userId: millions of unique values

// Medium cardinality
category: dozens to hundreds of unique values

// Low cardinality (use later in compound index)
status: 3-5 unique values (active, inactive, pending)

// Optimal order:
db.collection.createIndex({ 
  userId: 1,      // High cardinality - most selective
  category: 1,    // Medium cardinality
  status: 1       // Low cardinality
})
```

## Index Size Considerations

```javascript
// Check index sizes
db.orders.stats()

// Output includes:
// - indexSizes: { 
//     "_id_": 500000,
//     "customerId_1_status_1_orderDate_-1": 1200000 
//   }

// Compound indexes are larger than single-field indexes
// Trade-off: Larger size but much better query performance
```

## Advanced Example: Analytics Dashboard

```javascript
// Page view analytics
db.pageviews.insertMany([
  {
    url: "/products",
    userId: "u123",
    sessionId: "s456",
    timestamp: new Date("2026-01-20T10:30:00"),
    country: "US",
    device: "mobile"
  },
  // ... more documents
])

// Index 1: User activity analysis
db.pageviews.createIndex({ 
  userId: 1,          // Which user
  timestamp: -1       // When (newest first)
})

// Index 2: URL performance by country
db.pageviews.createIndex({ 
  url: 1,             // Which page
  country: 1,         // Which country
  timestamp: -1       // When
})

// Index 3: Device analytics
db.pageviews.createIndex({ 
  device: 1,          // Which device type
  url: 1,             // Which page
  timestamp: -1       // When
})

// Query 1: User's recent activity
db.pageviews.find({ userId: "u123" })
  .sort({ timestamp: -1 })
  .limit(50)

// Query 2: Page views by country today
db.pageviews.find({ 
  url: "/products",
  country: "US",
  timestamp: { $gte: new Date("2026-01-31") }
})

// Query 3: Mobile traffic analysis
db.pageviews.find({ 
  device: "mobile",
  url: "/products"
}).sort({ timestamp: -1 })
```

## Summary

Compound indexes are powerful tools for optimizing MongoDB queries:
- Index multiple fields in a single index structure
- Field order is critical for performance
- Follow the ESR rule: Equality, Sort, Range
- Support queries on index prefixes
- More efficient than index intersection
- Essential for complex query patterns
- Balance index count with write performance

Remember: The best compound index design comes from analyzing your actual query patterns and understanding your data access patterns.

## Next Steps
- Learn about Text Indexes for full-text search
- Explore Geospatial Indexes for location queries
- Study Partial Indexes to reduce index size
- Understand Index Build Performance and strategies
