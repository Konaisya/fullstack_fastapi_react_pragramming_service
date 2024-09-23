from fastapi import FastAPI
# from router.
from app.router.service import service_router

app = FastAPI()

app.include_router(service_router)