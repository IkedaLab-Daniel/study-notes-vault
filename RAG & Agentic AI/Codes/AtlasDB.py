from pymongo.mongo_client import MongoClient
from pymongo.operations import SearchIndexModel
from dotenv import load_dotenv
import os

load_dotenv()
import time
# Connect to your Atlas deployment
uri = os.getenv('MONGO_URI')
client = MongoClient(uri)
# Access your database and collection
database = client["rag_db"]
collection = database["documents"]
# Build the vector search index model
search_index_model = SearchIndexModel(
    definition={
        "fields": [
            {
                "type": "vector",
                "path": "embedding",         # your vector field name
                "numDimensions": 384,        # change as appropriate
                "similarity": "cosine"       # use "dotProduct" or "euclidean" if needed
            }
        ]
    },
    name="vector_index",
    type="vectorSearch"
)
# Create the search index
index_name = collection.create_search_index(model=search_index_model)
print(f"New search index '{index_name}' is building...")

# Wait until index is ready
while True:
    indexes = collection.list_search_indexes()
    idx = next((i for i in indexes if i["name"] == index_name), None)
    if idx and idx.get("queryable"):
        print(f"Index '{index_name}' is ready.")
        break
    print("Waiting for index to be ready...")
    time.sleep(5)

client.close()