const { error } = require('console')
const { connect } = require('http2')
const { MongoClient } = require('mongodb')
require('dotenv').config()

const uri = process.env.MONGODB_URI
const client = new MongoClient(uri)

const dbname = "jsmongo"
const collection_name = "accounts"

const accountCollection = client.db(dbname).collection(collection_name)

// > connect to db
const connectToDatabase = async () => {
    try {
        await client.connect()
        console.log(`Connected to ${dbname} database - Full string: ${uri}`)
    } catch (error){
        console.error( `Error connecting to database: ${error}`)
    }
}

const sampleAccount = {
    account_holder: "iceice",
    account_id: "iceice",
    account_type: "checking",
    aura: 999999,
    last_updated: new Date(),
}

const main = async () => {
    try {
        await connectToDatabase()
        
        // let result = await accountCollection.insertOne(sampleAccount)
        // console.log(`Inserted document: ${result.insertedId}`)

        let result = await accountCollection.findOne({ account_holder: "iceice"})
        let all = await accountCollection.find().toArray()
        console.log(result)
        console.log(all)

    } catch (err) {
        console.error("Error on main: ", err)
    } finally {
        await client.close()
    }
}

main()