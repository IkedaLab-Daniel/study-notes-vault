# Using $match and $group Stages in a MongoDB Aggregation Pipeline

Review the following sections, which show the code for the `$match` and `$group` aggregation stages.

## $match

The `$match` stage filters for documents that match specified conditions. Here's the code for `$match`:

```javascript
{
  $match: {
    "field_name": "value"
  }
}
```

### Key Points
- Similar to the `find()` query
- Should be placed early in the pipeline to reduce the number of documents
- Can use any MongoDB query operators (`$gt`, `$lt`, `$in`, etc.)
- Improves performance by filtering before other operations

## $group

The `$group` stage groups documents by a group key.

```javascript
{
  $group: {
    _id: <expression>, // Group key
    <field>: { <accumulator> : <expression> }
  }
}
```

### Common Accumulators
- `$sum` - Calculates the sum of numeric values
- `$avg` - Calculates the average of numeric values
- `$min` - Returns the minimum value
- `$max` - Returns the maximum value
- `$count` - Counts the number of documents
- `$push` - Returns an array of all values
- `$first` - Returns the first value
- `$last` - Returns the last value

## $match and $group in an Aggregation Pipeline

The following aggregation pipeline finds the documents with a field named `state` that matches a value `"CA"` and then groups those documents by the group key `"$city"` and shows the total number of zip codes in the state of California.

```javascript
db.zips.aggregate([
  {   
    $match: { 
      state: "CA"
    }
  },
  {
    $group: {
      _id: "$city",
      totalZips: { $count: {} }
    }
  }
])
```

### Pipeline Explanation
1. **$match stage**: Filters documents to only include those where `state` equals `"CA"`
2. **$group stage**: Groups the filtered documents by `city` and counts the total number of zip codes per city

### Example Output
```javascript
[
  { _id: "LOS ANGELES", totalZips: 123 },
  { _id: "SAN FRANCISCO", totalZips: 45 },
  { _id: "SAN DIEGO", totalZips: 67 },
  // ... more cities
]
```