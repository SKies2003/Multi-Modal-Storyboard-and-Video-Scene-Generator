# modules/video_generator.py
import os

def generate_video_from_image(image_path: str, output_path: str):
    # Using Stable Video Diffusion CLI
    os.system(f"stable-video-diffusion --input {image_path} --output {output_path} --num_frames 75")
