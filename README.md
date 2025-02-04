# MixArt 2.0: Next-Gen Generative Artwork with SDXL & ControlNet

![MixArt 2.0](https://your-image-link-here.com)

## 🚀 Overview
MixArt 2.0 is an advanced generative art pipeline leveraging **Stable Diffusion XL (SDXL)** for high-fidelity abstract and photorealistic artwork. By integrating **ControlNet** and **T2I-Adapter**, the pipeline provides precise user-guided generation, allowing artists and designers to maintain structural consistency while enabling creative freedom.

Personalization is enhanced through **DreamBooth fine-tuning**, ensuring unique and customized visual content generation. Optimized with **Torch 2.0, FlashAttention, and ONNX Runtime**, MixArt 2.0 delivers accelerated inference on modern GPUs, making high-quality AI-generated art accessible and efficient.

## ✨ Features
- **High-Fidelity Image Generation**: Uses **SDXL** for superior detail in abstract and photorealistic artwork.
- **ControlNet & T2I-Adapter**: Enables fine-grained control over structure and composition.
- **DreamBooth Fine-Tuning**: Personalize models with user-defined styles for unique artwork.
- **Optimized Inference**: Leverages **Torch 2.0, FlashAttention, and ONNX Runtime** for faster processing.
- **FastAPI Integration**: Provides a RESTful API for seamless interaction and image generation.

## 🛠️ Installation
### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- PyTorch 2.0+
- CUDA-compatible GPU (optional, but recommended)
- Hugging Face account for model authentication

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/sabdulrahman/MixArt.git
   cd MixArt
   ```
2. **Create a virtual environment and install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. **Set up environment variables:**
   Create a `.env` file and add your Hugging Face API token:
   ```bash
   HF_TOKEN=your_huggingface_token
   ```

## 🎨 Usage
### Running the API
1. **Start the FastAPI server:**
   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```
2. **Generate an image via API:**
   ```bash
   curl -X POST "http://localhost:8000/generate/" \
        -H "Content-Type: application/json" \
        -d '{
            "prompt": "A futuristic city skyline at sunset",
            "width": 512,
            "height": 512,
            "guidance_scale": 7.5,
            "steps": 20
        }'
   ```

### Running the Inference Script
To generate an image locally:
```bash
python inference.py --prompt "A surreal dreamscape with floating islands"
```

## ⚡ Optimization
- **Memory Efficiency**: Enabled attention slicing to fit low-VRAM GPUs.
- **Fast Processing**: Utilizes FlashAttention for speed improvements.
- **ONNX Runtime**: Deploy models with optimized execution for better inference performance.

## 📂 Project Structure
```
MixArt2.0/
│── config.py          # Configuration settings
│── inference.py       # Image generation pipeline
│── main.py            # FastAPI backend for serving images
│── requirements.txt   # Dependencies
│── .env               # Environment variables (not included in repo)
│── README.md          # Project documentation
```


## 💡 Future Enhancements
- ✅ Add **LoRA support** for fine-tuning on limited datasets
- ✅ Integrate **web-based UI** for interactive generation
- ✅ Support **multi-modal input** (text + sketches)

## 🤝 Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

