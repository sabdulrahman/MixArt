import os
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

MODEL_ID = "black-forest-labs/FLUX.1-schnell"
DEVICE = "cuda"
TORCH_DTYPE = "bfloat16"
GUIDANCE_SCALE = 0.0
NUM_INFERENCE_STEPS = 4
MAX_SEQUENCE_LENGTH = 256

HOST = "0.0.0.0"
PORT = 8000

CACHE_DIR = os.getenv("CACHE_DIR", "./cache")
