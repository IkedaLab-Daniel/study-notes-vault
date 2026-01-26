require('dotenv').config();

uri = process.env.MONGODB_URI
const {MongoClient} = require('mongodb')

console.log(uri)

const client = new MongoClient(uri)
const dbname = "sample"

const connectToDatabase = async () => {
    try {
        await client.connect();
        console.log(`Connect to ${dbname} database`)
    } catch (ice) {
        console.log(`Error connecting to database: ${ice}`)
    }
}