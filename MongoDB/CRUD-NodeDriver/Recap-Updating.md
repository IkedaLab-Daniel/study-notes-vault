# Updating Documents in Node.js Applications
Review the following code, which demonstrates how to update documents in MongoDB with Node.js.

## Using updateOne()
In this example, we use the updateOne() to update the value of an existing field in a document. Append the updateOne() method to the collection object to update a single document that matches the filter criteria, which are stored in the documentToUpdate variable. The update document contains the changes to be made and is stored in the update variable.
```js
const dbname = "bank"
const collection_name = "accounts"

const accountsCollection = client.db(dbname).collection(collection_name)

const documentToUpdate = { _id: ObjectId("62d6e04ecab6d8e130497482") }

const update = { $inc: { balance: 100 } }


const main = async () => {
  try {
    await connectToDatabase()
    let result = await accountsCollection.updateOne(documentToUpdate, update)
    result.modifiedCount === 1
      ? console.log("Updated one document")
      : console.log("No documents updated")
  } catch (err) {
    console.error(`Error updating document: ${err}`)
  } finally {
    await client.close()
  }
}

main()
```

## Using updateMany()
In this example, we update many documents by adding a value to the transfers_complete array of all checking account documents. The updateMany() method is appended to the collection object. The method accepts a filter that matches the document(s) that we want to update and an update statement that instructs the driver how to change the matching document. Both the filter and the update documents are stored in variables. The updateMany() method updates all the documents in the collection that match the filter.
```js
const database = client.db(dbname);
const bank = database.collection(collection_name);

const documentsToUpdate = { account_type: "checking" };

const update = { $push: { transfers_complete: "TR413308000" } }

const main = async () => {
  try {
    await connectToDatabase()
    let result = await accountsCollection.updateMany(documentsToUpdate, update)
    result.modifiedCount > 0
      ? console.log(`Updated ${result.modifiedCount} documents`)
      : console.log("No documents updated")
  } catch (err) {
    console.error(`Error updating documents: ${err}`)
  } finally {
    await client.close()
  }
}

main()
```