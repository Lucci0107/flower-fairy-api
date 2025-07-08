from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.post("/greta-webhook")
async def greta_webhook(request: Request):
    data = await request.json()

    style = data.get("style", "pastel")
    pose = data.get("pose", "floating gracefully")
    background = data.get("background", "enchanted forest")
    lighting = data.get("lighting", "soft morning light")
    effect = data.get("effect", "sparkles and glow")
    character_type = data.get("character_type", "flower")

    prompt = f"A highly detailed miniature figurine in {style} style, posing as '{{pose}}', with background '{{background}}', lighting as '{{lighting}}', and effect '{{effect}}'. The character is a {{character_type}} fairy with wings and floral decorations."

    response = openai.Image.create(
        model="dall-e-3",
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response["data"][0]["url"]

    return {"image_url": image_url, "prompt": prompt}
