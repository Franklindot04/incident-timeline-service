from pydantic import BaseModel, Field
from datetime import datetime


class Incident(BaseModel):
    id: int = Field(..., gt=0)
    title: str = Field(..., min_length=3)
    severity: str = Field(..., pattern="^(low|medium|high|critical)$")
    created_at: datetime = Field(default_factory=datetime.utcnow)
