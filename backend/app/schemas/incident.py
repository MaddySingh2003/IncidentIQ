from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class IncidentCreate(BaseModel):
    title: str = Field(..., min_length=5, max_length=150)
    description: str
    service: str
    environment: str
    severity: str
    tags: List[str] = []
    affected_version: Optional[str] = None


class IncidentResponse(BaseModel):
    id: str
    title: str
    description: str
    service: str
    environment: str
    severity: str
    status: str
    tags: List[str]
    affected_version: Optional[str]
    created_at: datetime