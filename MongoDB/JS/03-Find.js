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