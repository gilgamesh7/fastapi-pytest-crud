from fastapi import FastAPI
import uvicorn

from app.api import ping
from app.db import engine, database, metadata

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
    
app.include_router(ping.router)

if __name__ == "__main__":
    uvicorn.run("main:app")