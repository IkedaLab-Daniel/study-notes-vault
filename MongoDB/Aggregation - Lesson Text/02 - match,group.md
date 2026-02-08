# Using $match and $group Stages in a MongoDB Aggregation Pipeline
Review the following sections, which show the code for the $match and $group aggregation stages.

## $match
The $match stage filters for documents that match specified conditions. Here's the code for $match:
```js
{
  $match: {
     "field_name": "value"
  }
}
```

## $group
The $group stage groups documents by a group key.
```js
{
  $group:
    {
      _id: <expression>, // Group key
      <field>: { <accumulator> : <expression> }
    }
 }
```
$match and $group in an Aggregation Pipeline
The following aggregation pipeline finds the documents with a field named "state" that matches a value "CA" and then groups those documents by the group key "$city" and shows the total number of zip codes in the state of California.
```js
db.zips.aggregate([
{   
   $match: { 
      state: "CA"
    }
},
{
   $group: {
      _id: "$city",
      totalZips: { $count : { } }
   }
}
])
```