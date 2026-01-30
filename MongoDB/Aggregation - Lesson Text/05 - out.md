# Using $out in MongoDB Aggregation

## Overview
The `$out` stage writes the results of an aggregation pipeline to a specified collection. It must be the last stage in the pipeline and replaces the entire contents of the target collection with the aggregation results.

## Why Use $out?
- **Data Transformation**: Transform and store processed data permanently
- **Report Generation**: Create materialized views of aggregated data
- **ETL Operations**: Extract, transform, and load data into new collections
- **Data Archiving**: Store processed historical data
- **Performance**: Pre-compute expensive aggregations for faster queries
- **Data Migration**: Transform and move data between collections

## Basic Syntax

```javascript
db.collection.aggregate([
  // ... aggregation stages ...
  { $out: "targetCollection" }
])
```

### Key Characteristics:
- ⚠️ **Must be the last stage** in the pipeline
- ⚠️ **Replaces entire collection** - all existing documents are removed
- ✅ Creates collection if it doesn't exist
- ✅ Atomic operation - all or nothing
- ⚠️ Cannot write to capped collections
- ⚠️ Cannot write to system collections

## Simple Examples

### Example 1: Basic Usage
```javascript
// Original data
db.orders.insertMany([
  { customer: "Alice", item: "Laptop", price: 1200, quantity: 1 },
  { customer: "Bob", item: "Mouse", price: 25, quantity: 2 },
  { customer: "Alice", item: "Keyboard", price: 75, quantity: 1 },
  { customer: "Charlie", item: "Monitor", price: 300, quantity: 2 }
])

// Calculate total sales per customer and save to new collection
db.orders.aggregate([
  {
    $group: {
      _id: "$customer",
      totalSpent: { $sum: { $multiply: ["$price", "$quantity"] } },
      itemCount: { $sum: "$quantity" }
    }
  },
  {
    $project: {
      _id: 0,
      customer: "$_id",
      totalSpent: 1,
      itemCount: 1
    }
  },
  { $out: "customerSummary" }
])

// Check the results
db.customerSummary.find()
// Output:
// { customer: "Alice", totalSpent: 1275, itemCount: 2 }
// { customer: "Bob", totalSpent: 50, itemCount: 2 }
// { customer: "Charlie", totalSpent: 600, itemCount: 2 }
```

### Example 2: Creating Materialized View
```javascript
// Daily sales summary
db.sales.aggregate([
  {
    $group: {
      _id: {
        year: { $year: "$date" },
        month: { $month: "$date" },
        day: { $dayOfMonth: "$date" }
      },
      totalRevenue: { $sum: "$amount" },
      orderCount: { $sum: 1 },
      avgOrderValue: { $avg: "$amount" }
    }
  },
  {
    $project: {
      _id: 0,
      date: {
        $dateFromParts: {
          year: "$_id.year",
          month: "$_id.month",
          day: "$_id.day"
        }
      },
      totalRevenue: 1,
      orderCount: 1,
      avgOrderValue: { $round: ["$avgOrderValue", 2] }
    }
  },
  { $sort: { date: -1 } },
  { $out: "dailySalesSummary" }
])

// Now you can query the summary quickly
db.dailySalesSummary.find().limit(7)  // Last 7 days
```

### Example 3: Data Transformation
```javascript
// Transform user data into a simplified format
db.users.aggregate([
  {
    $project: {
      _id: 1,
      fullName: { $concat: ["$firstName", " ", "$lastName"] },
      email: { $toLower: "$email" },
      isActive: { $eq: ["$status", "active"] },
      registrationYear: { $year: "$createdAt" }
    }
  },
  { $out: "usersSimplified" }
])
```

## Advanced Usage

### Writing to Different Database
```javascript
// Write to collection in different database
db.sourceCollection.aggregate([
  { $match: { status: "completed" } },
  { $group: { _id: "$category", count: { $sum: 1 } } },
  { $out: { db: "analytics", coll: "categoryCounts" } }
])
```

