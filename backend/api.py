from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import router
from .database import init_models

app = FastAPI()
app.include_router(router.router)

origins = ["http://localhost:8080", "http://localhost"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def on_startup():
    await init_models()
