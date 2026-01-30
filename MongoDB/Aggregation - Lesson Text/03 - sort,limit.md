# Using $sort and $limit Stages in a MongoDB Aggregation Pipeline
Review the following sections, which show the code for the $sort and $limit aggregation stages.

## $sort
The $sort stage sorts all input documents and returns them to the pipeline in sorted order. We use 1 to represent ascending order, and -1 to represent descending order.
```js
{
    $sort: {
        "field_name": 1
    }
}
```

## $limit
The $limit stage returns only a specified number of records.
```js
{
  $limit: 5
}
```

## $sort and $limit in an Aggregation Pipeline
The following aggregation pipeline sorts the documents in descending order, so the documents with the greatest pop value appear first, and limits the output to only the first five documents after sorting.
```js
db.zips.aggregate([
{
  $sort: {
    pop: -1
  }
},
{
  $limit:  5
}
])
```