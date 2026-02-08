import requests
import base64
import os
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models import Model, ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters
from ibm_watsonx_ai.metanames import GenChatParamsMetaNames
load_dotenv()

from PIL import Image

### --- initializing the model --- ###
credentials = Credentials(
    url=os.getenv("URL"),
    api_key=os.getenv("API_KEY")
)
client = APIClient(credentials)

model_id = "meta-llama/llama-3-2-11b-vision-instruct"
project_id = os.getenv("PROJECT_ID")
params = TextChatParameters()

model = ModelInference(
    model_id=model_id,
    credentials=credentials,
    project_id=project_id,
    params=params
)

### --- Preparing an image for processing --- ###
def prepare_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_image

def prepare_image_from_url(image_url):
    response = requests.get(image_url)
    encoded_image = base64.b64encode(response.content).decode('utf-8')
    return encoded_image

### --- Creating the multimodal query function --- ###
def query_multimodal_model(encoded_image, user_question, system_prompt=""):
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": system_prompt + user_question
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "data:image/jpeg;base64," + encoded_image
                    }
                }
            ]
        }
    ]

    response = model.chat(messages=messages)

    return response['choices'][0]['message']['content']

image = prepare_image_from_url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwi1tt9wRKB9WFZV2JVO_y9kU_Db9Sb5atdw&s") # lain iwakura
question = "What can you see in this image?"
result = query_multimodal_model(image, question)

print(result)

print(" --- Working ---")