## Returning Specific Data from a Query in MongoDB
Review the following code, which demonstrates how to return selected fields from a query.

# Add a Projection Document
To specify fields to include or exclude in the result set, add a projection document as the second parameter in the call to db.collection.find().

Syntax:
```js
db.collection.find( <query>, <projection> )
```

## Include a Field
To include a field, set its value to 1 in the projection document.

Syntax:

```js
db.collection.find( <query>, { <field> : 1 })
```

Example:
```js
// Return all restaurant inspections - business name, result, and _id fields only
db.inspections.find(
  { sector: "Restaurant - 818" },
  { business_name: 1, result: 1 }
)
```

## Exclude a Field
To exclude a field, set its value to 0 in the projection document.

Syntax:
```js
db.collection.find(query, { <field> : 0, <field>: 0 })
```
Example:
```js
// Return all inspections with result of "Pass" or "Warning" - exclude date and zip code
db.inspections.find(
  { result: { $in: ["Pass", "Warning"] } },
  { date: 0, "address.zip": 0 }
)
```

While the _id field is included by default, it can be suppressed by setting its value to 0 in any projection.
```js
// Return all restaurant inspections - business name and result fields only
db.inspections.find(
  { sector: "Restaurant - 818" },
  { business_name: 1, result: 1, _id: 0 }
)
```