from pydantic import BaseModel
from datetime import datetime


class LogCreate(BaseModel):
    incident_id: str
    timestamp:str
    level: str
    service: str
    message: str
    raw_log: str
    normalized_log: str
    created_at: datetime