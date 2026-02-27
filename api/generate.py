from fastapi import FastAPI, Request
import requests
import os

app = FastAPI()

GPU_SERVER = "https://your-runpod-endpoint"

@app.post("/generate")
async def generate(req: Request):

    data = await req.json()

    response = requests.post(
        f"{GPU_SERVER}/sdapi/v1/txt2img",
        json={
            "prompt": data["prompt"],
            "steps": 20,
            "width": 512,
            "height": 512
        }
    )

    return response.json()
