Use the text Operator
The text operator performs a full-text search of data in our search index. In the following example, plotReleasedIndex is used with the text operator to search for documents that contain the word “nature” in the plot field.

db.movies.aggregate([
    {
      "$search": {
        "index": "plotReleasedIndex",
        "text": {
          "query": "nature",
          "path": "plot"
        }
      }
    },
   { "$project": {"_id": 0, "title": 1, "plot": 1 }}
  ])
Use the equals Operator
The equals operator returns documents with a field that matches a specified value. In the following example, plotReleasedIndex is used with the equals operator to search for movies that were released on March 31st, 1999.

db.movies.aggregate([
   {
      "$search": {
         "index": "plotReleasedIndex",
         "equals": {
            "path": "released",
            "value": ISODate("1999-03-31T00:00:00.000Z")
         }
      }
   },
   { "$project": {"_id": 0, "title": 1, "released": 1 }}
])