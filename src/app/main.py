from fastapi import FastAPI
import uvicorn

from app.api import ping

app = FastAPI()

app.include_router(ping.router)

if __name__ == "__main__":
    uvicorn.run("main:app")