### Complex Aggregation with $out
```javascript
// E-commerce: Product performance report
db.orderItems.aggregate([
  {
    $lookup: {
      from: "products",
      localField: "productId",
      foreignField: "_id",
      as: "product"
    }
  },
  { $unwind: "$product" },
  {
    $group: {
      _id: "$productId",
      productName: { $first: "$product.name" },
      category: { $first: "$product.category" },
      totalSold: { $sum: "$quantity" },
      totalRevenue: { $sum: { $multiply: ["$price", "$quantity"] } },
      averagePrice: { $avg: "$price" },
      orderCount: { $sum: 1 }
    }
  },
  {
    $project: {
      _id: 0,
      productId: "$_id",
      productName: 1,
      category: 1,
      totalSold: 1,
      totalRevenue: { $round: ["$totalRevenue", 2] },
      averagePrice: { $round: ["$averagePrice", 2] },
      orderCount: 1,
      revenuePerOrder: { 
        $round: [{ $divide: ["$totalRevenue", "$orderCount"] }, 2] 
      }
    }
  },
  { $sort: { totalRevenue: -1 } },
  { $out: "productPerformance" }
])

// Query the results
db.productPerformance.find({ category: "Electronics" })
  .sort({ totalRevenue: -1 })
  .limit(10)
```

## Practical Use Cases

### Use Case 1: ETL - Nightly Data Processing
```javascript
// Process logs and create daily summary
db.applicationLogs.aggregate([
  {
    $match: {
      timestamp: {
        $gte: new Date("2026-01-31T00:00:00Z"),
        $lt: new Date("2026-02-01T00:00:00Z")
      }
    }
  },
  {
    $group: {
      _id: {
        level: "$level",
        service: "$service"
      },
      count: { $sum: 1 },
      uniqueUsers: { $addToSet: "$userId" },
      errors: {
        $push: {
          $cond: [
            { $eq: ["$level", "error"] },
            { message: "$message", timestamp: "$timestamp" },
            "$$REMOVE"
          ]
        }
      }
    }
  },
  {
    $project: {
      _id: 0,
      level: "$_id.level",
      service: "$_id.service",
      count: 1,
      uniqueUserCount: { $size: "$uniqueUsers" },
      topErrors: { $slice: ["$errors", 10] }
    }
  },
  { $out: "dailyLogSummary_2026_01_31" }
])
```

### Use Case 2: Customer Segmentation
```javascript
// Segment customers based on behavior
db.customers.aggregate([
  {
    $lookup: {
      from: "orders",
      localField: "_id",
      foreignField: "customerId",
      as: "orders"
    }
  },
  {
    $project: {
      _id: 1,
      email: 1,
      name: 1,
      orderCount: { $size: "$orders" },
      totalSpent: {
        $sum: {
          $map: {
            input: "$orders",
            as: "order",
            in: "$$order.total"
          }
        }
      },
      lastOrderDate: { $max: "$orders.date" }
    }
  },
  {
    $addFields: {
      segment: {
        $switch: {
          branches: [
            { 
              case: { $gte: ["$totalSpent", 10000] }, 
              then: "VIP" 
            },
            { 
              case: { $and: [
                { $gte: ["$totalSpent", 1000] },
                { $lt: ["$totalSpent", 10000] }
              ]}, 
              then: "Regular" 
            },
            { 
              case: { $lt: ["$totalSpent", 1000] }, 
              then: "Occasional" 
            }
          ],
          default: "New"
        }
      },
      daysSinceLastOrder: {
        $divide: [
          { $subtract: [new Date(), "$lastOrderDate"] },
          86400000  // milliseconds in a day
        ]
      }
    }
  },
  { $out: "customerSegments" }
])

// Use the segmented data
db.customerSegments.find({ segment: "VIP" })
```

### Use Case 3: Data Archiving
```javascript
// Archive old completed orders
db.orders.aggregate([
  {
    $match: {
      status: "completed",
      completedDate: { $lt: new Date("2025-01-01") }
    }
  },
  {
    $lookup: {
      from: "orderItems",
      localField: "_id",
      foreignField: "orderId",
      as: "items"
    }
  },
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "customer"
    }
  },
  { $unwind: "$customer" },
  {
    $project: {
      orderId: "$_id",
      orderDate: "$createdDate",
      completedDate: 1,
      customerEmail: "$customer.email",
      customerName: "$customer.name",
      items: 1,
      total: 1,
      status: 1
    }
  },
  { $out: "ordersArchive2024" }
])
```

### Use Case 4: Real-Time Analytics Snapshot
```javascript
// Create hourly snapshot of active sessions
db.sessions.aggregate([
  {
    $match: {
      status: "active",
      lastActivity: { $gte: new Date(Date.now() - 3600000) }  // Last hour
    }
  },
  {
    $group: {
      _id: {
        country: "$country",
        device: "$device"
      },
      activeUsers: { $sum: 1 },
      avgSessionDuration: { $avg: "$duration" },
      pages: { $sum: "$pageViews" }
    }
  },
  {
    $project: {
      _id: 0,
      country: "$_id.country",
      device: "$_id.device",
      activeUsers: 1,
      avgSessionDuration: { $round: ["$avgSessionDuration", 0] },
      totalPages: "$pages",
      timestamp: new Date()
    }
  },
  { $out: "activeSessionsSnapshot" }
])
```

