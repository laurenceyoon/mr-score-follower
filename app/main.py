import asyncio
from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .redis import redis_client

app = FastAPI(title="MR Score Follower")

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
