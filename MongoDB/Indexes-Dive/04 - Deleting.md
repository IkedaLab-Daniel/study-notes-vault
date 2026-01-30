# Deleting and Hiding Indexes in MongoDB

## Overview
MongoDB provides multiple methods to manage indexes, including permanently deleting them or temporarily hiding them. Understanding when and how to use these operations is crucial for database maintenance and performance optimization.

## Why Delete or Hide Indexes?

### Reasons to Delete Indexes:
- **Unused Indexes**: Consuming disk space without providing value
- **Redundant Indexes**: Duplicating functionality of other indexes
- **Wrong Design**: Index doesn't match actual query patterns
- **Performance Impact**: Too many indexes slowing down writes
- **Schema Changes**: Data model has changed, making index obsolete

### Reasons to Hide Indexes:
- **Testing**: Evaluate performance impact before permanent deletion
- **Temporary Deactivation**: Disable during bulk operations
- **Gradual Rollback**: Test if removing index causes issues
- **Performance Analysis**: Compare query performance with/without index

## Deleting Indexes

### 1. Drop Index by Name
```javascript
// Drop a specific index by its name
db.collection.dropIndex("indexName")

// Example
db.users.dropIndex("email_1")
```

### 2. Drop Index by Specification
```javascript
// Drop index using the same specification used to create it
db.collection.dropIndex({ field: 1 })

// Examples
db.users.dropIndex({ email: 1 })
db.orders.dropIndex({ customerId: 1, status: 1 })
db.products.dropIndex({ category: 1, price: -1 })
```

### 3. Drop All Indexes
```javascript
// Drop all indexes EXCEPT the _id index
db.collection.dropIndexes()

// Example
db.products.dropIndexes()

// Note: The _id index cannot be dropped
```

### 4. Drop Multiple Specific Indexes
```javascript
// Drop indexes one by one
db.collection.dropIndex("index1")
db.collection.dropIndex("index2")
db.collection.dropIndex("index3")

// Or drop all and recreate what you need
db.collection.dropIndexes()
db.collection.createIndex({ field: 1 })
```

## Finding Index Names

Before deleting, you need to know the index name:

```javascript
// List all indexes with their names
db.collection.getIndexes()

// Output example:
[
  {
    "v": 2,
    "key": { "_id": 1 },
    "name": "_id_"
  },
  {
    "v": 2,
    "key": { "email": 1 },
    "name": "email_1"
  },
  {
    "v": 2,
    "key": { "customerId": 1, "status": 1 },
    "name": "customerId_1_status_1"
  }
]
```

## Hiding Indexes (MongoDB 4.4+)

Hiding indexes allows you to test the impact of removing an index without actually deleting it.

### Hide an Index
```javascript
// Hide index by name
db.collection.hideIndex("indexName")

// Hide index by specification
db.collection.hideIndex({ field: 1 })

// Examples
db.users.hideIndex("email_1")
db.products.hideIndex({ category: 1, price: -1 })
```

### Unhide an Index
```javascript
// Unhide index by name
db.collection.unhideIndex("indexName")

// Unhide index by specification  
db.collection.unhideIndex({ field: 1 })

// Examples
db.users.unhideIndex("email_1")
db.products.unhideIndex({ category: 1, price: -1 })
```

### Check if Index is Hidden
```javascript
// View all indexes and their hidden status
db.collection.getIndexes()

// Output shows "hidden: true" for hidden indexes:
[
  {
    "v": 2,
    "key": { "email": 1 },
    "name": "email_1",
    "hidden": true  // This index is hidden
  }
]
```

## Practical Examples

### Example 1: Removing Unused Index
```javascript
// Step 1: Check index usage
db.products.aggregate([{ $indexStats: {} }])

// Output shows index is never used:
{
  "name": "oldCategory_1",
  "key": { "oldCategory": 1 },
  "host": "localhost:27017",
  "accesses": {
    "ops": 0,        // Never used!
    "since": ISODate("2026-01-01T00:00:00.000Z")
  }
}

// Step 2: Hide the index first (safe approach)
db.products.hideIndex("oldCategory_1")

// Step 3: Monitor for a few days/weeks
// If no issues arise...

// Step 4: Permanently delete
db.products.dropIndex("oldCategory_1")
```

