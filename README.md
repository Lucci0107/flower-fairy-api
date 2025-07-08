# Flower Fairy Image Generator API

This is a FastAPI application for generating flower fairy images via OpenAI API.

## Endpoint

POST `/generate`

### Request JSON
```
{
  "style": "pastel",
  "pose": "floating gracefully",
  "background": "enchanted forest",
  "lighting": "soft morning light",
  "effect": "sparkles and glow",
  "character_type": "flower"
}
```

### Response JSON
```
{
  "image_url": "https://...",
  "prompt": "..."
}
```
