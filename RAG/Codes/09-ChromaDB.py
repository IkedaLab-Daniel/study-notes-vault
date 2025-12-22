import chromadb
from chromadb.utils import embedding_functions
print("\033[92m")

# > Define the embedding function using SentenceTransformers
ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# > Create new instance of ChromaClient
client = chromadb.Client()

# > Define the name for the collection to be created or retrieved
collection_name = "my_grocery_collection"

# > Function to perform similarity search in the collection
def perform_similarity_search(collection, all_items):
    try:
        query_term = input("Enter query term: \n >>> ")

        # > Perform a query search for the most similar documents to the 'query_term'
        results = collection.query(
            query_text=[query_term],
            n_result=3 # ? Top 3 result
        )

        print(f"\nQuery result for '{query_term}'")
        print(results)

    except Exception as error:
        print("Error:", error)

# > Define main functiuon to interact with the Chroma Database
def main():
    try:
        collection = client.create_collection(
            name=collection_name,
            metadata={"description": "A collection for storing grocery data"},
            configuration={
                "hnsw": {"space": "cosine"},
                "embedding_function": ef
            }
        )
        print(f"Collection created:", collection.name)

        texts = [
            'fresh red apples',
            'organic bananas',
            'ripe mangoes',
            'whole wheat bread',
            'farm-fresh eggs',
            'natural yogurt',
            'frozen vegetables',
            'grass-fed beef',
            'free-range chicken',
            'fresh salmon fillet',
            'aromatic coffee beans',
            'pure honey',
            'golden apple',
            'red fruit'
        ]

        # > Create a list of unique IDs for each text item in the 'texts' array
        # > Each ID follows the format 'food_<index>', where <index> starts from 1
        ids = [f"food_{index + 1}" for index, _ in enumerate(texts)]

        # > Add documents and their corresponding IDs to the collection
        # > The `add` method inserts the data into the collection
        # > The documents are the actual text items, and the IDs are unique identifiers
        # > ChromaDB will automatically generate embeddings using the configured embedding function
        collection.add(
            documents=texts,
            metadatas=[{"source": "grocery_store", "category": "food"} for _ in texts],
            ids=ids
        )

        # > Retrieve all the items (documents) stored in the collection
        # > The `get` method fetches all data from the collection
        all_items = collection.get()
        # > Log the retrieved items to the console for inspection
        # > This will print out all the documents, IDs, and metadata stored in the collection
        # print("Collection contents:", all_items)
        # print(f"Number of documents: {len(all_items['documents'])}")

    except Exception as error:
        print(f"Error: {error}")

if __name__ == "__main__":
    main()
    print(" --- End --- ")