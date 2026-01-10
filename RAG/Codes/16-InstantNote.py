import requests
# > --- Step 1: Speech-to-Text --- < #
def download_sample_audio():
    # ? URL of the audio file to be downloaded
    audio_file_path = "sample-meeting.wav"
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/hTqGqoC-LrW6S79HjuJUkg/trimmed-02.wav"

    # ? Check if audio exist first
    try:
        with open(audio_file_path, "r") as file:
            print("\033[92m\nOK ( ˶ˆᗜˆ˵ ) >> Sample audio already exist on this folder.\033[0m")
            return
    except:
        response = requests.get(url)

        if response.status_code == 200:
            with open(audio_file_path, "wb") as file:
                file.write(response.content)
                print("\033[92m\nOK ( ˶ˆᗜˆ˵ ) >> File downloaded successfully\033[0m")
        else:
            print("\033[91m\nERROR (╥﹏╥) >> Failed to download file\033[0m")

download_sample_audio()

# > Implement OpenAI Whisper for transcribing
from transformers import pipeline

def transcript_audio(audio_file):
    pipe = pipeline(
        "automatic-speech-recognition",
        model="openai/whisper-tiny.en",
        chunk_length_s=30,
    )

    # ? Perform speech recognition on the audio file
    prediction = pipe(audio_file, batch_size=8)["text"]

    if prediction:
        print("\033[92m\nOK ( ˶ˆᗜˆ˵ ) >> Audio successfully transcribed: \033[0m")
        print(prediction)
        return prediction
    else:
        print("\033[91m\nERROR (╥﹏╥) >> Failed to transcribe audio sample\033[0m")
        return "Error transcribing the audio"

# > Set up Gradio interface < #
import gradio as gr

iface = gr.Interface(
    fn=transcript_audio,
    inputs=gr.Audio(
        sources=["microphone", "upload"],
        type="filepath"
    ),
    outputs=gr.Textbox(),
    title="Audio Transcription App",
    description="Upload an audio file to transcribe it to text",
    api_name=False,
)

# iface.launch(server_name="0.0.0.0", server_port=5005)

# > Integrating LLM using IBM watsonx Granite
from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes # ? Specifying model types
from ibm_watsonx_ai import APIClient, Credentials # ? for client and credentials parameters
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParam # ? For managing model parameters
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods # ? for defining decoding methods
from langchain_ibm import WatsonxLLM, WatsonxEmbeddings # ? For interacting with IBM's LLM and embedding
from ibm_watsonx_ai.foundation_models.utils import get_embedding_model_specs # ? for retrieving model specification
from langchain.chains import LLMChain # ? For creating chains of operations with LLMs
from langchain.prompts import PromptTemplate # ? For defining prompt templates
from dotenv import load_dotenv
import os
load_dotenv()

parameters = {
    GenParam.DECODING_METHOD: "sample",
    GenParam.MAX_NEW_TOKENS: 512,
    GenParam.MIN_NEW_TOKENS: 1,
    GenParam.TEMPERATURE: 0.5,
    GenParam.TOP_K: 50,
    GenParam.TOP_P: 1,
}

model_id = 'ibm/granite-3-8b-instruct' # !'ibm/granite-3-3-8b-instruct' (not available on free tier (╥﹏╥))
project_id = os.getenv("PROJECT_ID")

granite_llm = WatsonxLLM(
    model_id=model_id,
    url=os.getenv("URL"),
    project_id=project_id,
    params=parameters,
    apikey=os.getenv("API_KEY"),
)

def test_llm_integration():
    query = input("Testing granite LLM integration | Ask any question: ")
    response = granite_llm.invoke(query)

    print("\033[92m\nOK ( ˶ˆᗜˆ˵ ) >> LLM integration confirmed. Response: ")
    print(response)

def clean_up_with_llm(generated_transcript):
    system_prompt = """You are an intelligent assistant tasked with processing spoken or written transcripts. Your job is to ensure that all domain-specific terms, abbreviations, and acronyms are presented in a clear and standardized format.

For each term that is commonly abbreviated as an acronym, spell out the full term followed by the acronym in parentheses the first time it appears. For example, “REM” should be transformed to “Rapid Eye Movement (REM)”, and “API” should be transformed to “Application Programming Interface (API)”.

If numbers or terms are spoken aloud and represent a specific named concept, convert them into their standard numeric or formal representation, followed by the full name in parentheses when appropriate. For example, “seven to nine hours” may remain as is, but “four zero one k” would be converted into its proper standardized form if it refers to a known concept.

Be aware that some acronyms or terms may have multiple meanings depending on context. You must determine the correct meaning based on surrounding content and apply the appropriate expansion. If a spoken number or phrase does not represent a specific named concept or standardized term, leave it unchanged.

Your task is to analyze the text, apply these transformations consistently, and ensure clarity without altering the original meaning or tone.

Once complete, output:

The adjusted transcript

A list of the words or phrases that were changed"""
    # Concatenate the system prompt and the user transcript
    prompt_input = system_prompt + "\n" + generated_transcript

    response = granite_llm.invoke(prompt_input)
    print("\033[92m\nNOT SURE ( ˶ˆᗜˆ˵ ) >> LLM Responded, but not sure if it does the job good. Check it out:")
    print(response)

# ? Clean up transcript usage
# generated_transcript = transcript_audio("generated_story.mp3")
# clean_up_with_llm(generated_transcript)


print("""\033[92m
  |-----------------|
  |    ( ˶ˆᗜˆ˵ )    |
  |     ~ end ~     |
  |-----------------|

\033[0m""")