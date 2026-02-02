from fastapi import FastAPI, BackgroundTasks
import time
import asyncio
import uvicorn

app = FastAPI()


def sync_task():
    time.sleep(3)
    print("Send email")


async def async_task():
    await asyncio.sleep(3)
    print("Request to another API")


@app.post("/")
async def route(bg_tasks: BackgroundTasks):
    # asyncio.create_task(async_task()) # кладём задачу в событиный цикл (для асинхронных функций)
    bg_tasks.add_task(sync_task)        # для синхронных фунцкий
    return {"ok": True}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
