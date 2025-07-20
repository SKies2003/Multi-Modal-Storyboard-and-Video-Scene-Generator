# modules/script_generator.py

import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

def generate_script(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    body = {
        "model": "openai/gpt-3.5-turbo",  # or try "mistralai/mixtral-8x7b"
        "messages": [
            {"role": "system", "content": "You are a movie scriptwriter."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)

    if response.status_code != 200:
        raise Exception(f"OpenRouter API error: {response.status_code}\n{response.text}")

    return response.json()["choices"][0]["message"]["content"]
