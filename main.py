
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    prompt = data.get("prompt", "a flower fairy")
    size = data.get("size", "1024x1024")
    return JSONResponse(content={"response": f"Generated image with prompt: '{prompt}' and size: '{size}'"})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=10000)
