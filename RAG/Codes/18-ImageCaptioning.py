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