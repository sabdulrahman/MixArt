from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from inference import generate_image
import uvicorn

app = FastAPI()

class ImageRequest(BaseModel):
    prompt: str
    negative_prompt: str = ""
    width: int = 1024
    height: int = 1024
    guidance_scale: float = 7.5
    steps: int = 50

@app.post("/generate/")
async def generate(request: ImageRequest):
    try:
        image_path = generate_image(
            prompt=request.prompt,
            negative_prompt=request.negative_prompt,
            width=request.width,
            height=request.height,
            guidance_scale=request.guidance_scale,
            steps=request.steps,
        )
        return {"image_path": image_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
