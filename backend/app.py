from typing import Dict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
latest_telemetry: Dict[str, dict] = {}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Telemetry(BaseModel):
    room_id: str
    sensor_type: str
    value: float
    unit: str
    status: str
    timestamp: str


@app.post("/api/telemetry")
async def receive_telemetry(data: Telemetry):
    sensor_key = f"{data.room_id}:{data.sensor_type}"
    latest_telemetry[sensor_key] = data.model_dump()
    return {"status": "ok"}


@app.get("/api/latest")
async def get_latest():
    items = sorted(
        latest_telemetry.values(),
        key=lambda item: (item["room_id"], item["sensor_type"]),
    )
    return {"items": items}
