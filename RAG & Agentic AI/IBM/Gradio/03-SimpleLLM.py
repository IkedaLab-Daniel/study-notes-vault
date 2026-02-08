# Import the necessary packages
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai import Credentials
from langchain_ibm import WatsonxLLM
from dotenv import load_dotenv
import os

load_dotenv()

watsonxai_API = os.getenv("api_key")

# Specify the model and project settings 
# (make sure the model you wish to use is commented out, and other models are commented)
#model_id = 'mistralai/mistral-small-3-1-24b-instruct-2503' # Specify the Mixtral 8x7B model
model_id = 'ibm/granite-3-8b-instruct' # Specify IBM's Granite 3.3 8B model

# Set the necessary parameters
parameters = {
    GenParams.MAX_NEW_TOKENS: 256,  # Specify the max tokens you want to generate
    GenParams.TEMPERATURE: 0.5, # This randomness or creativity of the model's responses
}

# Replace with your actual IBM Watson project ID (UUID format)
# You can find this in your IBM Cloud Watson Studio project settings
project_id =  os.getenv("project_id") # Replace this with your actual project GUID

# Wrap up the model into WatsonxLLM inference
watsonx_llm = WatsonxLLM(
    model_id=model_id,
    url="https://jp-tok.ml.cloud.ibm.com",
    project_id=project_id,
    params=parameters,
    apikey=watsonxai_API
)

# Get the query from the user input
query = input("Please enter your query: ")

# Print the generated response
print(watsonx_llm.invoke(query))