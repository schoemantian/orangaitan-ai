import requests
import openai
from config import (
    OPENAI_API_KEY,
)

openai.api_key = OPENAI_API_KEY

DALLE_API_URL = "https://api.openai.com/v1/images/generations"

def generate_image_response(prompt):
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "image-alpha-001",
        "prompt": prompt,
        "num_images": 1,
        "size": "256x256",
    }

    response = requests.post(DALLE_API_URL, json=data, headers=headers)
    if response.status_code == 200:
        image_url = response.json()["data"][0]["url"]
        return {"text": image_url}
    else:
        return {"text": "Error generating image."}