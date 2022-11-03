import asyncio
from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .redis_client import redis_client

app = FastAPI(title="MR Score Follower")
CURRENT_LOCATION = 1


async def update_location():
    while True:
        redis_client.set("loc", 2)
        await asyncio.sleep(5)
        redis_client.set("loc", 1)
        await asyncio.sleep(5)


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
    value = redis_client.get("loc") or CURRENT_LOCATION
    return {"loc": value}


if __name__ == "__main__":
    asyncio.run(update_location())
    # update_location()
