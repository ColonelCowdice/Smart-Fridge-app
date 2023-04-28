import openai
import requests
from PIL import Image
from io import BytesIO
import weather

# Set up OpenAI API key
openai.api_key = "Enter API key here"

# Define image prompt
prompt = "Create an Advert for the city of" + weather.city

# Use OpenAI to generate textual description of image
result = openai.Completion.create(
    engine="text-davinci-002",
    prompt=f"Generate a textual description of an image of '{prompt}'",
    max_tokens=50,
    n=1,
    stop=None,
    temperature=0.5
)

# Extract textual description from OpenAI response
textual_description = result.choices[0].text.strip()

# Use DALL-E API to generate image based on textual description
response = requests.post(
    "https://api.openai.com/v1/images/generations",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    },
    json={
        "model": "image-alpha-001",
        "prompt": textual_description,
        "num_images": 1
    }
)

# Extract image data from response and display it
image_url = response.json()["data"][0]["url"]
image_data = requests.get(image_url).content
image = Image.open(BytesIO(image_data))

# Resize image to 500x500
image = image.resize((739, 550))

# Save the image as Ad.png
ad = 'Ad.png'
image.save(ad)
#image.show(ad)
