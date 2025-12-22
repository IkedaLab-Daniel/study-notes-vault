import chromadb
from chromadb.utils import embedding_functions
from utils import print_error, print_success

ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.Client()
collection_name = "iceice"

def create_a_collection():
    collection = client.create_collection(
        name=collection_name,
        metadata={"description": "dev.iceice"},
        configuration={
            "hnsw": {"space": "cosine"},
            "embedding_function": ef
        }
    )
    print_success(f"Collection created: {collection.name}")

def main():
    try:
        create_a_collection()
        
    except Exception as error:
        print_error(error)

main()        

print(" --- End --- ")