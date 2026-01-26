require('dotenv').config();

uri = process.env.MONGODB_URI
const {MongoClient} = require('mongodb')

console.log(uri)

const client = new MongoClient(uri)
const dbname = "sample"

const connectToDatabase = async () => {
    try {
        await client.connect();
        console.log(`
₊˚｡⋆❆⋆｡˚₊
            `)
        console.log(`Connected to "${dbname}" database`)
        const databaselist = await client.db().admin().listDatabases()
        console.log("\nDatabases: ")
        console.log(databaselist)
    } catch (ice) {
        console.log(`Error connecting to database: ${ice}`)
    }
}

const main = async () => {
    try {
        await connectToDatabase();
    } catch (ice) {
        console.log(`Error connecting to the database: ${ice}`)
    } finally {
        await client.close()
    }
}

main()