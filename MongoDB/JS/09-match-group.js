/**
 * Using MongoDB Aggregation Stages with Node.js: $match and $group
 * 
 * This demonstrates how to build the $match and $group stages of an 
 * aggregation pipeline in MongoDB with Node.js.
 */

const { MongoClient } = require('mongodb')
require('dotenv').config()

const uri = process.env.MONGODB_URI
const client = new MongoClient(uri)

// Database and collection configuration
const dbname = "bank"
const collection_name = "accounts"
const accountsCollection = client.db(dbname).collection(collection_name)

/**
 * Aggregation Pipeline
 * 
 * $match: Filters documents by using a simple equality match or comparison operators.
 *         Should be placed early in the pipeline to reduce the number of documents.
 *         Example: { $match: { author: "Dave" } } or { $match: { likes: { $gt: 100 } } }
 * 
 * $group: Separates documents according to a group key and returns one document 
 *         for every unique group key. Can be used with aggregation expressions 
 *         to perform calculations.
 *         Example: { $group: { _id: "$movie", totalTickets: { $sum: "$tickets" } } }
 */

const pipeline = [
  // Stage 1: Match accounts with balance less than $1,000
  { 
    $match: { 
      balance: { $lt: 1000 } 
    } 
  },
  
  // Stage 2: Group by account_type and calculate totals
  {
    $group: {
      _id: "$account_type",
      total_balance: { $sum: "$balance" },
      avg_balance: { $avg: "$balance" }
    }
  }
]

/**
 * Main function to execute the aggregation pipeline
 * The aggregate method returns a cursor that we can iterate over to get results
 */
const main = async () => {
  try {
    // Connect to database
    await client.connect()
    console.log(`Connected to the database 🌍`)
    console.log(`Database: ${dbname}`)
    console.log(`Collection: ${collection_name}\n`)
    
    // Execute aggregation pipeline
    let result = await accountsCollection.aggregate(pipeline)
    
    // Iterate through results
    console.log("Aggregation Results:")
    console.log("-------------------")
    for await (const doc of result) {
      console.log(doc)
    }
    
  } catch (err) {
    console.error(`Error connecting to the database: ${err}`)
  } finally {
    await client.close()
    console.log("\nDatabase connection closed")
  }
}

main()