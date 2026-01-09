import requests
# > --- Step 1: Speech-to-Text --- < #
def download_sample_audio():
    # ? URL of the audio file to be downloaded
    audio_file_path = "sample-meeting.wav"
    url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/hTqGqoC-LrW6S79HjuJUkg/trimmed-02.wav"

    # ? Check if audio exist first
    try:
        with open(audio_file_path, "r") as file:
            print("\033[92m\nOK ( ˶ˆᗜˆ˵ ) >> Sample audio already exist on this folder.")
            return
    except:
        response = requests.get(url)

        if response.status_code == 200:
            with open(audio_file_path, "wb") as file:
                file.write(response.content)
                print("\033[92m\nOK ( ˶ˆᗜˆ˵ ) >> File downloaded successfully")
        else:
            print("\033[91m\nERROR (╥﹏╥) >> Failed to download file")

download_sample_audio()