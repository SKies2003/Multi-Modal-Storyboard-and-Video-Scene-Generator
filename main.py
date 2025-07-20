# main.py
import os
from config import *
from modules.script_generator import generate_script
from modules.storyboard_generator import generate_storyboard_image
from modules.video_generator import generate_video_from_image

def extract_scenes(script: str):
    scenes = []
    paragraphs = script.split("\n\n")
    for para in paragraphs:
        if any(tag in para.upper() for tag in ["EXT.", "INT."]) or "FIGURE" in para.upper() or "LOCKET" in para.lower():
            scenes.append(para.strip())
    return scenes[:3]  # Limit to first 3 key scenes

def main():
    os.makedirs(OUTPUT_SCRIPT_DIR, exist_ok=True)
    os.makedirs(OUTPUT_STORYBOARD_DIR, exist_ok=True)
    os.makedirs(OUTPUT_VIDEO_DIR, exist_ok=True)

    story_idea = input("Enter your story idea: ")
    
    script = generate_script(story_idea)
    script_path = os.path.join(OUTPUT_SCRIPT_DIR, "script.txt")
    with open(script_path, 'w') as f:
        f.write(script)

    scenes = extract_scenes(script)

    for i, scene in enumerate(scenes):
        img_path = os.path.join(OUTPUT_STORYBOARD_DIR, f"scene_{i+1}.png")
        vid_path = os.path.join(OUTPUT_VIDEO_DIR, f"scene_{i+1}.mp4")

        print(f"Generating storyboard for Scene {i+1}")
        generate_storyboard_image(scene, img_path)

        print(f"Generating video for Scene {i+1}")
        generate_video_from_image(img_path, vid_path)

    print("Pipeline completed.")

if __name__ == "__main__":
    main()
