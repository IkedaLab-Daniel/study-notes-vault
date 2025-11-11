# Using $sort and $limit Stages in a MongoDB Aggregation Pipeline

Review the following sections, which show the code for the `$sort` and `$limit` aggregation stages.

## $sort

The `$sort` stage sorts all input documents and returns them to the pipeline in sorted order. We use `1` to represent ascending order, and `-1` to represent descending order.

```javascript
{
  $sort: {
    "field_name": 1
  }
}
```

### Key Points
- `1` = Ascending order (A-Z, 0-9, oldest to newest)
- `-1` = Descending order (Z-A, 9-0, newest to oldest)
- Can sort by multiple fields
- Sorts are performed in memory (consider indexing for large datasets)
- The order of fields matters when sorting by multiple fields

### Sort by Multiple Fields Example

```javascript
{
  $sort: {
    state: 1,
    city: 1,
    pop: -1
  }
}
```

## $limit

The `$limit` stage returns only a specified number of records.

```javascript
{
  $limit: 5
}
```

### Key Points
- Limits the number of documents passed to the next stage
- Often used with `$sort` to get "top N" results
- Should be placed after `$sort` to get meaningful results
- Improves performance by reducing document processing

## $sort and $limit in an Aggregation Pipeline

The following aggregation pipeline sorts the documents in descending order, so the documents with the greatest `pop` value appear first, and limits the output to only the first five documents after sorting.

```javascript
db.zips.aggregate([
  {
    $sort: {
      pop: -1
    }
  },
  {
    $limit: 5
  }
])
```

### Pipeline Explanation
1. **$sort stage**: Sorts all documents by population (`pop`) in descending order (highest first)
2. **$limit stage**: Returns only the top 5 documents with the highest population

### Example Output
```javascript
[
  { _id: "60623", city: "CHICAGO", state: "IL", pop: 112047 },
  { _id: "11226", city: "BROOKLYN", state: "NY", pop: 111396 },
  { _id: "10021", city: "NEW YORK", state: "NY", pop: 106564 },
  { _id: "10025", city: "NEW YORK", state: "NY", pop: 100027 },
  { _id: "90201", city: "BELL GARDENS", state: "CA", pop: 99568 }
]
```

### Common Pattern: Top N Results

This pattern is frequently used to find:
- Top 10 customers by sales
- Most popular products
- Highest rated items
- Latest records (when sorting by date)

```javascript
// Get top 10 customers by total purchases
db.orders.aggregate([
  {
    $group: {
      _id: "$customerId",
      totalPurchases: { $sum: "$amount" }
    }
  },
  {
    $sort: { totalPurchases: -1 }
  },
  {
    $limit: 10
  }
])
```