/**
 * Using MongoDB Aggregation Stages with Node.js: $sort and $project
 * 
 * This demonstrates how to build the $sort and $project stages of an 
 * aggregation pipeline in MongoDB with Node.js.
 */

const { MongoClient } = require('mongodb')
require('dotenv').config()

const uri = process.env.MONGODB_URI
const client = new MongoClient(uri)

// Database and collection configuration
const dbname = "bank"
const collection_name = "accounts"

/**
 * Aggregation Pipeline
 * 
 * $sort: Takes all input documents and sorts them in a specific order.
 *        Sort key: 1 for ascending order, -1 for descending order.
 *        Examples:
 *        - { $sort: { balance: 1 } } - ascending order by balance
 *        - { $sort: { balance: -1 } } - descending order by balance
 * 
 * $project: Passes along only a subset of fields by specifying which to include/exclude.
 *           Can also create new computed fields based on original document data.
 *           Examples:
 *           - { $project: { _id: 0, account_id: 1 } } - exclude _id, include account_id
 *           - Can create computed fields like full names, currency conversions, etc.
 * 
 * Pipeline Goal:
 * - Find checking accounts with balance >= $1,500
 * - Sort by balance in descending order
 * - Return account_id, account_type, balance, and computed gbp_balance field
 */

const pipeline = [
  // Stage 1: Filter for checking accounts with balance >= $1,500
  { 
    $match: { 
      account_type: "checking", 
      balance: { $gte: 1500 } 
    } 
  },

  // Stage 2: Sort documents by balance in descending order (highest first)
  { 
    $sort: { 
      balance: -1 
    } 
  },

  // Stage 3: Project only requested fields and add computed field
  {
    $project: {
      _id: 0,
      account_id: 1,
      account_type: 1,
      balance: 1,
      // Compute GBP (Great British Pound) balance using conversion rate
      gbp_balance: { $divide: ["$balance", 1.3] }
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
    
    // Get collection reference
    let accounts = client.db(dbname).collection(collection_name)
    
    // Execute aggregation pipeline
    let result = await accounts.aggregate(pipeline)
    
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
