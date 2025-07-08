from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class GenerateRequest(BaseModel):
    prompt: str
    size: str

@app.post("/generate")
async def generate_image(request: GenerateRequest):
    # 仮のレスポンス
    return {"response": f"Image generated for prompt: '{request.prompt}' with size: {request.size}"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000)