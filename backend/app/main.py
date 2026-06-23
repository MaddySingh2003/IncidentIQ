from fastapi import FastAPI
from app.api.routes.health import router as health_router

app = FastAPI(
    title="SentinelRCA API",
    description="AI-Powered Incident Intelligence Platform",
    version="0.1.0",
)

app.include_router(health_router, prefix="/api")


@app.get("/")
def root():
    return {
        "message": "SentinelRCA backend is running",
        "status": "healthy",
    }