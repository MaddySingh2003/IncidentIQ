from fastapi import APIRouter, HTTPException

from app.schemas.incident import IncidentCreate
from app.services.incident_service import IncidentService

router = APIRouter(
    prefix="/incidents",
    tags=["Incidents"]
)


@router.post("")
async def create_incident(incident: IncidentCreate):

    return await IncidentService.create_incident(incident)


@router.get("")
async def get_incidents():

    return await IncidentService.get_all_incidents()


@router.get("/{incident_id}")
async def get_incident(incident_id: str):

    incident = await IncidentService.get_incident(incident_id)

    if incident is None:
        raise HTTPException(
            status_code=404,
            detail="Incident not found"
        )

    return incident