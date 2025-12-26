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

print("\033[92m --- END --- ")

