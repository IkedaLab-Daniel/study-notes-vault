""" Setup """
# > Ignore Warning
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

# > Load ENV file
from dotenv import load_dotenv
import os

load_dotenv()

# > 1 - Build LLM
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models.extensions.langchain import WatsonxLLM

def llm():
    model_id = 'mistralai/mistral-small-3-1-24b-instruct-2503'

    parameter = {
        GenParams.MAX_NEW_TOKENS: 256,
        GenParams.TEMPERATURE: 0.5
    }


    credentials = {
        "url": os.getenv('URL'),
        "api_key": os.getenv('API_KEY')
    }

    project_id = os.getenv('PROJECT_ID')

    model = ModelInference(
        model_id=model_id,
        params=parameter,
        credentials=credentials,
        project_id=project_id,
    )
    
    watsonxLLM = WatsonxLLM(model=model)
    return watsonxLLM

# > Use the Text Splitter
from langchain.text_splitter import RecursiveCharacterTextSplitter

def text_splitter(data, chunk_size, chunk_overlap):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    # ? Use split_documents for Document objects, split_text for strings
    if isinstance(data, list):
        chunk = splitter.split_documents(data)
    else:
        chunk = splitter.split_text(data)
    return chunk

# > Create embedding model
from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames
from langchain_ibm import WatsonxEmbeddings

def watsonx_embedding():
    embed_params = {
        EmbedTextParamsMetaNames.TRUNCATE_INPUT_TOKENS: 3,
        EmbedTextParamsMetaNames.RETURN_OPTIONS: {"input_text": True},
    }

    watsonx_embedding = WatsonxEmbeddings(
        model_id="ibm/slate-125m-english-rtrvr-v2",
        url=os.getenv("URL"),
        project_id=os.getenv("PROJECT_ID"),
        params=embed_params,
        apikey=os.getenv("API_KEY")
    )

    return watsonx_embedding

# > Use Retrievers
    # > Vector Store-Backed Retriever
    # > Use TextLoader

from langchain_community.document_loaders import TextLoader

loader = TextLoader("companypolicies.txt")
txt_data = loader.load()
chunks_txt = text_splitter(txt_data, 200, 20)

    # > Store the embedding into a Chroma DB
from langchain.vectorstores import Chroma

vectordb =  Chroma.from_documents(chunks_txt, watsonx_embedding())

query = "Email policy"
retriever = vectordb.as_retriever(search_kwargs={"k": 3})  # ? K -> Limit retrival Result
# docs = retriever.invoke(query)
# print(docs)

    # > MMR Search
mmr_retriever = vectordb.as_retriever(search_type="mmr")
# docs = mmr_retriever.invoke(query)
# print(docs)

threshold_retriever = vectordb.as_retriever(
    # ? You can also set a retrieval method that defines a similarity score threshold, returning only documents with a score above that threshold.
    search_type="similarity_score_threshold",
    search_kwargs={"score_threshold": 0.4}
)

thres_docs = threshold_retriever.invoke(query)
# print(thres_docs)

# > Multi-Query Reader
from langchain_community.document_loaders import PyPDFLoader

loader =  PyPDFLoader("langchain-paper.pdf")
pdf_data = loader.load()

# print(pdf_data[0]) # ? Print Page 1

    # > Split
chunks_pdf = text_splitter(pdf_data, 500, 20)

    # > VectorDB
ids = vectordb.get()["ids"]
vectordb.delete(ids) # We need to delete existing embeddings from previous documents and then store current document embeddings in.
vectordb = Chroma.from_documents(documents=chunks_pdf, embedding=watsonx_embedding())

    # > MultiQueryRetriever
from langchain.retrievers.multi_query import MultiQueryRetriever

query = "What does the paper say about langchain?"

retriever = MultiQueryRetriever.from_llm(
    retriever=vectordb.as_retriever(), llm=llm()
)
    # > Set logging for the queries
import logging

logging.basicConfig()
logging.getLogger("langchain.retrievers.multi_query").setLevel(logging.INFO)

# docs = retriever.invoke(query)
# print(docs)

# > Self Quering Retriever
from langchain_core.documents import Document
from langchain.chains.query_constructor.base import AttributeInfo
from langchain.retrievers.self_query.base import SelfQueryRetriever
from lark import lark

docs = [
    Document(
        page_content="A bunch of scientists bring back dinosaurs and mayhem breaks loose",
        metadata={"year": 1993, "rating": 7.7, "genre": "science fiction"},
    ),
    Document(
        page_content="Leo DiCaprio gets lost in a dream within a dream within a dream within a ...",
        metadata={"year": 2010, "director": "Christopher Nolan", "rating": 8.2},
    ),
    Document(
        page_content="A psychologist / detective gets lost in a series of dreams within dreams within dreams and Inception reused the idea",
        metadata={"year": 2006, "director": "Satoshi Kon", "rating": 8.6},
    ),
    Document(
        page_content="A bunch of normal-sized women are supremely wholesome and some men pine after them",
        metadata={"year": 2019, "director": "Greta Gerwig", "rating": 8.3},
    ),
    Document(
        page_content="Toys come alive and have a blast doing so",
        metadata={"year": 1995, "genre": "animated"},
    ),
    Document(
        page_content="Three men walk into the Zone, three men walk out of the Zone",
        metadata={
            "year": 1979,
            "director": "Andrei Tarkovsky",
            "genre": "thriller",
            "rating": 9.9,
        },
    ),
]

metadata_field_info = [
    AttributeInfo(
        name="genre",
        description="The genre of the movie. One of ['science fiction', 'comedy', 'drama', 'thriller', 'romance', 'action', 'animated']",
        type="string",
    ),
    AttributeInfo(
        name="year",
        description="The year the movie was released",
        type="integer",
    ),
    AttributeInfo(
        name="director",
        description="The name of the movie director",
        type="string",
    ),
    AttributeInfo(
        name="rating", description="A 1-10 rating for the movie", type="float"
    ),
]

vectordb = Chroma.from_documents(docs, watsonx_embedding())

document_content_description = "Brief summary of a movie"

retriever = SelfQueryRetriever.from_llm(
    llm(),
    vectordb,
    document_content_description,
    metadata_field_info,
)

result = retriever.invoke("What's a highly rated (above 8.5) science fiction film?")
print(result)

print("\033[92m --- END --- ")