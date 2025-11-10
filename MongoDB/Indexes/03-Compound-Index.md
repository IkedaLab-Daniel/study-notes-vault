# Working with Compound Indexes

Review the code below, which demonstrates how to create a compound index in a collection.

## Create a Compound Index

Use `createIndex()` to create a new index in a collection. Within the parentheses of `createIndex()`, include an object that contains two or more fields and their sort order.

```javascript
db.customers.createIndex({
  active:1, 
  birthdate:-1,
  name:1
})
```

## Order of Fields in a Compound Index

The order of the fields matters when creating the index and the sort order. It is recommended to list the fields in the following order: **Equality, Sort, and Range**.

- **Equality**: field/s that matches on a single field value in a query
- **Sort**: field/s that orders the results by in a query
- **Range**: field/s that the query filter in a range of valid values

The following query includes an equality match on the `active` field, a sort on `birthday` (descending) and `name` (ascending), and a range query on `birthday` too.

```javascript
db.customers.find({
  birthdate: {
    $gte:ISODate("1977-01-01")
  },
  active:true
}).sort({
  birthdate:-1, 
  name:1
})
```

Here's an example of an efficient index for this query:

```javascript
db.customers.createIndex({
  active:1, 
  birthdate:-1,
  name:1
})
```

## View the Indexes used in a Collection

Use `getIndexes()` to see all the indexes created in a collection.

```javascript
db.customers.getIndexes()
```

## Check if an Index is Being Used on a Query

Use `explain()` in a collection when running a query to see the Execution plan. This plan provides the details of the execution stages (IXSCAN, COLLSCAN, FETCH, SORT, etc.). Some of these are:

- **IXSCAN** stage indicates the query is using an index and what index is being selected.
- **COLLSCAN** stage indicates a collection scan is perform, not using any indexes.
- **FETCH** stage indicates documents are being read from the collection.
- **SORT** stage indicates documents are being sorted in memory.

```javascript
db.customers.explain().find({
  birthdate: {
    $gte:ISODate("1977-01-01")
  },
  active:true
}).sort({
  birthdate:-1,
  name:1
})
```

## Cover a Query by the Index

An Index covers a query when MongoDB does not need to fetch the data from memory since all the required data is already returned by the index.

In most cases, we can use projections to return only the required fields and cover the query. Make sure those fields in the projection are in the index.

By adding the projection `{name:1,birthdate:1,_id:0}` in the previous query, we can limit the returned fields to only `name` and `birthdate`. These fields are part of the index and when we run the `explain()` command, the execution plan shows only two stages:

- **IXSCAN** - Index scan using the compound index
- **PROJECTION_COVERED** - All the information needed is returned by the index, no need to fetch from memory

```javascript
db.customers.explain().find({
  birthdate: {
    $gte:ISODate("1977-01-01")
  },
  active:true
},
{
  name:1,
  birthdate:1, 
  _id:0
}).sort({
  birthdate:-1,
  name:1
})
```