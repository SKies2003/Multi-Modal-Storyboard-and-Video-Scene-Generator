from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # ✅ Load environment variables from .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_script(story_prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # switch from gpt-4 if necessary
        messages=[
            {"role": "system", "content": "You are a scriptwriter. Turn the prompt into a scene-by-scene movie script."},
            {"role": "user", "content": story_prompt}
        ]
    )
    return response.choices[0].message.content.strip()
