# Multi-Modal-Storyboard-and-Video-Scene-Generator

An end-to-end creative pipeline that transforms a simple story idea into a visual storyboard and short video scenes.

## Key features

1. Takes a high-level text prompt (e.g., "a detective discovering a clue in a rainy city at night").
2. Uses an LLM for scripting to generate a detailed script with scene descriptions and character actions.
3. For each scene in the script, use a text-to-image model (e.g., Midjourney, DALL-E 3) to generate a key storyboard image.
4. Use an image-to-video or text-to-video model (e.g., Stable Video Diffusion, Pika) to generate a short, 3-5 second video clip for each scene.
