# modules/storyboard_generator.py
import os
import openai

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_storyboard_image(scene_description: str, output_path: str):
    response = client.images.generate(
        model="dall-e-3",
        prompt=scene_description,
        size="1024x1024",
        n=1
    )
    image_url = response.data[0].url
    os.system(f"wget '{image_url}' -O {output_path}")
