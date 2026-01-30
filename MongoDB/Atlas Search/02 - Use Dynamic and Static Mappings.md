# Use Dynamic and Static Mappings
To use dynamic mapping in a search index, we use the mappings field in the index definition and set the dynamic option to true. Here’s an example:
```js
db.movies.createSearchIndex(
   { "mappings": { "dynamic": true } }
)
```

To use static mapping, set the dynamic option to false.

Here’s an example where both types are used in a single search index:
```js
db.movies.createSearchIndex(
    "plotReleasedIndex",
     {
        "mappings": {
          "dynamic": false,
           "fields": {
              "plot": {
                 "type": "string"
              },
              "released": {
                 "type": "embeddedDocument",
                 "dynamic": true
              }
           }
        }
     }
  )
```