# Using explain() to Verify Index Usage in MongoDB

## Overview
The `explain()` method is one of the most powerful tools for understanding how MongoDB executes queries. It shows you whether indexes are being used, how many documents are scanned, execution time, and much more. This is essential for query optimization and index validation.

## Why Use explain()?
- ✅ **Verify Index Usage**: Confirm your queries are using indexes
- ✅ **Performance Analysis**: Measure query execution time
- ✅ **Query Optimization**: Identify slow queries and bottlenecks
- ✅ **Index Validation**: Ensure indexes are effective
- ✅ **Debugging**: Understand why queries are slow
- ✅ **Plan Analysis**: See how MongoDB plans to execute a query

## Basic Syntax

```javascript
db.collection.find(query).explain()

// Or with verbosity mode
db.collection.find(query).explain("queryPlanner")     // Default
db.collection.find(query).explain("executionStats")   // Recommended
db.collection.find(query).explain("allPlansExecution") // Detailed
```

## Verbosity Modes

### 1. queryPlanner (Default)
Returns the query plan without executing the query.

```javascript
db.users.find({ email: "user@example.com" }).explain("queryPlanner")

// Shows:
// - Which index will be used
// - Query plan stages
// - Winning plan vs rejected plans
// - Does NOT execute the query
```

### 2. executionStats (Most Useful)
Executes the query and returns detailed statistics.

```javascript
db.users.find({ email: "user@example.com" }).explain("executionStats")

// Shows everything from queryPlanner PLUS:
// - Actual execution time
// - Number of documents examined
// - Number of documents returned
// - Index keys examined
// - Execution stages with stats
```

### 3. allPlansExecution (Most Detailed)
Returns stats for all candidate plans.

```javascript
db.users.find({ email: "user@example.com" }).explain("allPlansExecution")

// Shows everything from executionStats PLUS:
// - Stats for all considered plans
// - Why certain plans were rejected
// - Complete execution details
```

## Understanding explain() Output

### Key Fields to Look For

#### 1. winningPlan
Shows the plan MongoDB chose to execute:

```javascript
{
  "queryPlanner": {
    "winningPlan": {
      "stage": "FETCH",
      "inputStage": {
        "stage": "IXSCAN",           // ✅ GOOD: Using index
        "indexName": "email_1",
        "indexBounds": {...}
      }
    }
  }
}
```

#### 2. executionStats
Critical performance metrics:

```javascript
{
  "executionStats": {
    "executionSuccess": true,
    "nReturned": 1,              // Documents returned to client
    "executionTimeMillis": 2,     // Total execution time
    "totalKeysExamined": 1,       // Index entries scanned
    "totalDocsExamined": 1,       // Documents examined
    "executionStages": {...}
  }
}
```

#### 3. executionStages
Detailed breakdown of execution:

```javascript
{
  "executionStages": {
    "stage": "FETCH",
    "nReturned": 1,
    "executionTimeMillisEstimate": 0,
    "inputStage": {
      "stage": "IXSCAN",
      "nReturned": 1,
      "indexName": "email_1"
    }
  }
}
```

## Common Stage Types

### COLLSCAN (Collection Scan) - ⚠️ Usually Bad
```javascript
{
  "stage": "COLLSCAN",    // ⚠️ Scanning entire collection
  "direction": "forward"
}

// Means: No index used, scanning all documents
// Action: Create an appropriate index!
```

### IXSCAN (Index Scan) - ✅ Good
```javascript
{
  "stage": "IXSCAN",      // ✅ Using an index
  "indexName": "email_1",
  "indexBounds": {
    "email": [["user@example.com", "user@example.com"]]
  }
}

// Means: Query is using an index
// Action: Good! Monitor to ensure it stays efficient
```

### FETCH - ✅ Normal
```javascript
{
  "stage": "FETCH",       // Retrieving actual documents
  "inputStage": {
    "stage": "IXSCAN"     // After index scan
  }
}

// Means: Using index to find docs, then fetching full documents
// Action: Normal for most queries
```

### SORT - ⚠️ Can Be Problematic
```javascript
{
  "stage": "SORT",        // ⚠️ In-memory sort
  "sortPattern": { "createdAt": -1 },
  "memUsage": 104857600,  // Memory used
  "inputStage": {...}
}

// Means: Sorting in memory (no index for sort)
// Action: Consider creating index with sort fields
```

