from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA

# > Step 1 - Load Document
loader = TextLoader("ai.txt")
documents = loader.load()

# > Step 2 - Split document into chunk
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)

# > Step 3 - Create Embedding
embeddings = OllamaEmbeddings(
    model="nomic-embed-text"
)

# > Step 4 - Create vector store
vectorstore = FAISS.from_documents(chunks, embeddings)

# > Step 5 - Create retriever
retriever = vectorstore.as_retriever(
    search_kwargs={"k":2}
)

# > Step 6 - Load local LLM
llm = Ollama(
    model="gemma3:1b",
    temperature=0
)

# > Step 7 - Build retrieval QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever,
    chain_type="stuff"
)

# > Step 8 - Test Questions
questions = [
    "What is Artificial Intelligence?",
    "What is machine learning?",
    "Where is AI used?"
]

print("\n\n\n")

for q in questions:
    print(f"""\033[34m
|----------------------------------------------------------------|
        >>    Question: {q} <<
|----------------------------------------------------------------|
    \033[0m""")
    answer = qa_chain.invoke(q)
    print(f"""\033[92m
|--------------------------------|
            Answer:
{answer["result"]}
|--------------------------------|
""")



print(f"""\033[92m
    |-----------------------------------------|
    >> Code execution completed successfully <<
    |-----------------------------------------|
\033[0m""")