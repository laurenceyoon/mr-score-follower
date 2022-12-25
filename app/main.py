import asyncio
from http import HTTPStatus
import time

from fastapi import FastAPI, WebSocket
from fastapi.responses import RedirectResponse

from .redis_client import redis_client
from .core.helper import start_performance_following
from fastapi import BackgroundTasks

app = FastAPI(title="MR Score Follower")
CURRENT_LOCATION = 1


@app.get("/", tags=["Basic API"])
def root():
    return RedirectResponse("/docs")

# Test APIs
@app.get("/test", tags=["Test"])
def test():
    print("test API for synchronous request")
    return {"hello": "world"}


@app.get("/async-test", tags=["Test"])
async def async_test():
    print("test API for asynchronous request - sleep for 0.1 sec...")
    await asyncio.sleep(0.1)
    return {"async hello": "world"}


@app.get("/redis-test", tags=["Test"])
def redis_test(value: float = 1):
    redis_client.set("key", value)
    value = redis_client.get("key")
    return {"key": value}


@app.get("/current", tags=["Basic API"])
def current_location():
    value = redis_client.get("location") or CURRENT_LOCATION
    # if int(value) == 264:
    #     value = 0
    return float(value)


@app.get(
    "/follow",
    status_code=HTTPStatus.ACCEPTED,
    tags=["Basic API"],
)
def follow_piece(background_tasks: BackgroundTasks):
    piece = "./resources/bwv66.6_full.wav"
    
    background_tasks.add_task(start_performance_following, piece_path=piece)
    return {"response": f"following"}


@app.websocket(
    "/ws",
)
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("websocket accept")
    piece = "./resources/bwv66.6_full.wav"
    # asyncio.ensure_future(start_performance_following)
    while True:
        value = int(redis_client.get("location") or CURRENT_LOCATION)
        print(f"value? {value}")
        await websocket.send_text(f"{value}")
        await asyncio.sleep(3)
        print(f"sent!!")
