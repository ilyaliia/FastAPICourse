import time

from fastapi import FastAPI, Request, Response

from typing import Callable

import uvicorn

app = FastAPI()


@app.middleware("http")
async def my_middleware(request: Request, call_next: Callable):
    ip_addres = request.client.host
    print(f"{ip_addres}")
    # if ip_addres in ["127.0.0.1", "localhost"]:
    #     return Response(status_code=429, content="Request limit")

    start = time.perf_counter()
    response = await call_next(request)
    end = time.perf_counter() - start
    print("Finish time: ", end)
    response.headers["X-Special"] = "I am special"
    return response


@app.get("/users")
async def get_users():
    time.sleep(0.5)
    return [{"id": 1, "name": "Ilya"}]

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
