from fastapi import FastAPI
# from router.
from app.router.service import service_router
app = FastAPI(description="Service API", version="0.0.1")

app.include_router(service_router)