## Important Behaviors

### 1. Collection Replacement
```javascript
// Initial state
db.targetCollection.insertMany([
  { name: "Doc1", value: 100 },
  { name: "Doc2", value: 200 }
])

db.targetCollection.find()
// { name: "Doc1", value: 100 }
// { name: "Doc2", value: 200 }

// Run aggregation with $out
db.sourceCollection.aggregate([
  { $match: { type: "new" } },
  { $out: "targetCollection" }
])

// targetCollection now ONLY contains results from aggregation
// Previous documents are completely replaced!
```

### 2. Atomic Operation
```javascript
// $out is atomic - either all documents are written or none
// If pipeline fails, target collection remains unchanged

db.source.aggregate([
  { $group: { _id: "$category", count: { $sum: 1 } } },
  { $out: "target" }
])

// If aggregation fails at any stage, "target" is not modified
```

### 3. Index Preservation
```javascript
// Indexes on target collection are preserved
db.targetCollection.createIndex({ category: 1 })
db.targetCollection.createIndex({ date: -1 })

// After $out, indexes still exist
db.sourceCollection.aggregate([
  { $match: { status: "active" } },
  { $out: "targetCollection" }
])

db.targetCollection.getIndexes()  // Indexes still present
```

### 4. Creating New Collections
```javascript
// If collection doesn't exist, $out creates it
db.sourceCollection.aggregate([
  { $group: { _id: "$type", count: { $sum: 1 } } },
  { $out: "newCollection" }  // Creates "newCollection" if it doesn't exist
])
```

## Limitations and Restrictions

### 1. Must Be Last Stage
```javascript
// ❌ INVALID - $out must be last
db.collection.aggregate([
  { $group: { _id: "$category", count: { $sum: 1 } } },
  { $out: "summary" },
  { $sort: { count: -1 } }  // Error! Can't have stages after $out
])

// ✅ VALID - $out is last
db.collection.aggregate([
  { $group: { _id: "$category", count: { $sum: 1 } } },
  { $sort: { count: -1 } },
  { $out: "summary" }
])
```

### 2. Cannot Write to Capped Collections
```javascript
// Create capped collection
db.createCollection("cappedLogs", { capped: true, size: 100000 })

// ❌ INVALID - Cannot use $out with capped collections
db.source.aggregate([
  { $match: { level: "error" } },
  { $out: "cappedLogs" }  // Error!
])
```

### 3. Cannot Write to System Collections
```javascript
// ❌ INVALID - Cannot write to system collections
db.source.aggregate([
  { $match: {} },
  { $out: "system.profile" }  // Error!
])
```

### 4. Sharded Collections (Special Considerations)
```javascript
// When writing to sharded collection:
// - Must include shard key in output documents
// - Output collection must be sharded on same key

// If orders is sharded on { customerId: 1 }
db.sales.aggregate([
  {
    $group: {
      _id: "$customerId",  // Must include shard key
      total: { $sum: "$amount" }
    }
  },
  { $out: "customerTotals" }
])
```

## $out vs $merge

### Key Differences

| Feature | $out | $merge |
|---------|------|--------|
| **Replaces Collection** | Yes - complete replacement | No - can update/insert |
| **Must Be Last Stage** | Yes | Yes |
| **Update Existing Docs** | No | Yes |
| **Insert Only** | Yes | Optional |
| **Custom Update Logic** | No | Yes |
| **Version** | Available since 2.6 | Available since 4.2 |

### When to Use $out
```javascript
// Use $out when:
// ✅ You want to completely replace collection contents
// ✅ Creating snapshot/materialized views
// ✅ Simple ETL operations
// ✅ Working with MongoDB < 4.2

db.orders.aggregate([
  { $match: { date: { $gte: new Date("2026-01-01") } } },
  { $group: { _id: "$category", total: { $sum: "$amount" } } },
  { $out: "monthlySummary" }  // Replace entire collection
])
```

