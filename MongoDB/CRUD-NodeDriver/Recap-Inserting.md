# Inserting a Document in Node.js Applications
Review the following code, which demonstrates how to insert a single document and multiple documents into a collection.


## Insert a Document
To insert a single document into a collection, append insertOne() to the collection variable. The insertOne() method accepts a document as an argument and returns a promise. In this example, the document that's being inserted is stored in a variable called sampleAccount, which is declared just above the main() function.
```js
const dbname = "bank"
const collection_name = "accounts"
 
const accountsCollection = client.db(dbname).collection(collection_name)

const sampleAccount = {
 account_holder: "Linus Torvalds",
 account_id: "MDB829001337",
 account_type: "checking",
 balance: 50352434,
}

const main = async () => {
 try {
   await connectToDatabase()
   // insertOne method is used here to insert the sampleAccount document
   let result = await accountsCollection.insertOne(sampleAccount)
   console.log(`Inserted document: ${result.insertedId}`)
 } catch (err) {
   console.error(`Error inserting document: ${err}`)
 } finally {
   await client.close()
 }
}
 
main()
```

##. Insert Many Documents
To insert more than one document, append the insertMany() method to the collection object, and then pass an array of documents to the insertMany() method. The insertMany() method returns a promise. We await the promise to get the result of the operation, which we then use to log the number of documents that are inserted to the console. In this example, the accounts to be inserted are stored in an array variable called sampleAccounts. This variable is defined just above the main() function.
```js
const dbname = "bank"
const collection_name = "accounts"
 
const accountsCollection = client.db(dbname).collection(collection_name)

const sampleAccounts = [
 {
   account_id: "MDB011235813",
   account_holder: "Ada Lovelace",
   account_type: "checking",
   balance: 60218,
 },
 {
   account_id: "MDB829000001",
   account_holder: "Muhammad ibn Musa al-Khwarizmi",
   account_type: "savings",
   balance: 267914296,
 },
]
 
const main = async () => {
 try {
   await connectToDatabase()
   let result = await accountsCollection.insertMany(sampleAccounts)
   console.log(`Inserted ${result.insertedCount} documents`)
   console.log(result)
 } catch (err) {
   console.error(`Error inserting documents: ${err}`)
 } finally {
   await client.close()
 }
}

main()
```