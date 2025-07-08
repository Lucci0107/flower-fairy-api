
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import openai

app = FastAPI()

# CORS設定（任意）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI APIキーを環境変数から取得
openai.api_key = os.getenv("OPENAI_API_KEY")

# リクエスト用モデル
class FairyRequest(BaseModel):
    style: str
    pose: str
    background: str
    lighting: str
    effect: str
    character_type: str

# 画像生成エンドポイント
@app.post("/generate")
async def generate_image(req: FairyRequest):
    prompt = (
        f"A highly detailed miniature figurine in {req.style} style, "
        f"posing as '{req.pose}', with background '{req.background}', "
        f"lighting as '{req.lighting}', and effect '{req.effect}'. "
        f"The character is a {req.character_type} fairy with wings and floral decorations."
    )

    try:
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return {"image_url": image_url, "prompt": prompt}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
