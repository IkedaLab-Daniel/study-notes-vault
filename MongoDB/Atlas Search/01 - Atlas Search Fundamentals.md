# Code Summary: Atlas Search Fundamentals

## Create a Search Index
To create a search index in Atlas Search, use createSearchIndex(). In this example, we use the createSearchIndex() method inside the MongoDB Shell to index the plot field, which is a string.
```js
db.movies.createSearchIndex(
  "plotIndex",
   {
      "mappings": {
         "fields": {
            "plot": {
               "type": "string"
            }
         }
      }
   }
)
```

## Run a Search Query
To run a search query in Atlas, use the $search or $searchMeta stage in a MongoDB aggregation pipeline. Here we use the $search stage with the index that we created on the plot field.
```js
db.movies.aggregate([
    {
      "$search": {
        "index": "plotIndex",
        "text": {
          "query": "space",
          "path": "plot"
        }
      }
    }
  ])
```

## Customize Results
To make search results easier to read, we can add a $limit stage and a $project stage. In the $project stage we can also add the $meta aggregation operator to let us see how results were scored. Here’s an example:
```js
db.movies.aggregate([
  {
    "$search": {
      "index": "plotIndex",
      "text": {
        "query": "space",
        "path": "plot",
      },
    },
  },
  { "$limit": 3 },
  {
    "$project": {
      "_id": 0,
      "title": 1,
      "plot": 1,
      "score": { "$meta": "searchScore" },
    },
  },
]);
```

## Return Summary of Results
To return a summary of your search results, use the $searchMeta stage at the beginning of your aggregation pipeline and add the count field.
```js
db.movies.aggregate([
    {
      "$searchMeta": {
        "index": "plotIndex",
        "text": {
          "query": "space",
          "path": "plot"
        },
        "count": {
          "type": "total"
        }
      }
    }
  ])
```