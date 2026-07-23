from fastapi import APIRouter

from app.services.llm.llm_service import LLMService

router=APIRouter(
    prefix="/incidents",
    tags=["AI Analysis"]
)

@router.post("/{incident_id}/analyze")
async def analyze_incident(incident_id:str):
    return await LLMService.analyze(incident_id)