import gradio as gr
import requests

API_URL = "http://localhost:8000/generate/"

def generate_image_ui(prompt, negative_prompt, width, height, guidance_scale, steps):
    response = requests.post(API_URL, json={
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "width": width,
        "height": height,
        "guidance_scale": guidance_scale,
        "steps": steps
    })
    result = response.json()
    return result["image_path"]

with gr.Blocks() as demo:
    gr.Markdown("## MixArt 2.0 - AI Generated Artwork")
    
    prompt = gr.Textbox(label="Prompt", placeholder="Describe your image")
    negative_prompt = gr.Textbox(label="Negative Prompt", placeholder="What to avoid")
    width = gr.Slider(512, 1024, step=64, value=1024, label="Width")
    height = gr.Slider(512, 1024, step=64, value=1024, label="Height")
    guidance_scale = gr.Slider(1.0, 15.0, step=0.5, value=7.5, label="Guidance Scale")
    steps = gr.Slider(10, 100, step=5, value=50, label="Sampling Steps")

    generate_button = gr.Button("Generate Image")
    output_image = gr.Image()

    generate_button.click(generate_image_ui, inputs=[prompt, negative_prompt, width, height, guidance_scale, steps], outputs=output_image)

demo.launch()
