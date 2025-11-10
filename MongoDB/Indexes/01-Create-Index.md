# Creating a Single Field Index

Review the code below, which demonstrates how to create a single field index in a collection.

## Create a Single Field Index

Use `createIndex()` to create a new index in a collection. Within the parentheses of `createIndex()`, include an object that contains the field and sort order.

```javascript
db.customers.createIndex({
  birthdate: 1
})
```

## Create a Unique Single Field Index

Add `{unique:true}` as a second, optional, parameter in `createIndex()` to force uniqueness in the index field values. Once the unique index is created, any inserts or updates including duplicated values in the collection for the index field/s will fail.

```javascript
db.customers.createIndex({
  email: 1
},
{
  unique:true
})
```

**Note:** MongoDB only creates the unique index if there is no duplication in the field values for the index field/s.

## View the Indexes used in a Collection

Use `getIndexes()` to see all the indexes created in a collection.

```javascript
db.customers.getIndexes()
```

## Check if an Index is Being Used on a Query

Use `explain()` in a collection when running a query to see the Execution plan. This plan provides the details of the execution stages (IXSCAN, COLLSCAN, FETCH, SORT, etc.).

- **IXSCAN** stage indicates the query is using an index and what index is being selected.
- **COLLSCAN** stage indicates a collection scan is perform, not using any indexes.
- **FETCH** stage indicates documents are being read from the collection.
- **SORT** stage indicates documents are being sorted in memory.

```javascript
db.customers.explain().find({
  birthdate: {
    $gt:ISODate("1995-08-01")
  }
})

db.customers.explain().find({
  birthdate: {
    $gt:ISODate("1995-08-01")
  }
}).sort({
  email:1
})
```