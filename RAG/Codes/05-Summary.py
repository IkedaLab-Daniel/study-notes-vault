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
import wget

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
    model="gemma:2b",     # local LLM
    temperature=0.5,      # GenParams.TEMPERATURE
    num_predict=256       # GenParams.MAX_NEW_TOKENS
)

print("\n\n------------------------------------------\nAll working")