# Using $out Stage in a MongoDB Aggregation Pipeline

The `$out` stage writes the results of an aggregation pipeline to a specified collection.

## $out

The `$out` stage takes the documents returned by the aggregation pipeline and writes them to a specified collection. This stage must be the last stage in the pipeline.

```javascript
{
  $out: "collection_name"
}
```

### Key Points
- **Must be the last stage** in the aggregation pipeline
- Writes results to a new or existing collection
- If the collection exists, `$out` **replaces it completely**
- Creates the collection if it doesn't exist
- The operation is atomic (all or nothing)
- Cannot write to capped collections
- Cannot be used with `$merge` in the same pipeline
- Useful for materialized views or creating summary collections

### Important Warning
⚠️ **`$out` will replace the entire target collection if it already exists!** All existing data in that collection will be lost. Use with caution in production environments.

## Basic Syntax

```javascript
db.collection.aggregate([
  { $stage1: {...} },
  { $stage2: {...} },
  { $out: "new_collection_name" }
])
```

## Simple Example

Create a new collection with only California zip codes:

```javascript
db.zips.aggregate([
  {
    $match: {
      state: "CA"
    }
  },
  {
    $out: "california_zips"
  }
])
```

### Result
- Creates a new collection called `california_zips`
- Contains only documents where `state` is "CA"
- Original `zips` collection remains unchanged

## Example: Creating a Summary Collection

Aggregate sales data and store the results in a summary collection:

```javascript
db.sales.aggregate([
  {
    $match: {
      date: { $gte: ISODate("2025-01-01") }
    }
  },
  {
    $group: {
      _id: "$product",
      totalSales: { $sum: "$amount" },
      averagePrice: { $avg: "$price" },
      count: { $sum: 1 }
    }
  },
  {
    $sort: {
      totalSales: -1
    }
  },
  {
    $out: "product_sales_summary"
  }
])
```

### Pipeline Explanation
1. **$match**: Filters sales from 2025 onwards
2. **$group**: Groups by product and calculates totals
3. **$sort**: Sorts by total sales in descending order
4. **$out**: Writes results to `product_sales_summary` collection

## Example: Creating Computed Fields

Transform data and store in a new collection:

```javascript
db.customers.aggregate([
  {
    $match: {
      active: true
    }
  },
  {
    $set: {
      fullName: {
        $concat: ["$firstName", " ", "$lastName"]
      },
      membershipYears: {
        $divide: [
          { $subtract: [new Date(), "$joinDate"] },
          1000 * 60 * 60 * 24 * 365
        ]
      }
    }
  },
  {
    $project: {
      fullName: 1,
      email: 1,
      membershipYears: 1,
      totalPurchases: 1,
      _id: 1
    }
  },
  {
    $out: "active_customers_summary"
  }
])
```

## Example: Combining Multiple Collections

Create a denormalized collection for faster queries:

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "customerInfo"
    }
  },
  {
    $unwind: "$customerInfo"
  },
  {
    $project: {
      orderId: "$_id",
      orderDate: 1,
      amount: 1,
      customerName: "$customerInfo.name",
      customerEmail: "$customerInfo.email",
      _id: 0
    }
  },
  {
    $out: "orders_with_customer_info"
  }
])
```

## Using $out with Same Database

By default, `$out` writes to the same database:

```javascript
db.zips.aggregate([
  {
    $match: { state: "NY" }
  },
  {
    $out: "ny_zips"
  }
])
// Creates 'ny_zips' in the current database
```

## Using $out with Different Database

You can specify a different database using an object:

```javascript
db.zips.aggregate([
  {
    $match: { state: "TX" }
  },
  {
    $out: {
      db: "archive",
      coll: "texas_zips"
    }
  }
])
```

## Best Practices

### 1. Test Before Production
Always test your aggregation pipeline on a subset of data before using `$out` in production.

```javascript
// Test without $out first
db.collection.aggregate([
  { $match: {...} },
  { $group: {...} },
  { $limit: 10 }  // Test with limited results
])

// Then add $out when confident
```

### 2. Use Meaningful Collection Names
Name output collections descriptively:

```javascript
// Good names
{ $out: "monthly_sales_summary_2025" }
{ $out: "active_customers_snapshot" }
{ $out: "product_inventory_report" }

// Avoid vague names
{ $out: "temp" }
{ $out: "data" }
```

### 3. Consider Using $merge Instead
If you need to update rather than replace, consider `$merge`:

```javascript
// $out replaces entire collection
{ $out: "summary" }

// $merge can update/insert documents
{ $merge: { into: "summary", whenMatched: "replace" } }
```

### 4. Backup Important Collections
Before using `$out` on an existing collection, create a backup:

```javascript
// Backup first
db.important_data.aggregate([
  { $out: "important_data_backup" }
])

// Then perform your operation
db.source.aggregate([
  // ... your pipeline
  { $out: "important_data" }
])
```

## Common Use Cases

### 1. Daily/Monthly Reports
```javascript
// Create daily sales summary
db.transactions.aggregate([
  {
    $match: {
      date: { $gte: ISODate("2025-11-12T00:00:00Z") }
    }
  },
  {
    $group: {
      _id: "$category",
      totalRevenue: { $sum: "$amount" },
      transactions: { $sum: 1 }
    }
  },
  {
    $out: "daily_sales_2025_11_12"
  }
])
```

### 2. Data Archival
```javascript
// Archive old records
db.logs.aggregate([
  {
    $match: {
      timestamp: { $lt: ISODate("2024-01-01") }
    }
  },
  {
    $out: "logs_archive_2023"
  }
])
```

### 3. Creating Materialized Views
```javascript
// Pre-compute expensive aggregations
db.events.aggregate([
  {
    $group: {
      _id: {
        user: "$userId",
        month: { $month: "$date" }
      },
      eventCount: { $sum: 1 },
      lastEvent: { $max: "$date" }
    }
  },
  {
    $out: "user_monthly_activity"
  }
])
```

## Performance Considerations

- `$out` is a blocking operation - it waits until all documents are written
- For large datasets, this can take considerable time
- The operation holds a write lock on the target collection
- Consider running during off-peak hours for production systems
- Index the output collection after creation if needed

## Error Handling

If `$out` fails (e.g., due to disk space), the entire operation is rolled back:

```javascript
try {
  db.large_collection.aggregate([
    // ... complex pipeline
    { $out: "summary" }
  ])
  print("Pipeline completed successfully")
} catch (error) {
  print("Pipeline failed: " + error)
  // Original collections remain unchanged
}
```

## Summary

- **Purpose**: Write aggregation results to a collection
- **Position**: Must be the last stage
- **Behavior**: Replaces target collection if it exists
- **Use Cases**: Reports, summaries, materialized views, data archival
- **Caution**: Destructive operation - backs up important data first
- **Alternative**: Consider `$merge` for non-destructive updates
