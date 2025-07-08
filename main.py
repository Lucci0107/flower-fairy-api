from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    user_message = data.get("message", "")
    return {"response": f"🌸花の精霊を生成中にゃ：「{user_message}」🌸"}
