from fastapi import APIRouter
from app.models.incident import Incident
from app.core.validation import validate_incident
from app.db.sqlite import get_db, init_db

router = APIRouter()

init_db()

@router.post("/")
def create_incident(incident: Incident):
    validate_incident(incident)
    db = get_db()
    db["incidents"].insert({
        "id": incident.id,
        "title": incident.title,
        "severity": incident.severity,
        "created_at": incident.created_at.isoformat()
    })
    return {"message": "Incident created", "incident": incident}

@router.get("/")
def list_incidents():
    db = get_db()
    return list(db["incidents"].rows)
