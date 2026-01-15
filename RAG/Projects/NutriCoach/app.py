import requests
import re
import base64
import os
from dotenv import load_dotenv
from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai import APIClient
from ibm_watsonx_ai.foundation_models import Model, ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames
from PIL import Image
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
load_dotenv()

### --- Step 2 --- ###
credentials = Credentials(
    url = os.getenv('URL'),
    api_key=os.getenv('API_KEY')
)

client = APIClient(credentials)

model_id = "meta-llama/llama-4-maverick-17b-128e-instruct-fp8"
project_id = os.getenv('PROJECT_ID')
params = TextChatParameters()

model = ModelInference(
    model_id=model_id,
    credentials=credentials,
    project_id=project_id,
    params=params
)

### --- Step 3 --- ###
def input_image_setup(uploaded_file):
    """
    Encodes the uploaded image file into a base64 string to be used with AI models.
    Parameters:
    - uploaded_file: File-like object uploaded via a file uploader (Streamlit or other frameworks)
    Returns:
    - encoded_image (str): Base64 encoded string of the image data
    """
    # ? Check if a file has been uploaded
    if uploaded_file is not None:
        # ? Read the file into bytes
        bytes_data = uploaded_file.read()

        # ? Encode the image to a base64 string
        encoded_image = base64.b64encode(bytes_data).decode("utf-8")

        return encoded_image
    else:
        raise FileNotFoundError("No file upload")
    
### Step 4
### Step 5
@app.route('/generate', methods=['POST'])
def index():
    # This is where you'll add your main application logic later, after step 5
    #TODO
    pass

if __name__ == '__main__':
    app.run(debug=True)