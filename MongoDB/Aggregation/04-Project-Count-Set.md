# Using $project, $count, and $set Stages in a MongoDB Aggregation Pipeline

Review the following sections, which show the code for the `$project`, `$set`, and `$count` aggregation stages.

## $project

The `$project` stage specifies the fields of the output documents. `1` means that the field should be included, and `0` means that the field should be suppressed. The field can also be assigned a new value.

```javascript
{
  $project: {
    state: 1, 
    zip: 1,
    population: "$pop",
    _id: 0
  }
}
```

### Key Points
- `1` = Include the field in output
- `0` = Exclude the field from output
- Can rename fields by assigning them to a new name
- Can create computed fields using expressions
- `_id` is included by default unless explicitly excluded with `_id: 0`
- Reduces document size by selecting only needed fields

### Common Use Cases
- Reshaping documents for cleaner output
- Renaming fields for consistency
- Creating calculated fields
- Removing sensitive data from results

### Example with Computed Fields

```javascript
{
  $project: {
    city: 1,
    state: 1,
    populationInThousands: { $divide: ["$pop", 1000] },
    isLargeCity: { $gte: ["$pop", 50000] },
    _id: 0
  }
}
```

## $set

The `$set` stage creates new fields or changes the value of existing fields, and then outputs the documents with the new fields.

```javascript
{
  $set: {
    place: {
      $concat: ["$city", ",", "$state"]
    },
    pop: 10000
  }
}
```

### Key Points
- Adds new fields to documents without removing existing ones
- Can modify existing field values
- More concise than `$project` when you want to keep all fields
- Use `$set` when adding/modifying a few fields
- Use `$project` when you need to reshape the entire document

### $set vs $project
- **$set**: Keeps all existing fields and adds/modifies specified fields
- **$project**: Only includes fields explicitly specified (unless using `field: 1`)

### Example: Adding Multiple Computed Fields

```javascript
{
  $set: {
    fullAddress: {
      $concat: ["$city", ", ", "$state", " ", "$zip"]
    },
    lastUpdated: new Date(),
    populationCategory: {
      $cond: {
        if: { $gte: ["$pop", 100000] },
        then: "Large",
        else: "Small"
      }
    }
  }
}
```

## $count

The `$count` stage creates a new document, with the number of documents at that stage in the aggregation pipeline assigned to the specified field name.

```javascript
{
  $count: "total_zips"
}
```

### Key Points
- Returns a single document with the count
- The output document has only one field (the count field)
- Useful for getting statistics about filtered data
- Often used as the final stage in a pipeline
- More efficient than using `$group` with `$sum: 1` when you only need the count

### Example Output

```javascript
// Input: 100 documents
// Output after $count:
{ total_zips: 100 }
```

### Example Pipeline with $count

```javascript
db.zips.aggregate([
  {
    $match: {
      state: "NY",
      pop: { $gte: 50000 }
    }
  },
  {
    $count: "large_cities_in_ny"
  }
])

// Output:
// { large_cities_in_ny: 25 }
```

## Complete Example: Combining All Three Stages

```javascript
db.zips.aggregate([
  // Filter for California zip codes
  {
    $match: {
      state: "CA"
    }
  },
  // Add a computed field
  {
    $set: {
      cityState: {
        $concat: ["$city", ", ", "$state"]
      },
      sizeCategory: {
        $cond: {
          if: { $gte: ["$pop", 50000] },
          then: "Large",
          else: "Small"
        }
      }
    }
  },
  // Reshape the output
  {
    $project: {
      cityState: 1,
      population: "$pop",
      sizeCategory: 1,
      _id: 0
    }
  },
  // Limit to first 5 results
  {
    $limit: 5
  }
])
```

### Pipeline Explanation
1. **$match**: Filters documents for California only
2. **$set**: Adds `cityState` (formatted string) and `sizeCategory` (computed field)
3. **$project**: Reshapes output to show only specific fields with renamed `population`
4. **$limit**: Returns only the first 5 documents