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
import torch
from transformers import pipeline

pipe = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-tiny.en",
    chunk_length_s=30,
)

# sample = 'sample-meeting.wav'
sample = 'sample_audio.mp3'

# ? Perform speech recognition on the audio file
prediction = pipe(sample, batch_size=8)["text"]

if prediction:
    print("\033[92m\nOK ( ˶ˆᗜˆ˵ ) >> Audio successfully transcribed: \033[0m")
    print(prediction)
else:
    print("\033[91m\nERROR (╥﹏╥) >> Failed to transcribe audio sample\033[0m")

print("\033[92mEND (ᵔ ᵕ ᵔ˶)\033[0m")