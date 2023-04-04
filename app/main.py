from fastapi import FastAPI
from fastapi.middleware.gzip import GZipMiddleware

from app.ui import init

app = FastAPI()

app.add_middleware(GZipMiddleware, minimum_size=1000)


@app.on_event("startup")
async def startup():
    init(app)
