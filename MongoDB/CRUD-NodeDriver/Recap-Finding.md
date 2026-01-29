# Querying a MongoDB Collection in Node.js Applications
Review the following code, which demonstrates how to query documents in MongoDB with Node.js.

## Using find()
The find() method is a read operation that returns a cursor to the documents that match the query. The find() method takes a query or filter document as an argument. If you do not specify a query document, the find() method returns all documents in the collection.

In this example, we find all accounts that have a balance greater than or equal to 4700. The find() method accepts a query filter, which we assign to a variable called documentsToFind. We process each document that’s returned from the find() method by iterating the cursor, which is assigned to the variable result.
```js
const dbname = "bank"
const collection_name = "accounts"
 
const accountsCollection = client.db(dbname).collection(collection_name)

// Document used as a filter for the find() method
const documentsToFind = { balance: { $gt: 4700 } }
 
const main = async () => {
 try {
   await connectToDatabase()
   // find() method is used here to find documents that match the filter
   let result = accountsCollection.find(documentsToFind)
   let docCount = accountsCollection.countDocuments(documentsToFind)
   await result.forEach((doc) => console.log(doc))
   console.log(`Found ${await docCount} documents`)
 } catch (err) {
   console.error(`Error finding documents: ${err}`)
 } finally {
   await client.close()
 }
}

main()
```

## Using findOne()
In this example, we return a single document from a query, which is assigned to a variable called documentToFind. We use the findOne() method on the collection object to return the first document that matches the filter criteria, which are defined in the documentToFind variable.
```js
const dbname = "bank"
const collection_name = "accounts"
 
const accountsCollection = client.db(dbname).collection(collection_name)

// Document used as a filter for the findOne() method
const documentToFind = { _id: ObjectId("62a3638521a9ad028fdf77a3") }

const main = async () => {
 try {
   await connectToDatabase()
   // findOne() method is used here to find a the first document that matches the filter
   let result = await accountsCollection.findOne(documentToFind)
   console.log(`Found one document`)
   console.log(result)
 } catch (err) {
   console.error(`Error finding document: ${err}`)
 } finally {
   await client.close()
 }
}

main()
```