### Example 2: Removing Redundant Indexes
```javascript
// Current indexes
db.orders.getIndexes()
// [
//   { "key": { "customerId": 1 }, "name": "customerId_1" },
//   { "key": { "customerId": 1, "status": 1 }, "name": "customerId_1_status_1" }
// ]

// The single-field index is redundant!
// The compound index supports queries on customerId alone

// Remove the redundant index
db.orders.dropIndex("customerId_1")

// Keep only the compound index
// It supports both:
// - { customerId: 1 }
// - { customerId: 1, status: 1 }
```

### Example 3: Testing Performance Impact
```javascript
// You suspect an index isn't helping
db.logs.getIndexes()
// Shows: "timestamp_1" index

// Hide it to test performance
db.logs.hideIndex("timestamp_1")

// Run your typical queries and monitor performance
db.logs.find({ timestamp: { $gte: new Date("2026-01-01") } })
  .explain("executionStats")

// If performance degrades:
db.logs.unhideIndex("timestamp_1")  // Restore it

// If performance is fine or better:
db.logs.dropIndex("timestamp_1")    // Delete permanently
```

### Example 4: Bulk Operation Optimization
```javascript
// Before bulk insert, hide indexes to speed up writes
db.analytics.hideIndex("userId_1_timestamp_-1")
db.analytics.hideIndex("eventType_1")

// Perform bulk operation
db.analytics.insertMany([
  // ... millions of documents
], { ordered: false })

// Re-enable indexes
db.analytics.unhideIndex("userId_1_timestamp_-1")
db.analytics.unhideIndex("eventType_1")
```

## Safety Considerations

### 1. Cannot Drop _id Index
```javascript
// This will fail
db.collection.dropIndex("_id_")
// Error: can't drop _id index
```

### 2. Impact on Running Queries
```javascript
// Dropping an index while queries are using it may cause:
// - Queries to fall back to collection scans
// - Sudden performance degradation
// - Increased load on database

// Best practice: Hide first, monitor, then drop
db.collection.hideIndex("indexName")
// Monitor for issues
db.collection.dropIndex("indexName")
```

### 3. Backup Index Definitions
```javascript
// Before dropping, save index definitions
const indexes = db.collection.getIndexes()
print(JSON.stringify(indexes, null, 2))

// Or export to a file (in shell)
// mongosh --eval "printjson(db.collection.getIndexes())" > indexes_backup.json

// This allows you to recreate indexes if needed
```

### 4. Production Best Practices
```javascript
// ❌ BAD: Drop index directly in production
db.products.dropIndex("category_1")

// ✅ GOOD: Safe approach
// Step 1: Hide the index
db.products.hideIndex("category_1")

// Step 2: Monitor for 24-48 hours
// Check slow query logs, application performance, user reports

// Step 3: If no issues, drop permanently
db.products.dropIndex("category_1")

// Step 4: If issues occur, unhide immediately
db.products.unhideIndex("category_1")
```

## When Hidden Indexes Are Used

Hidden indexes are NOT used by the query planner, except:

```javascript
// Hidden indexes are still used by:
// - Explicit hint() commands
db.collection.find({ field: "value" }).hint("hidden_index_name")

// - TTL (Time To Live) operations
// - Unique constraint validation
```

## Monitoring Index Usage

### Method 1: Using $indexStats
```javascript
// Get index usage statistics
db.collection.aggregate([
  { $indexStats: {} }
])

// Output:
[
  {
    "name": "email_1",
    "key": { "email": 1 },
    "host": "localhost:27017",
    "accesses": {
      "ops": 15234,      // Times used
      "since": ISODate("2026-01-01T00:00:00.000Z")
    }
  },
  {
    "name": "unused_index_1",
    "key": { "oldField": 1 },
    "accesses": {
      "ops": 0,          // Never used!
      "since": ISODate("2026-01-01T00:00:00.000Z")
    }
  }
]
```

### Method 2: Query Profiler
```javascript
// Enable profiling for slow queries
db.setProfilingLevel(1, { slowms: 100 })

// Check profiled queries
db.system.profile.find().sort({ ts: -1 }).limit(10)

// Analyze which indexes are being used
db.system.profile.aggregate([
  { $group: { 
      _id: "$planSummary", 
      count: { $sum: 1 } 
    }
  },
  { $sort: { count: -1 } }
])
```