### PROJECTION_COVERED - ✅ Excellent
```javascript
{
  "stage": "PROJECTION_COVERED",  // ✅ Covered query!
  "transformBy": { "email": 1, "_id": 0 }
}

// Means: Query satisfied entirely from index
// Action: Excellent! No documents fetched
```

## Practical Examples

### Example 1: Checking if Index is Used

```javascript
// Sample collection
db.users.insertMany([
  { name: "Alice", email: "alice@example.com", age: 30 },
  { name: "Bob", email: "bob@example.com", age: 25 },
  { name: "Charlie", email: "charlie@example.com", age: 35 }
])

// Query WITHOUT index
db.users.find({ email: "alice@example.com" }).explain("executionStats")

// Output shows:
{
  "executionStats": {
    "executionTimeMillis": 15,
    "totalKeysExamined": 0,        // ⚠️ No index keys examined
    "totalDocsExamined": 3,        // ⚠️ All documents scanned
    "executionStages": {
      "stage": "COLLSCAN"          // ⚠️ Collection scan!
    }
  }
}

// Create index
db.users.createIndex({ email: 1 })

// Query WITH index
db.users.find({ email: "alice@example.com" }).explain("executionStats")

// Output shows:
{
  "executionStats": {
    "executionTimeMillis": 0,
    "totalKeysExamined": 1,        // ✅ Only 1 index entry
    "totalDocsExamined": 1,        // ✅ Only 1 document
    "executionStages": {
      "stage": "FETCH",
      "inputStage": {
        "stage": "IXSCAN",         // ✅ Using index!
        "indexName": "email_1"
      }
    }
  }
}
```

### Example 2: Analyzing Compound Index Usage

```javascript
// Create compound index
db.orders.createIndex({ customerId: 1, status: 1, orderDate: -1 })

// Query using full index
db.orders.find({ 
  customerId: "c123", 
  status: "pending" 
}).sort({ orderDate: -1 }).explain("executionStats")

// Output:
{
  "winningPlan": {
    "stage": "FETCH",
    "inputStage": {
      "stage": "IXSCAN",
      "indexName": "customerId_1_status_1_orderDate_-1",  // ✅ Using compound index
      "indexBounds": {
        "customerId": [["c123", "c123"]],
        "status": [["pending", "pending"]],
        "orderDate": [["MaxKey", "MinKey"]]
      }
    }
  },
  "executionStats": {
    "totalKeysExamined": 5,
    "totalDocsExamined": 5
  }
}

// Query using only prefix (still efficient)
db.orders.find({ customerId: "c123" }).explain("executionStats")

// Output shows same index used (prefix supported):
{
  "inputStage": {
    "stage": "IXSCAN",
    "indexName": "customerId_1_status_1_orderDate_-1",  // ✅ Prefix works!
    "indexBounds": {
      "customerId": [["c123", "c123"]],
      "status": [["MinKey", "MaxKey"]],     // Full range
      "orderDate": [["MaxKey", "MinKey"]]   // Full range
    }
  }
}
```

### Example 3: Detecting In-Memory Sorts

```javascript
// Query with sort but no index
db.posts.find({ author: "Alice" }).sort({ createdAt: -1 }).explain("executionStats")

// Output shows in-memory sort:
{
  "executionStats": {
    "executionTimeMillis": 250,  // ⚠️ Slow!
    "executionStages": {
      "stage": "SORT",           // ⚠️ In-memory sort
      "sortPattern": { "createdAt": -1 },
      "memUsage": 524288,
      "inputStage": {
        "stage": "COLLSCAN"      // ⚠️ And collection scan!
      }
    }
  }
}

// Create compound index with sort field
db.posts.createIndex({ author: 1, createdAt: -1 })

// Same query after index
db.posts.find({ author: "Alice" }).sort({ createdAt: -1 }).explain("executionStats")

// Output shows index-based sort:
{
  "executionStats": {
    "executionTimeMillis": 5,    // ✅ Much faster!
    "executionStages": {
      "stage": "FETCH",
      "inputStage": {
        "stage": "IXSCAN",       // ✅ Index scan
        "indexName": "author_1_createdAt_-1"
        // No SORT stage - sorted by index!
      }
    }
  }
}
```

