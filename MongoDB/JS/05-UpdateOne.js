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