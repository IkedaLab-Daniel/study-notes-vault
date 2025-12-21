from pymongo import MongoClient
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv('MONGO_URI')
client = MongoClient(uri)
db = client.rag_db
collection = db.documents

model = SentenceTransformer("all-MiniLM-L6-v2")

def ingest_document():
    documents = [
        "MongoDB supports vector search for AI applications.",
        "RAG combines retrieval and generation.",
        "Vector databases store embeddings for similarity search.",
        "Agentic AI systems can reason in steps."
    ]

    for doc in documents:
        embedding = model.encode(doc).tolist()
        collection.insert_one({
            "text": doc,
            "embedding": embedding
        })

    print("Documents ingested")

def retrieve(query, k=3):
    """ Vector Search Function (Core RAG Logic) """

    query_embedding = model.encode(query).tolist()

    pipeline = [
        {
            "$vectorSearch": {
                "index": "vector_index",
                "queryVector": query_embedding,
                "path": "embedding",
                "numCandidates": 100,
                "limit": k
            }
        },
        {
            "$project": {
                "_id": 0,
                "text": 1,
                "score": {"$meta": "vectorSearchScore"}
            }
        }
    ]

    return list(collection.aggregate(pipeline))

llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=512
)

def answer(question):
    docs = retrieve(question)
    print("Retrieved docs:", docs)  # ! DEBUG

    context = "\n".join([d["text"] for d in docs])

    prompt = f"""
You are an AI assistant.
Use the context to answer the question.

Context:
{context}

Question:
{question}

Answer:
"""
    
    response = llm(prompt)[0]["generated_text"]
    return response

def main():
    print("MongoDB RAG CLI")
    while True:
        q = input("\n> ")
        if q.lower() == "exit":
            break
        print("\n" + answer(q))

if __name__ == "__main__":
    main()