### Method 3: Explain Plans
```javascript
// Check if queries use expected index
db.collection.find({ field: "value" }).explain("executionStats")

// Look for:
// - "stage": "IXSCAN" (using index) vs "COLLSCAN" (not using index)
// - "indexName": Which index was used
```

## Recreating Deleted Indexes

If you need to recreate an index you deleted:

```javascript
// Save index definition before dropping
const indexDef = db.collection.getIndexes().find(idx => idx.name === "email_1")

// Later, recreate using the saved definition
db.collection.createIndex(
  indexDef.key,
  {
    name: indexDef.name,
    unique: indexDef.unique || false,
    sparse: indexDef.sparse || false
    // ... other options
  }
)
```

## Common Scenarios

### Scenario 1: Identifying Unused Indexes
```javascript
// Find all collections and their indexes
db.getCollectionNames().forEach(function(collName) {
  print("\n=== Collection: " + collName + " ===")
  db[collName].aggregate([{ $indexStats: {} }]).forEach(function(idx) {
    if (idx.accesses.ops === 0) {
      print("UNUSED: " + idx.name + " - " + JSON.stringify(idx.key))
    }
  })
})
```

### Scenario 2: Cleaning Up After Schema Migration
```javascript
// Old schema had 'email' field, new schema has 'emailAddress'

// List indexes
db.users.getIndexes()
// Shows: "email_1" (old), "emailAddress_1" (new)

// Verify new index is being used
db.users.find({ emailAddress: "user@example.com" }).explain()

// Remove old index
db.users.dropIndex("email_1")
```

### Scenario 3: Removing Indexes Before Major Bulk Update
```javascript
// Save current indexes
const indexes = db.products.getIndexes()

// Drop non-essential indexes (keep _id and unique constraints)
db.products.dropIndex("category_1_price_-1")
db.products.dropIndex("tags_1")
db.products.dropIndex("createdAt_-1")

// Perform bulk update
db.products.updateMany(
  {},
  { $set: { updatedAt: new Date() } }
)

// Recreate indexes
db.products.createIndex({ category: 1, price: -1 })
db.products.createIndex({ tags: 1 })
db.products.createIndex({ createdAt: -1 })
```

### Scenario 4: A/B Testing Index Strategies
```javascript
// Strategy A: Current index
db.orders.getIndexes()
// Shows: { customerId: 1, createdAt: -1 }

// Test Strategy B: Hide current, create new
db.orders.hideIndex("customerId_1_createdAt_-1")
db.orders.createIndex({ customerId: 1, status: 1, createdAt: -1 })

// Monitor performance with new index
// ... wait and analyze ...

// If Strategy B is better:
db.orders.dropIndex("customerId_1_createdAt_-1")

// If Strategy A was better:
db.orders.unhideIndex("customerId_1_createdAt_-1")
db.orders.dropIndex("customerId_1_status_1_createdAt_-1")
```

## Error Handling

### Error: Index Not Found
```javascript
db.collection.dropIndex("nonexistent_index")
// Error: index not found with name [nonexistent_index]

// Always check if index exists first
const indexes = db.collection.getIndexes()
const indexExists = indexes.some(idx => idx.name === "indexName")
if (indexExists) {
  db.collection.dropIndex("indexName")
}
```

### Error: Cannot Drop _id Index
```javascript
db.collection.dropIndex("_id_")
// Error: can't drop _id index

// The _id index is mandatory and cannot be dropped
```

### Error: Background Operation in Progress
```javascript
db.collection.dropIndex("index_1")
// Error: cannot drop index during index build

// Wait for index build to complete, then try again
db.currentOp()  // Check for running operations
```

## Performance Impact

### Dropping Indexes
- ✅ **Faster writes**: Fewer indexes to update
- ✅ **Less disk space**: Index files are deleted
- ✅ **Reduced memory**: Less index data in RAM
- ❌ **Slower queries**: If queries relied on the index

### Hiding Indexes
- ✅ **Quick operation**: Just marks index as hidden
- ✅ **Easy to reverse**: Unhide is instant
- ✅ **No data loss**: Index structure remains intact
- ❌ **Still uses disk space**: Hidden index not deleted

## Best Practices

### 1. Use Hide Before Drop
```javascript
// Safe workflow:
// 1. Hide index
db.collection.hideIndex("indexName")

// 2. Monitor for issues (24-48 hours recommended)
// 3. If no issues, drop permanently
db.collection.dropIndex("indexName")

// 4. If issues occur, unhide immediately
db.collection.unhideIndex("indexName")
```

