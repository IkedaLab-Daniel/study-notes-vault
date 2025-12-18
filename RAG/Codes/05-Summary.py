def warn(*args, **kwargs):
    pass

import warnings
warnings.warn = warn
warnings.filterwarnings("ignore")

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory

from langchain_community.chat_models import ChatOllama
from print_agent import print_agent

# > 1 - Load
    # ? See file Download.py

# > 2 - Split
filename = 'companyPolicies.txt'

loader = TextLoader(filename)
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
# ! print(len(texts))

# > 3 - Embedding and Storing
embeddings = HuggingFaceEmbeddings()
docsearch = Chroma.from_documents(texts, embeddings)  # store the embedding in docsearch using Chromadb
print('document ingested')

# > LLM Model Construction
flan_ul2_llm = ChatOllama(
    model="gemma3:1b",     # local LLM
    temperature=0.5,      # GenParams.TEMPERATURE
    num_predict=256       # GenParams.MAX_NEW_TOKENS
)

# > Using Prompt Template
prompt_template = """
Use the information from the document to answer the question at the end. If you don't know the answer, just say that you don't know, definately do not try to make up an answer.

{context}

Question: {question}
"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["context", "question"]
)

chain_type_kwargs = {"prompt": PROMPT}

# > Retrieval | Intregrating Langchain

qa = RetrievalQA.from_chain_type(
    llm=flan_ul2_llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(),
    chain_type_kwargs=chain_type_kwargs,
    return_source_documents=False
)
query = input("Enter query: ")
response = qa.invoke(query)

print(f"""\033[92m
|-------------------------- Query -----------------------------|
  >> {response['query']}
|--------------------------------------------------------------|
\033[0m""")
print_agent()
print(f""" \033[92m
|-------------------------- Answer ----------------------------|
  >> {response['result']}
|--------------------------------------------------------------|
\033[0m""")

print("\n\n------------------------------------------\nAll working")