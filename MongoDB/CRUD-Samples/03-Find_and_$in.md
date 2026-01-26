## Finding Documents in a MongoDB Collection
Review the following code, which demonstrates how to query documents in MongoDB.

## Find a Document with Equality
When given equality with an _id field, the find() command will return the specified document that matches the _id. Here's an example:

```sh
db.zips.find({ _id: ObjectId("5c8eccc1caa187d17ca6ed16") })
```

## Find a Document by Using the $in Operator
Use the $in operator to select documents where the value of a field equals any value in the specified array. Here's an example:
```sh
db.zips.find({ city: { $in: ["PHOENIX", "CHICAGO"] } })
```