from ibm_watsonx_ai import Credentials, APIClient
from dotenv import load_dotenv
import os

load_dotenv()
URL = os.getenv("URL")
API_KEY = os.getenv("API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")

credentials = Credentials(
    url=URL,
    api_key=API_KEY,
)

client = APIClient(credentials)
# > Get TextModels ENUM
client.foundation_models.TextModels

# > Print dict of Enums
client.foundation_models.TextModels.show()