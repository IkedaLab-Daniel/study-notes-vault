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
client.foundation_models.TextModels.show()

### --- Image Preparation --- ###
url_image_1 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/5uo16pKhdB1f2Vz7H8Utkg/image-1.png'
url_image_2 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/fsuegY1q_OxKIxNhf6zeYg/image-2.png'
url_image_3 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/KCh_pM9BVWq_ZdzIBIA9Fw/image-3.png'
url_image_4 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/VaaYLw52RaykwrE3jpFv7g/image-4.png'

image_urls = [url_image_1, url_image_2, url_image_3, url_image_4] 

### --- Watsonx.AI --- ###
model_id = 'ibm/granite-vision-3-2-2b'

from ibm_watsonx_ai.foundation_models.schema import TextChatParameters
TextChatParameters.show()

params = TextChatParameters(
    temperature=0.2,
    top_p=0.5,
)

print(params)