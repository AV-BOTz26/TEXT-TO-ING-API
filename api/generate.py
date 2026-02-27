from fastapi import FastAPI
import requests

app = FastAPI()

GPU_SERVER = "https://text-to-ing-api.vercel.app"

@app.get("/")
def home():
    return {"status": "API Working"}

@app.post("/")
async def generate(data: dict):

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
