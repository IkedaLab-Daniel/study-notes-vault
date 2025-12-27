from dotenv import load_dotenv
import os
load_dotenv()

# > Use the Self-Querying Retriever to invoke a query with a filter

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from ibm_watsonx_ai.metanames import EmbedTextParamsMetaNames
from langchain_ibm import WatsonxEmbeddings
from utils import print_agent
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models import ModelInference
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

def main():
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
    print_agent()
    print(result)

if __name__ == "__main__":
    print(""" 
11 - Exercise 2: Use the Self-Querying Retriever to invoke a query with a filter
""")
    main()