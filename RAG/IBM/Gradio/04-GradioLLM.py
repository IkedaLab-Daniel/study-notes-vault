from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai import Credentials
from langchain_ibm import WatsonxLLM
import gradio as gr
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# > Model and project settings
model_id = 'ibm/granite-3-8b-instruct'
# > Set necessary parameters
parameters = {
    GenParams.MAX_NEW_TOKENS: 256,
    GenParams.TEMPERATURE: 0.5
}

# > Wrap up model into WatsonxLLM interface
watsonx_llm = WatsonxLLM(
    model_id=model_id,
    url= "https://jp-tok.ml.cloud.ibm.com",
    project_id= os.getenv("PROJECT_ID"),
    params=parameters,
    apikey= os.getenv("API_KEY")
)

# > Function to generate a response from the model
def generate_response(prompt):
    generate_response = watsonx_llm.invoke(prompt)
    return generate_response

# > Create Gradio interface
chat_application = gr.Interface(
    fn=generate_response,
    allow_flagging="never",
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Type your questions here"),
    outputs=gr.Textbox(label="Output"),
    title="Watsonx.ai Chatbot (by Ice)",
    description="Ask any questions and the chatbot willl try to answer"
)

# > Launch the app
chat_application.launch(server_name="127.0.0.1", server_port=7860)