from ibm_watsonx_ai import Credentials, APIClient
from dotenv import load_dotenv
import os

load_dotenv()

credentials = Credentials(
    url=os.getenv("URL"),
    api_key=os.getenv("API_KEY"),
)

PROJECT_ID = os.getenv("PROJECT_ID")

client = APIClient(credentials)

# > GET TextModels ENUM
client.foundation_models.TextModels

# > PRINT doct of Enums
# client.foundation_models.TextModels.show()

### --- Image Preparation --- ###
# url_image_0 = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQwi1tt9wRKB9WFZV2JVO_y9kU_Db9Sb5atdw&s'
url_image_0 = 'https://media.tenor.com/FI9CZRTgweMAAAAe/lain-lain-iwakura.png'
url_image_1 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/5uo16pKhdB1f2Vz7H8Utkg/image-1.png'
url_image_2 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/fsuegY1q_OxKIxNhf6zeYg/image-2.png'
url_image_3 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/KCh_pM9BVWq_ZdzIBIA9Fw/image-3.png'
url_image_4 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/VaaYLw52RaykwrE3jpFv7g/image-4.png'

image_urls = [url_image_0, url_image_1, url_image_2, url_image_3, url_image_4] 

### --- Watsonx.AI --- ###
# ! model_id = 'ibm/granite-vision-3-2-2b'      --- Model 'ibm/granite-vision-3-2-2b' is not supported for this environment
model_id = 'meta-llama/llama-3-2-11b-vision-instruct'   # ? Alternative model


from ibm_watsonx_ai.foundation_models.schema import TextChatParameters
# TextChatParameters.show()

params = TextChatParameters(
    temperature=0.2,
    top_p=0.5,
)

# print(params)

# > Initalize the Model
from ibm_watsonx_ai.foundation_models import ModelInference

model = ModelInference(
    model_id=model_id,
    credentials=credentials,
    project_id=PROJECT_ID,
    params=params
)

### --- Encode the Image --- ###
import base64
import requests

def encode_image_to_base64(image_urls):
    """
    Downloads and encodes a list of image URLs to base64 strings.

    Parameters:
    - image_urls (list): A list of image URLs.

    Returns:
    - list: A list of base64-encoded image strings.
    """
    encoded_images = []

    for url in image_urls:
        response = requests.get(url)
        if response.status_code == 200:
            encoded_image = base64.b64encode(response.content).decode("utf-8")
            encoded_images.append(encoded_image)
            print(type(encoded_image))
        else:
            print(f"Warning: Failed to fetch image from {url} (Status code: {response.status_code})")
            encoded_images.append(None)

    return encoded_images

encoded_images = encode_image_to_base64(image_urls)

def generate_model_response(encoded_image, user_query, assistant_prompt="You are a helpful assistant. Answer the following user query in 1 or 2 sentences: "):
    """
    Sends an image and a query to the model and retrieves the description or answer.

    Parameters:
    - encoded_image (str): Base64-encoded image string.
    - user_query (str): The user's question about the image.
    - assistant_prompt (str): Optional prompt to guide the model's response.

    Returns:
    - str: The model's response for the given image and query.
    """

    # ? Create the message object
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": assistant_prompt + user_query
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "data:image/jpeg;base64," + encoded_image,
                    }
                }
            ]
        }
    ]

    # ? send the request to the model
    response = model.chat(messages=messages)

    # ? return the model's response
    return response['choices'][0]['message']['content']

user_query = "Describe the photo"

for i in range(len(encoded_images)):
    image = encoded_images[i]

    response = generate_model_response(image, user_query)

    # > print response
    print(f"Description for image {i + 1}: {response}\n\n")


print(" --- End --- ")
