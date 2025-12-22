import chromadb
from chromadb.utils import embedding_functions
from utils import print_error, print_success, employees

ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.Client()
collection_name = "iceice"

# > Task 2: Create a Collection and Embed Data
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

    return collection

# > Task 3: Generate Embeddings and Add Texts to a Collection
def generate_embeddings_add_text(collection):
    employee_documents = []
    for employee in employees:
        document = f"{employee['role']} with {employee['experience']} years of experience in {employee['department']}. "
        document += f"Skills: {employee['skills']}. Located in {employee['location']}. "
        document += f"Employment type: {employee['employment_type']}."
        employee_documents.append(document)

    # > Adding data to the collection in the Chroma database
    collection.add(
        ids = [employee["id"] for employee in employees],
        documents = employee_documents,
        metadatas = [{
            "name": employee["name"],
            "department": employee["department"],
            "role": employee["role"],
            "experience": employee["experience"],
            "location": employee["location"],
            "employment_type": employee["employment_type"]
        } for employee in employees]
    )
    # > Retrive All
    all_items = collection.get()
    print_success("Data retrieved")
    print(f"Number of documents: {len(all_items['documents'])}")

def main():
    try:
        collection = create_a_collection()
        generate_embeddings_add_text(collection)
        
    except Exception as error:
        print_error(error)

main()        

print("\n ---- End ---- ")