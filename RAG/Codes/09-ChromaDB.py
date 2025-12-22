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

# > Define main functiuon to interact with the Chroma Database
def main():
    try:
        pass
    except Exception as error:
        print(f"Error: {error}")
print(" --- End --- ")