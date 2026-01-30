## Assign a Data Type in a Search Index
To set a field’s data type, use the type option followed by the data type supported by Atlas Search. For example, here the type is set to string:
```js
db.collection.createSearchIndex(
    "indexName",
     {
        "mappings": {
          "dynamic": false,
           "fields": {
              "fieldName": {
                 "type": "string"
              }
           }
        }
     }
  )
```

To index an array of subdocuments, use the embeddedDocuments data type. When using the embeddedDocuments field type, we can either dynamically map so that all of the supported data type fields are indexed, or we can statically map individual fields. For example:
```js
{
  "mappings": {
    "dynamic": false,
    "fields": {
      "": {
        "type": "embeddedDocuments",
        "dynamic": true|false,
        "fields": {
          "": {
            
          }
        }
      }
    }
  }
}
```

## Assign Multiple Data Types
We can also assign a field multiple data types. In the following example, the directors field is assigned both the string and objectId data types.
```js
db.movies.createSearchIndex(
    "directorsIndex",
     {
        "mappings": {
          "dynamic": false,
           "fields": {
              "directors": [
                {
                 "type": "string"
              },
              {
                  "type": "objectId"
              }
            ]
           }
        }
     }
  )
```