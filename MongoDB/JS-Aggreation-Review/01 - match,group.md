# Using MongoDB Aggregation Stages with Node.js: $match and $group
Review the following code, which demonstrates how to build the $match and $group stages of an aggregation pipeline in MongoDB with Node.js.


## Using $match
Aggregation gives you a way to transform data from your collection by passing documents from one stage to another. These stages can consist of operators that transform or organize your data in a specific way. In this lesson, we used $match and $group.

The $match stage filters documents by using a simple equality match, like $match: { author: "Dave"}, or aggregation expressions using comparison operators, like $match: { likes: { $gt: 100 } }. This operator accepts a query document and passes the resulting documents to the next stage. $match should be placed early in your pipeline to reduce the number of documents to process.


## Using $group
The $group stage separates documents according to a group key and returns one document for every unique group key. The group key is usually a field in the document, but it can also be an expression that resolves to a field. The $group stage can be used with aggregation expressions to perform calculations on the grouped documents. An example of this is adding up the total number of movie tickets sold by using the $sum operator:
```js
$group: { _id: "$movie", totalTickets: { $sum: "$tickets" } }
```
The "$movie" is the group key, and the totalTickets field is the result of the $sum operator.

In the following code, we assign our collection name to a variable for convenience. First, we declare some variables to hold the database connection and the collection we'll use:
```js
const client = new MongoClient(uri)
const dbname = "bank";
const collection_name = "accounts";
const accountsCollection = client.db(dbname).collection(collection_name);
```

Next, we build an aggregation pipeline that uses $match and $group and that will find accounts with a balance of less than $1,000. Then we group the results by the account_type, and calculate the total_balance and avg_balance for each type.
```js
const pipeline = [
  // Stage 1: match the accounts with a balance less than $1,000
  { $match: { balance: { $lt: 1000 } } },
  // Stage 2: Calculate average balance and total balance
  {
    $group: {
      _id: "$account_type",
      total_balance: { $sum: "$balance" },
      avg_balance: { $avg: "$balance" },
    },
  },
]
```
To run an aggregation pipeline, we append the aggregate method to the collection. The aggregate method takes an array of stages as an argument, which is stored in a variable. The aggregate method returns a cursor that we can iterate over to get the results.
```js
const main = async () => {
  try {
    await client.connect()
    console.log(`Connected to the database 🌍. \nFull connection string: ${safeURI}`)
    let result = await accountsCollection.aggregate(pipeline)
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