import torch
from diffusers import FluxPipeline
from huggingface_hub import login
from config import HF_TOKEN, MODEL_ID, DEVICE, TORCH_DTYPE, GUIDANCE_SCALE, NUM_INFERENCE_STEPS, MAX_SEQUENCE_LENGTH

if HF_TOKEN:
    login(token=HF_TOKEN, add_to_git_credential=True)

pipe = FluxPipeline.from_pretrained(
    MODEL_ID,
    torch_dtype=getattr(torch, TORCH_DTYPE),
    use_auth_token=HF_TOKEN  # Ensure authentication for private models
).to(DEVICE)

def generate_image(prompt: str, seed: int = 0):
    generator = torch.Generator(device=DEVICE).manual_seed(seed)

    # Generate image
    image = pipe(
        prompt,
        guidance_scale=GUIDANCE_SCALE,
        num_inference_steps=NUM_INFERENCE_STEPS,
        max_sequence_length=MAX_SEQUENCE_LENGTH,
        generator=generator
    ).images[0]

    image_path = "output.png"
    image.save(image_path)
    return image_path
