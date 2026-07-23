from fastapi import APIRouter

from app.repositories.log_repository import LogRepository
from app.services.clustering_service import ClusteringService

router=APIRouter(
    prefix="/incidents",
    tags=["Clusters"]
)

@router.get("/{incident_id}/clusters")
async def clusters(incident_id:str):
    
    logs=await LogRepository.get_log_by_incidents(incident_id)
    return ClusteringService.cluster(logs)