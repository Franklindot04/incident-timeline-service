from fastapi import APIRouter
from app.models.incident import Incident
from app.core.validation import validate_incident

router = APIRouter()

# temporary in-memory store
INCIDENTS = []

@router.post("/")
def create_incident(incident: Incident):
    validate_incident(incident)
    INCIDENTS.append(incident)
    return {"message": "Incident created", "incident": incident}

@router.get("/")
def list_incidents():
    return INCIDENTS
