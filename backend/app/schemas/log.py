from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class LogEntry(BaseModel):
    incident_id: str
    timestamp: Optional[datetime] = None
    service: str
    level: str
    raw_log: str
    normalized_log: Optional[str] = None
    created_at: datetime = datetime.utcnow()