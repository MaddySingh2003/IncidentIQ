from fastapi import FastAPI
from app.api.routes.health import router as health_router
from app.api.routes.incidents import router as incident_router
from app.api.routes.logs import router as logs_router
from app.api.routes.analytics import router as analytics_router
from app.api.routes.clusters import router as clusters_router
from app.api.routes.analysis import router as analysis_router

app = FastAPI(
    title="INCIDENTIQ API",
    description="AI-Powered Incident Intelligence Platform",
    version="0.1.0",
)
app.include_router(analysis_router, prefix="/api")

app.include_router(logs_router, prefix="/api")

app.include_router(health_router, prefix="/api")
app.include_router(incident_router, prefix="/api")
app.include_router(analytics_router, prefix="/api")
app.include_router(clusters_router, prefix="/api")


@app.get("/")
def root():
    return {
        "message": "INCIDENTIQ backend is running",
        "status": "healthy",
    }