### Example 4: Covered Query

```javascript
// Create index
db.products.createIndex({ category: 1, price: 1, name: 1 })

// Covered query - only request indexed fields
db.products.find(
  { category: "Electronics" },
  { _id: 0, category: 1, price: 1, name: 1 }  // Projection
).explain("executionStats")

// Output shows covered query:
{
  "executionStats": {
    "totalKeysExamined": 10,
    "totalDocsExamined": 0,      // ✅ ZERO documents examined!
    "executionStages": {
      "stage": "PROJECTION_COVERED",  // ✅ Covered query!
      "transformBy": { "_id": 0, "category": 1, "price": 1, "name": 1 },
      "inputStage": {
        "stage": "IXSCAN",
        "indexName": "category_1_price_1_name_1"
      }
    }
  }
}

// Non-covered query - includes non-indexed field
db.products.find(
  { category: "Electronics" },
  { _id: 0, category: 1, price: 1, name: 1, description: 1 }  // description not in index
).explain("executionStats")

// Output shows document fetch:
{
  "executionStats": {
    "totalKeysExamined": 10,
    "totalDocsExamined": 10,     // ⚠️ Had to fetch documents
    "executionStages": {
      "stage": "PROJECTION_SIMPLE",  // Not covered
      "inputStage": {
        "stage": "FETCH",        // Document fetch needed
        "inputStage": {
          "stage": "IXSCAN"
        }
      }
    }
  }
}
```

## Key Metrics Interpretation

### Efficiency Ratio

```javascript
// Good index usage:
{
  "totalKeysExamined": 10,
  "totalDocsExamined": 10,
  "nReturned": 10
}
// Ratio = 1:1:1 (Perfect! Examining exactly what we need)

// Inefficient query:
{
  "totalKeysExamined": 1000,
  "totalDocsExamined": 1000,
  "nReturned": 10
}
// Ratio = 100:100:1 (Bad! Examining 100x more than returning)
// Action: Refine index or query
```

### Execution Time

```javascript
// Fast query
{
  "executionTimeMillis": 2     // ✅ Excellent
}

// Slow query
{
  "executionTimeMillis": 500   // ⚠️ Needs optimization
}

// Very slow query
{
  "executionTimeMillis": 5000  // ❌ Critical! Must optimize
}
```

### Documents Examined vs Returned

```javascript
// Ideal: Equal numbers
{
  "totalDocsExamined": 10,
  "nReturned": 10             // ✅ Perfect selectivity
}

// Problematic: Large difference
{
  "totalDocsExamined": 10000,
  "nReturned": 10             // ⚠️ Poor selectivity
}
// Consider: More selective index or query refinement
```

## Using explain() with Different Operations

### With find()
```javascript
db.collection.find({ field: "value" }).explain("executionStats")
```

### With aggregate()
```javascript
db.collection.aggregate([
  { $match: { field: "value" } },
  { $group: { _id: "$category", count: { $sum: 1 } } }
], { explain: true })

// Or with verbosity
db.collection.explain("executionStats").aggregate([
  { $match: { field: "value" } }
])
```

### With update()
```javascript
db.collection.explain("executionStats").update(
  { field: "value" },
  { $set: { updated: true } }
)
```

### With delete()
```javascript
db.collection.explain("executionStats").remove({ field: "value" })
```

### With count()
```javascript
db.collection.explain("executionStats").count({ field: "value" })
```

## Reading Index Bounds

Index bounds show the range of index entries scanned:

```javascript
// Equality query
db.users.find({ age: 25 }).explain()

"indexBounds": {
  "age": [
    [25, 25]     // Exact match: only value 25
  ]
}

// Range query
db.users.find({ age: { $gte: 25, $lt: 30 } }).explain()

"indexBounds": {
  "age": [
    [25, 30)     // Range: 25 (inclusive) to 30 (exclusive)
  ]
}

// Multiple ranges with $in
db.users.find({ age: { $in: [25, 30, 35] } }).explain()

"indexBounds": {
  "age": [
    [25, 25],
    [30, 30],
    [35, 35]
  ]
}
```

## Identifying Problems