### When to Use $merge (Instead of $out)
```javascript
// Use $merge when:
// ✅ You want to update existing documents
// ✅ You need to preserve some existing data
// ✅ You want incremental updates
// ✅ You need custom merge logic

db.orders.aggregate([
  { $match: { date: { $gte: new Date("2026-01-31") } } },
  { $group: { _id: "$category", dailyTotal: { $sum: "$amount" } } },
  { 
    $merge: {
      into: "categorySummary",
      on: "_id",
      whenMatched: "merge",  // Update existing
      whenNotMatched: "insert"  // Insert new
    }
  }
])
```

## Best Practices

### 1. Test with Small Dataset First
```javascript
// ❌ BAD - Testing with full production data
db.hugeCollection.aggregate([
  // ... complex pipeline ...
  { $out: "results" }
])

// ✅ GOOD - Test with limit first
db.hugeCollection.aggregate([
  { $limit: 1000 },  // Test with small sample
  // ... complex pipeline ...
  { $out: "resultsTest" }
])

// After verifying, run on full dataset
```

### 2. Backup Target Collection
```javascript
// Before running $out on important collection
// Create backup
db.importantCollection.aggregate([
  { $match: {} },
  { $out: "importantCollection_backup_20260131" }
])

// Then run your aggregation
db.source.aggregate([
  // ... pipeline ...
  { $out: "importantCollection" }
])
```

### 3. Use Descriptive Collection Names
```javascript
// ❌ BAD - Unclear names
{ $out: "temp" }
{ $out: "data2" }

// ✅ GOOD - Descriptive names with context
{ $out: "customerSummary_2026_01" }
{ $out: "productPerformance_daily" }
{ $out: "userSegments_v2" }
```

### 4. Schedule Regular Updates
```javascript
// Create a scheduled job (pseudo-code)
// Run daily at 2 AM

function updateDailySummary() {
  const yesterday = new Date()
  yesterday.setDate(yesterday.getDate() - 1)
  yesterday.setHours(0, 0, 0, 0)
  
  const today = new Date()
  today.setHours(0, 0, 0, 0)
  
  db.transactions.aggregate([
    {
      $match: {
        date: { $gte: yesterday, $lt: today }
      }
    },
    {
      $group: {
        _id: {
          category: "$category",
          status: "$status"
        },
        count: { $sum: 1 },
        total: { $sum: "$amount" }
      }
    },
    { $out: `dailySummary_${yesterday.toISOString().split('T')[0]}` }
  ])
}
```

### 5. Monitor Performance
```javascript
// Monitor aggregation performance
const startTime = new Date()

db.source.aggregate([
  { $match: { status: "completed" } },
  { $group: { _id: "$category", count: { $sum: 1 } } },
  { $out: "summary" }
])

const endTime = new Date()
console.log(`Aggregation took: ${endTime - startTime}ms`)

// Log to monitoring collection
db.aggregationLogs.insertOne({
  pipeline: "customer_summary",
  startTime: startTime,
  endTime: endTime,
  duration: endTime - startTime,
  status: "completed"
})
```

### 6. Handle Errors Gracefully
```javascript
// Wrap in try-catch
try {
  db.source.aggregate([
    { $group: { _id: "$category", count: { $sum: 1 } } },
    { $out: "summary" }
  ])
  
  console.log("Summary created successfully")
  
} catch (error) {
  console.error("Aggregation failed:", error.message)
  
  // Log error
  db.errors.insertOne({
    operation: "$out aggregation",
    collection: "summary",
    error: error.message,
    timestamp: new Date()
  })
}
```

## Performance Considerations

### 1. Index Source Collection
```javascript
// Create indexes on fields used in $match
db.orders.createIndex({ status: 1, date: -1 })

// Then run aggregation
db.orders.aggregate([
  { $match: { status: "completed", date: { $gte: new Date("2026-01-01") } } },
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } },
  { $out: "customerTotals" }
])
```

### 2. Use $match Early
```javascript
// ❌ BAD - Filtering after processing
db.collection.aggregate([
  { $lookup: { /* ... */ } },
  { $unwind: "$data" },
  { $match: { status: "active" } },  // Late filter
  { $out: "results" }
])

// ✅ GOOD - Filter early to reduce data volume
db.collection.aggregate([
  { $match: { status: "active" } },  // Early filter
  { $lookup: { /* ... */ } },
  { $unwind: "$data" },
  { $out: "results" }
])
```

### 3. Consider allowDiskUse
```javascript
// For large datasets that might exceed memory
db.largeCollection.aggregate([
  { $group: { _id: "$field", data: { $push: "$$ROOT" } } },
  { $out: "results" }
], { allowDiskUse: true })  // Allow using disk for large operations
```

