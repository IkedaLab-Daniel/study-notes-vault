# Introduction to MongoDB Aggregation

This section contains key definitions for this lesson, as well as the code for an aggregation pipeline.

## Definitions

### Aggregation
Collection and summary of data. The aggregation framework allows you to perform complex data processing operations on your MongoDB collections, similar to SQL's GROUP BY, JOIN, and other analytical operations.

### Stage
One of the built-in methods that can be completed on the data, but does not permanently alter it. Each stage transforms the documents as they pass through the pipeline. Common stages include:
- `$match` - Filter documents
- `$group` - Group documents by a specified field
- `$sort` - Sort documents
- `$project` - Reshape documents by adding or removing fields
- `$limit` - Limit the number of documents
- `$skip` - Skip a specified number of documents
- `$lookup` - Perform a left outer join with another collection
- `$unwind` - Deconstruct an array field

### Aggregation Pipeline
A series of stages completed on the data in order. Documents pass through the stages in sequence, with the output of one stage serving as the input to the next stage. This allows for powerful data transformations and analysis.

## Structure of an Aggregation Pipeline

```javascript
db.collection.aggregate([
  {
    $stage1: {
      { expression1 },
      { expression2 }
    }
  },
  {
    $stage2: {
      { expression1 }
    }
  }
])
```

## Basic Example

Here's a simple example that filters and groups data:

```javascript
db.sales.aggregate([
  {
    $match: {
      status: "completed"
    }
  },
  {
    $group: {
      _id: "$product",
      totalSales: { $sum: "$amount" },
      count: { $sum: 1 }
    }
  },
  {
    $sort: {
      totalSales: -1
    }
  }
])
```

This pipeline:
1. **Filters** documents where status is "completed"
2. **Groups** by product and calculates total sales and count
3. **Sorts** results by total sales in descending order

## Key Points

- Aggregation pipelines are processed in order from top to bottom
- Each stage receives documents from the previous stage
- Operations are performed in memory (use indexes when possible)
- Results can be returned directly or stored in a new collection using `$out` or `$merge`
- Aggregation does not modify the original documents in the collection