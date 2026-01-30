# Using MongoDB Aggregation Stages with Node.js: $sort and $project
Review the following code, which demonstrates how to build the $sort and $project stages of an aggregation pipeline in MongoDB with Node.js.

## $sort
Aggregation is a powerful tool that gives us the ability to compute and transform our data. In this lesson, we focused on the $sort and $project stages.

The $sort stage takes all the input documents and sorts them in a specific order. The documents can be sorted in numerical, alphabetical, ascending, or descending order.

The $sort stage accepts a sort key that specifies the field to sort on. The sort key can be 1 for ascending order or -1 for descending order. For example:

- { $sort: { balance: 1 } } sorts the documents in ascending order by the balance field.

- { $sort: { balance: -1 } } sorts the documents in descending order by the balance field.

## $project
The $project stage takes all the input documents and passes along only a subset of the fields in those documents by specifying the fields to include or exclude.

For example, if we want our resulting documents to include only the account_id, we write { $project: { _id: 0, account_id: 1 } }. The _id field is excluded by setting it to 0, and the account_id field is included by setting it to 1.

The $project stage can also create new computed fields based on data from the original documents. An example of this is creating a projected field that contains someone's full name, where only the first and last names are stored in the original document.

In the following example, we build an aggregation pipeline that uses $match, $sort, and $project, and that will find checking accounts with a balance of greater than or equal to $1,500. Then, we sort the results by the balance in descending order and return only the account_id, account_type, balance, and a new computed field named gbp_balance, which stands for Great British Pounds (GBP) balance.
```js
const pipeline = [
  // Stage 1: $match - filter the documents (checking, balance >= 1500)
  { $match: { account_type: "checking", balance: { $gte: 1500 } } },

  // Stage 2: $sort - sorts the documents in descending order (balance)
  { $sort: { balance: -1 } },

  // Stage 3: $project - project only the requested fields and one computed field (account_type, account_id, balance, gbp_balance)
  {
    $project: {
      _id: 0,
      account_id: 1,
      account_type: 1,
      balance: 1,
      // GBP stands for Great British Pound
      gbp_balance: { $divide: ["$balance", 1.3] },
    },
  },
]
```

To run an aggregation pipeline, we append the aggregate method to the collection. The aggregate method takes an array of stages as an argument, which is stored here as a variable. The aggregate method returns a cursor that we can iterate over to get the results.
```js
const main = async () => {
  try {
    await client.connect()
    console.log(`Connected to the database 🌍\n ${uri}`)
    let accounts = client.db("bank").collection("accounts")
    let result = await accounts.aggregate(pipeline)
    for await (const doc of result) {
      console.log(doc)
    }
  } catch (err) {
    console.error(`Error connecting to the database: ${err}`)
  } finally {
    await client.close()
  }
}

main()
```