# modules/storyboard_generator.py

import replicate
import os
import requests
from dotenv import load_dotenv

load_dotenv()
os.environ["REPLICATE_API_TOKEN"] = os.getenv("REPLICATE_API_TOKEN")

def generate_storyboard_image(prompt: str, output_path: str):
    output = replicate.run(
        "stability-ai/sdxl:db21e45f8c84e4a0aef44c5765d66009f962f8f5c219d13789aab38b0d3d95c2",
        input={
            "prompt": prompt,
            "width": 1024,
            "height": 1024,
            "num_inference_steps": 30,
            "guidance_scale": 7.5,
        }
    )

    image_url = output[0]
    response = requests.get(image_url)
    with open(output_path, "wb") as f:
        f.write(response.content)
