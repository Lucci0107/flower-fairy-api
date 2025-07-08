from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class FairyRequest(BaseModel):
    style: str
    pose: str
    background: str
    lighting: str
    effect: str
    character_type: str

@app.post("/generate")
async def generate_image(request: FairyRequest):
    # Dummy image generation logic
    prompt = (
        f"A highly detailed miniature figurine in {request.style} style, "
        f"posing as '{request.pose}', with background '{request.background}', "
        f"lighting as '{request.lighting}', and effect '{request.effect}'. "
        f"The character is a {request.character_type} fairy with wings and floral decorations."
    )
    return JSONResponse(content={
        "image_url": "https://example.com/generated-image.png",
        "prompt": prompt
    })

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)