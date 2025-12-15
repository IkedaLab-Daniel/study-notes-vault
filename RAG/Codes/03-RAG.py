from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import faiss
from langchain_community.llms import ollama
from langchain.chains import retrieval_qa

# > Step 1 - Load Document
loader = TextLoader("ai.txt")
document = loader.load()

# > Step 2 - Split document into chunk
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

print(f"""\033[92m
    |-----------------------------------------|
    >> Code execution completed successfully <<
    |-----------------------------------------|
\033[0m""")