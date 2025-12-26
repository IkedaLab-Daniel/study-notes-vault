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
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )

    chunk = text_splitter.split_text(data)
    return chunk

print("\033[92m --- END --- ")

