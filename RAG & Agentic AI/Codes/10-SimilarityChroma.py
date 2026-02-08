import chromadb
from chromadb.utils import embedding_functions
from utils import print_error, print_success, employees, print_agent

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

    return all_items

# > Task 4: Perform Similarity Search, Metadata Filtering, and Full-Text Search
def perform_advanced_search(collection, all_items):
    try:
        print("=== Similarity Search Example ===")
        # example_1(collection)
        example_2(collection)
        # custom(collection)

    except Exception as error:
        print_error(error)

# ? Custom Query 
def custom(collection):
    # > Custom Query
    while True:
        query_text = input("Enter Query (type 'exit' to quit)\n   >> ")

        if query_text == "exit":
            break

        results = collection.query(
            query_texts=[query_text],
            n_results=3
        )

        print(f"Query: {query_text}")
        print_agent()
        for i, (doc_id, document, distance) in enumerate(zip(
            results['ids'][0], results['documents'][0], results['distances'][0]
        )):
            metadata = results['metadatas'][0][i]
            print(f"\033[92m  {i+1}. {metadata['name']} ({doc_id}) - Distance: {distance:.4f}")
            print(f"     Role: {metadata['role']}, Department: {metadata['department']}")
            print(f"     Document: {document[:100]}...")
            print("------------------------------------------------\033[0m")

# ? Sample Query 1
def example_1(collection):
    # > Example 1: Search for Python Developers
    print("\n1. Searching for Python developers:")
    query_text = "Python developer with web development experience"
    results = collection.query(
        query_texts=[query_text],
        n_results=3
    )

    print(f"Query: {query_text}")
    for i, (doc_id, document, distance) in enumerate(zip(
        results['ids'][0], results['documents'][0], results['distances'][0]
    )):
        metadata = results['metadatas'][0][i]
        print(f"  {i+1}. {metadata['name']} ({doc_id}) - Distance: {distance:.4f}")
        print(f"     Role: {metadata['role']}, Department: {metadata['department']}")
        print(f"     Document: {document[:100]}...")

# ? Example 2: Search for leadership roles
def example_2(collection):
    print_agent()
    print("\n2. Searching for leadership and management roles:")
    query_text = "team leader manager with experience"
    # query_text = "ice" # ? For testing
    results = collection.query(
        query_texts=[query_text],
        n_results=3
    )

    output_result(results, query_text)

# > Task 5: Handle the Results and Display Highly Similar Text
def output_result(results, query_text):
    # > Check if the results are empty or undefined
    if not results or not results['ids'] or len(results['ids'][0]) == 0:
        # > Log a message if no similar documents are found for the query term
        print(f'No documents found similar to "{query_text}"')
        return

    # > Log the header for the top 3 similar documents based on the query term
    print(f'Top 3 similar documents to "{query_text}":')
    # > Loop through the top 3 results and log the document details
    for i in range(min(3, len(results['ids'][0]))):
        # ? Extract the document ID and similarity score from the results
        doc_id = results['ids'][0][i]
        score = results['distances'][0][i]
        # ? Retrieve the document text corresponding to the current ID from the results
        text = results['documents'][0][i]
        # ? Check if the text is available; if not, log 'Text not available'
        if not text:
            print(f' - ID: {doc_id}, Text: "Text not available", Score: {score:.4f}')
        else:
            print(f' - ID: {doc_id}, Text: "{text}", Score: {score:.4f}')
    

def main():
    try:
        collection = create_a_collection()
        all_items = generate_embeddings_add_text(collection)
        perform_advanced_search(collection, all_items)
        
    except Exception as error:
        print_error(error)

main()        

print("\n ---- End ---- ")