### Problem 1: No Index Used (COLLSCAN)

```javascript
// Symptom
{
  "stage": "COLLSCAN",
  "totalDocsExamined": 1000000,  // Scanned all docs!
  "executionTimeMillis": 2500
}

// Solution
db.collection.createIndex({ queryField: 1 })
```

### Problem 2: In-Memory Sort

```javascript
// Symptom
{
  "stage": "SORT",
  "sortPattern": { "date": -1 },
  "memUsage": 33554432
}

// Solution
db.collection.createIndex({ filterField: 1, date: -1 })
```

### Problem 3: Low Selectivity

```javascript
// Symptom
{
  "totalDocsExamined": 50000,
  "nReturned": 100,           // Only 0.2% relevant!
  "executionTimeMillis": 500
}

// Solutions:
// 1. More selective index (compound index)
// 2. Refine query criteria
// 3. Add filters to reduce result set
```

### Problem 4: Wrong Index Used

```javascript
// Available indexes:
// - { email: 1 }
// - { email: 1, status: 1, createdAt: -1 }

// Query
db.users.find({ email: "user@example.com", status: "active" })
  .sort({ createdAt: -1 })
  .explain()

// If output shows:
"indexName": "email_1"  // ⚠️ Using less optimal index!

// Force better index with hint():
db.users.find({ email: "user@example.com", status: "active" })
  .sort({ createdAt: -1 })
  .hint({ email: 1, status: 1, createdAt: -1 })
  .explain()
```

## Comparing Query Plans

### Before and After Index Creation

```javascript
// Before
const before = db.collection.find({ field: "value" })
  .explain("executionStats")

console.log("Before:", {
  time: before.executionStats.executionTimeMillis,
  docsExamined: before.executionStats.totalDocsExamined,
  stage: before.executionStats.executionStages.stage
})

// Create index
db.collection.createIndex({ field: 1 })

// After
const after = db.collection.find({ field: "value" })
  .explain("executionStats")

console.log("After:", {
  time: after.executionStats.executionTimeMillis,
  docsExamined: after.executionStats.totalDocsExamined,
  stage: after.executionStats.executionStages.stage
})
```

## Best Practices

### 1. Always Use executionStats
```javascript
// ❌ Less useful
db.collection.find(query).explain()

// ✅ More useful
db.collection.find(query).explain("executionStats")
```

### 2. Check Key Metrics
```javascript
const stats = db.collection.find(query).explain("executionStats")

// Focus on:
// 1. executionTimeMillis - How long?
// 2. totalDocsExamined - How many docs scanned?
// 3. nReturned - How many returned?
// 4. stage - IXSCAN (good) or COLLSCAN (bad)?
// 5. indexName - Which index used?
```

### 3. Look for Red Flags
```javascript
// 🚩 COLLSCAN on large collections
// 🚩 High totalDocsExamined vs nReturned ratio
// 🚩 In-memory SORT
// 🚩 executionTimeMillis > acceptable threshold
// 🚩 totalKeysExamined >> nReturned
```

### 4. Test with Production-Like Data
```javascript
// Index performance varies with data size and distribution
// Always test with realistic data volumes

// Good practice: Test with subset of production data
// mongodump --query='{"createdAt":{$gte:ISODate("2026-01-01")}}' ...
```

### 5. Use hint() for Testing
```javascript
// Force specific index to test performance
db.collection.find(query)
  .hint({ field: 1 })
  .explain("executionStats")

// Compare with natural selection
db.collection.find(query)
  .hint({ $natural: 1 })  // No index (collection scan)
  .explain("executionStats")
```

## Advanced: Analyzing Complex Queries

### Aggregation Pipeline

```javascript
db.orders.explain("executionStats").aggregate([
  { $match: { status: "completed" } },
  { $group: { 
      _id: "$customerId", 
      total: { $sum: "$amount" } 
    }
  },
  { $sort: { total: -1 } },
  { $limit: 10 }
])

// Check each stage:
"stages": [
  {
    "$cursor": {
      "queryPlanner": {
        "winningPlan": {
          "stage": "FETCH",
          "inputStage": {
            "stage": "IXSCAN",  // ✅ $match uses index
            "indexName": "status_1"
          }
        }
      }
    }
  },
  { "$group": {...} },
  { "$sort": {...} },
  { "$limit": {...} }
]
```

