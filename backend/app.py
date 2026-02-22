from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
latest_value = None

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Telemetry(BaseModel):
    value: int

@app.post("/api/telemetry")
async def main(data: Telemetry):
    global latest_value
    latest_value = data.value
    return {"status": "ok"}

@app.get("/api/latest")
async def get_latest():
    return {"value": latest_value}
