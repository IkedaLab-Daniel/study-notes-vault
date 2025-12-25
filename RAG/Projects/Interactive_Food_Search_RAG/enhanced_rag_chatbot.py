from shared_functions import *
from typing import List, Dict, Any
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai.foundation_models import ModelInference
import json
from dotenv import load_dotenv
import os

load_dotenv()

# > Global variables
food_items = []

# IBM Watsonx.ai Configuration
my_credentials = {
    "url": "https://jp-tok.ml.cloud.ibm.com",
    "apikey": os.getenv("API_KEY")
}

model_id = 'ibm/granite-3-8b-instruct'
gen_parms = {"max_new_tokens": 400}
project_id = os.getenv("PROJECT_ID")
space_id = None
verify = False

# > Initialize the LLM model
model = ModelInference(
    model_id=model_id,
    credentials=my_credentials,
    params=gen_parms,
    project_id=project_id,
    space_id=space_id,
    verify=verify
)

# > Test Watsonx LLM connection
result = model.generate(prompt="Hello")
print("\nResult:")
print(result['results'][0]['generated_text'])

print("\n --- working ---")