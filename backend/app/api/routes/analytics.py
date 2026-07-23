from fastapi import APIRouter
from app.services.analytics_service import AnalyticsService


router=APIRouter(
    prefix="/incidents",
    tags=["Analytics"]
)


@router.get("/{incident_id}/analytics")
async def analytics(incident_id:str):
    return await AnalyticsService.get_incident_analytics(incident_id)
