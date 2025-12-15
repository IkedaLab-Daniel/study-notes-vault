from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import faiss
from langchain_community.llms import ollama
from langchain.chains import retrieval_qa

# > Step 1 - Load Document
loader = TextLoader("ai.txt")
document = loader.load()

print(f"""\033[92m
    |-----------------------------------------|
    >> Code execution completed successfully <<
    |-----------------------------------------|
\033[0m""")