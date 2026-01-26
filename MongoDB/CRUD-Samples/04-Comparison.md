Finding Documents by Using Comparison Operators
Review the following comparison operators: $gt, $lt, $lte, and $gte.

## $gt
Use the $gt operator to match documents with a field greater than the given value. For example:

```sh
db.sales.find({ "items.price": { $gt: 50}})
```

## $lt
Use the $lt operator to match documents with a field less than the given value. For example:

```sh
db.sales.find({ "items.price": { $lt: 50}})
```

## $lte
Use the $lte operator to match documents with a field less than or equal to the given value. For example:

```sh
db.sales.find({ "customer.age": { $lte: 65}})
```

## $gte
Use the $gte operator to match documents with a field greater than or equal to the given value. For example:

```sh
db.sales.find({ "customer.age": { $gte: 65}})
```