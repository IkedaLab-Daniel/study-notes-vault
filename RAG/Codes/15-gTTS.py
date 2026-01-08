from ibm_watsonx_ai import Credentials, APIClient
from dotenv import load_dotenv
from utils import print_agent
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

model_id = 'mistralai/mistral-medium-2505'

# > --- Defining model parameters
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams

params = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 1000,
}

model = ModelInference(
    model_id=model_id,
    credentials=credentials,
    project_id=PROJECT_ID,
    params=params,
)

# > Generate a story with Mistral
def generate_story(topic):
    prompt = f"""Write an engaging and educational story about {topic} for beginners. 
            Use simple and clear language to explain basic concepts. 
            Include interesting facts and keep it friendly and encouraging. 
            The story should be around 200-300 words and end with a brief summary of what we learned. 
            Make it perfect for someone just starting to learn about this topic."""
    
    # > Generate text using the model
    response = model.generate_text(prompt=prompt)
    return response

def test_gen():
    topic = input("Enter topic for the story to generate: ")
    story = generate_story(topic)
    if story:
        print_agent()
        print(f""" 
|-----------------------------------------------------------|
>> {story}
|-----------------------------------------------------------|
""")
        
test_gen()