### 2. Document Your Changes
```javascript
// Keep a log of index changes
// Before dropping:
const indexDef = db.orders.getIndexes().find(idx => idx.name === "oldIndex_1")
// Save this information: date, reason, definition

// Example log entry:
// Date: 2026-01-31
// Action: Dropped index "oldIndex_1" 
// Reason: Never used (0 ops in 30 days)
// Definition: { customerId: 1, oldStatus: 1 }
```

### 3. Monitor After Changes
```javascript
// After dropping indexes, monitor:
// - Query performance
// - Slow query logs
// - Application metrics
// - Database load

// Enable profiling to catch slow queries
db.setProfilingLevel(1, { slowms: 100 })

// Check for slow queries
db.system.profile.find({ millis: { $gt: 100 } })
  .sort({ ts: -1 })
  .limit(10)
```

### 4. Regular Index Audits
```javascript
// Monthly or quarterly, review indexes:

// Script to find unused indexes
db.getCollectionNames().forEach(function(collName) {
  if (!collName.startsWith("system.")) {
    db[collName].aggregate([{ $indexStats: {} }]).forEach(function(idx) {
      if (idx.name !== "_id_" && idx.accesses.ops < 10) {
        print(collName + ": " + idx.name + " - Used " + idx.accesses.ops + " times")
      }
    })
  }
})
```

### 5. Consider Index Build Time
```javascript
// Dropping is instant, but recreating takes time

// For large collections, consider:
// - Time needed to rebuild if you need to recreate
// - Impact on production during rebuild
// - Whether hiding is sufficient for your use case

// Check collection size before dropping critical indexes
db.collection.stats().size
```

## Advanced: Scripting Index Management

### Bulk Remove Unused Indexes
```javascript
// Find and hide all unused indexes across all collections
db.getCollectionNames().forEach(function(collName) {
  if (!collName.startsWith("system.")) {
    db[collName].aggregate([{ $indexStats: {} }]).forEach(function(idx) {
      if (idx.name !== "_id_" && idx.accesses.ops === 0) {
        print("Hiding: " + collName + "." + idx.name)
        db[collName].hideIndex(idx.name)
      }
    })
  }
})
```

### Export Index Definitions
```javascript
// Export all indexes for backup
const allIndexes = {}
db.getCollectionNames().forEach(function(collName) {
  if (!collName.startsWith("system.")) {
    allIndexes[collName] = db[collName].getIndexes()
  }
})

print(JSON.stringify(allIndexes, null, 2))
// Save output to file for backup
```

### Restore Index Definitions
```javascript
// Given saved index definitions, recreate them
const savedIndexes = {
  "orders": [
    { "key": { "customerId": 1, "status": 1 }, "name": "customerId_1_status_1" }
  ]
  // ... more collections
}

Object.keys(savedIndexes).forEach(function(collName) {
  savedIndexes[collName].forEach(function(idx) {
    if (idx.name !== "_id_") {
      print("Creating: " + collName + "." + idx.name)
      db[collName].createIndex(idx.key, { name: idx.name })
    }
  })
})
```

## Summary

### Deleting Indexes:
- Permanently removes index structure
- Frees up disk space immediately
- Cannot be undone (must recreate)
- Use for confirmed unused or redundant indexes

### Hiding Indexes:
- Temporarily disables index from query planner
- Keeps index structure intact
- Easily reversible
- Perfect for testing impact before deletion

### Recommended Workflow:
1. Identify candidate indexes (unused, redundant)
2. Hide index first
3. Monitor performance (24-48 hours minimum)
4. If no issues, drop permanently
5. If issues arise, unhide immediately
6. Document all changes

### Key Commands:
```javascript
// Deleting
db.collection.dropIndex("indexName")
db.collection.dropIndex({ field: 1 })
db.collection.dropIndexes()

// Hiding/Unhiding
db.collection.hideIndex("indexName")
db.collection.unhideIndex("indexName")

// Viewing
db.collection.getIndexes()
db.collection.aggregate([{ $indexStats: {} }])
```

Remember: Always test in a non-production environment first, and have a rollback plan before making changes to production indexes!

## Next Steps
- Learn about Index Build Performance
- Explore Partial Indexes to reduce index size
- Study Index Maintenance strategies
- Understand Index Statistics and monitoring tools
