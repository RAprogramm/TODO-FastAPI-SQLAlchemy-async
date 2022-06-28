from fastapi import FastAPI

from . import router
from .database import init_models

app = FastAPI()
app.include_router(router.router)


@app.on_event("startup")
async def on_startup():
    await init_models()