## Real-World Complete Example

```javascript
// E-commerce: Create comprehensive product analytics

// Step 1: Gather and transform data
db.orderItems.aggregate([
  // Join with products
  {
    $lookup: {
      from: "products",
      localField: "productId",
      foreignField: "_id",
      as: "productInfo"
    }
  },
  { $unwind: "$productInfo" },
  
  // Join with orders for date info
  {
    $lookup: {
      from: "orders",
      localField: "orderId",
      foreignField: "_id",
      as: "orderInfo"
    }
  },
  { $unwind: "$orderInfo" },
  
  // Filter recent data (last 90 days)
  {
    $match: {
      "orderInfo.date": { $gte: new Date(Date.now() - 90*24*60*60*1000) }
    }
  },
  
  // Group by product
  {
    $group: {
      _id: "$productId",
      productName: { $first: "$productInfo.name" },
      category: { $first: "$productInfo.category" },
      brand: { $first: "$productInfo.brand" },
      
      // Sales metrics
      totalUnits: { $sum: "$quantity" },
      totalRevenue: { $sum: { $multiply: ["$price", "$quantity"] } },
      orderCount: { $sum: 1 },
      
      // Price analytics
      avgPrice: { $avg: "$price" },
      minPrice: { $min: "$price" },
      maxPrice: { $max: "$price" },
      
      // Customer analytics
      uniqueCustomers: { $addToSet: "$orderInfo.customerId" },
      
      // Time analytics
      firstSale: { $min: "$orderInfo.date" },
      lastSale: { $max: "$orderInfo.date" }
    }
  },
  
  // Calculate derived metrics
  {
    $project: {
      _id: 0,
      productId: "$_id",
      productName: 1,
      category: 1,
      brand: 1,
      
      totalUnits: 1,
      totalRevenue: { $round: ["$totalRevenue", 2] },
      orderCount: 1,
      
      avgPrice: { $round: ["$avgPrice", 2] },
      minPrice: 1,
      maxPrice: 1,
      priceRange: { $round: [{ $subtract: ["$maxPrice", "$minPrice"] }, 2] },
      
      uniqueCustomerCount: { $size: "$uniqueCustomers" },
      revenuePerCustomer: { 
        $round: [{ $divide: ["$totalRevenue", { $size: "$uniqueCustomers" }] }, 2] 
      },
      
      firstSale: 1,
      lastSale: 1,
      daysSinceLastSale: {
        $round: [{
          $divide: [
            { $subtract: [new Date(), "$lastSale"] },
            86400000
          ]
        }, 0]
      },
      
      generatedAt: new Date()
    }
  },
  
  // Sort by revenue
  { $sort: { totalRevenue: -1 } },
  
  // Write to analytics collection
  { $out: "productAnalytics90Days" }
], { allowDiskUse: true })

// Step 2: Create indexes on output collection for fast queries
db.productAnalytics90Days.createIndex({ category: 1, totalRevenue: -1 })
db.productAnalytics90Days.createIndex({ brand: 1 })
db.productAnalytics90Days.createIndex({ totalRevenue: -1 })

// Step 3: Query the results
// Top products by category
db.productAnalytics90Days.find({ category: "Electronics" })
  .sort({ totalRevenue: -1 })
  .limit(10)

// Products that haven't sold recently
db.productAnalytics90Days.find({ daysSinceLastSale: { $gt: 30 } })
  .sort({ daysSinceLastSale: -1 })
```

## Summary

### Key Points:
- `$out` writes aggregation results to a collection
- Must be the last stage in the pipeline
- **Replaces** the entire target collection
- Creates collection if it doesn't exist
- Preserves indexes on target collection
- Atomic operation - all or nothing

### Use $out For:
✅ Complete collection replacement  
✅ Materialized views  
✅ ETL operations  
✅ Data archiving  
✅ Report generation  
✅ Pre-computed analytics  

### Avoid $out When:
❌ You need incremental updates (use `$merge` instead)  
❌ Writing to capped collections  
❌ Writing to system collections  
❌ Need to preserve existing data  

### Best Practices:
1. Test with small datasets first
2. Backup important collections before using $out
3. Use descriptive collection names
4. Monitor performance and errors
5. Consider using $merge for incremental updates
6. Index source collections for better performance
7. Use allowDiskUse for large datasets

## Next Steps
- Learn about `$merge` for more flexible output options
- Explore aggregation performance optimization
- Study materialized views and caching strategies
- Understand incremental data processing patterns