### Multi-Stage Execution

```javascript
db.collection.find({ field1: "value1", field2: "value2" })
  .sort({ field3: -1 })
  .limit(10)
  .explain("executionStats")

// Analyze execution flow:
"executionStages": {
  "stage": "LIMIT",
  "inputStage": {
    "stage": "FETCH",
    "inputStage": {
      "stage": "IXSCAN",
      "indexName": "field1_1_field2_1_field3_-1",
      "keysExamined": 10,      // ✅ Only examined what's needed
      "docsExamined": 10
    }
  }
}
```

## Real-World Debugging Example

```javascript
// Slow query report: Users complaining about slow search
db.products.find({ 
  category: "Electronics",
  price: { $lte: 500 },
  inStock: true
}).sort({ popularity: -1 }).limit(20)

// Step 1: Check current performance
const explain = db.products.find({ 
  category: "Electronics",
  price: { $lte: 500 },
  inStock: true
}).sort({ popularity: -1 }).limit(20).explain("executionStats")

// Output shows:
{
  "executionTimeMillis": 1500,  // 🚩 Very slow!
  "totalDocsExamined": 100000,  // 🚩 Scanning too many
  "nReturned": 20,
  "executionStages": {
    "stage": "LIMIT",
    "inputStage": {
      "stage": "SORT",          // 🚩 In-memory sort
      "inputStage": {
        "stage": "FETCH",
        "inputStage": {
          "stage": "IXSCAN",
          "indexName": "category_1"  // 🚩 Suboptimal index
        }
      }
    }
  }
}

// Step 2: Create optimized index following ESR rule
db.products.createIndex({ 
  category: 1,        // Equality
  inStock: 1,         // Equality
  price: 1,           // Range
  popularity: -1      // Sort
})

// Step 3: Test again
const explainAfter = db.products.find({ 
  category: "Electronics",
  price: { $lte: 500 },
  inStock: true
}).sort({ popularity: -1 }).limit(20).explain("executionStats")

// Output shows:
{
  "executionTimeMillis": 5,     // ✅ Much faster!
  "totalDocsExamined": 20,      // ✅ Only examined what's needed
  "nReturned": 20,
  "executionStages": {
    "stage": "LIMIT",
    "inputStage": {
      "stage": "FETCH",
      "inputStage": {
        "stage": "IXSCAN",
        "indexName": "category_1_inStock_1_price_1_popularity_-1"
        // No SORT stage - sorted by index!
      }
    }
  }
}

// Result: 300x faster! (1500ms → 5ms)
```

## Summary

### Essential explain() Usage

```javascript
// Always use this for performance analysis:
db.collection.find(query).explain("executionStats")
```

### What to Look For

✅ **Good Signs:**
- `stage: "IXSCAN"` - Using an index
- `totalDocsExamined ≈ nReturned` - Good selectivity
- Low `executionTimeMillis` - Fast execution
- `PROJECTION_COVERED` - Covered query
- No `SORT` stage - Sorted by index

⚠️ **Warning Signs:**
- `stage: "COLLSCAN"` - No index used
- `stage: "SORT"` - In-memory sort
- `totalDocsExamined >> nReturned` - Poor selectivity
- High `executionTimeMillis` - Slow query
- Large `memUsage` - Memory intensive

### Quick Checklist

1. ✅ Is an index being used? (`IXSCAN` vs `COLLSCAN`)
2. ✅ Is it the right index? (check `indexName`)
3. ✅ How many documents examined vs returned?
4. ✅ Is there an in-memory sort? (`SORT` stage)
5. ✅ What's the execution time? (`executionTimeMillis`)
6. ✅ Can it be a covered query? (`PROJECTION_COVERED`)

### Remember

- Use `explain("executionStats")` for actual performance data
- Compare metrics before and after index creation
- Look at the ratio of documents examined to returned
- Check for COLLSCAN and SORT stages
- Test with production-like data volumes
- Monitor regularly to ensure indexes remain effective

## Next Steps
- Learn about Index Selection and Query Planner
- Explore Performance Profiling tools
- Study Index Build Optimization
- Understand Query Optimization techniques
