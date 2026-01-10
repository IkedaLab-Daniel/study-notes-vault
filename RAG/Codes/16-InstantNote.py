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


iface.launch(server_name="0.0.0.0", server_port=5005)
