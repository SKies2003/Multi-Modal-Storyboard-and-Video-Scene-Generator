# modules/storyboard_generator.py

import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_storyboard_image(prompt: str, output_path: str):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "stability/stable-diffusion-xl",  # alternative: "openai/dall-e-3"
        "prompt": prompt
    }

    response = requests.post("https://openrouter.ai/api/v1/images/generations", headers=headers, json=data)

    if response.status_code != 200:
        raise Exception(f"Image generation error: {response.status_code}\n{response.text}")

    image_url = response.json()["data"][0]["url"]

    os.system(f"curl -L '{image_url}' -o {output_path}")
