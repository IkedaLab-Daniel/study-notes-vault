from openai import OpenAI
import requests
client = OpenAI()

response = client.images.generate(
    model="dall-e-2",
    prompt="a white siamese cat",
    size="1024x1024",
    n=1
)

url = response.data[0].url

# Download and save the image
image_data = requests.get(url).content
with open("generated_image.png", "wb") as f:
    f.write(image_data)

print(f"Image saved as 'generated_image.png'")