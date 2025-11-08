from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://iceice:iceice@myatlasclusteredu.og4ezo2.mongodb.net/?appName=myAtlasClusterEDU"

client = MongoClient(MONGODB_URI)

for db_name in client.list_database_names():
    print(db_name)