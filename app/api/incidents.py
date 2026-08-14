from fastapi import APIRouter
from app.models.incident import Incident
from app.core.validation import validate_incident
from app.db.sqlite import get_db, init_db, update_incident as update_incident_db
from app.db.sqlite import delete_incident as delete_incident_db

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

@router.put("/{incident_id}")
def update_incident_endpoint(incident_id: int, incident: Incident):
    validate_incident(incident)
    updated = update_incident_db(incident_id, {
        "title": incident.title,
        "severity": incident.severity,
        "created_at": incident.created_at.isoformat()
    })
    if not updated:
        return {"error": "Incident not found"}
    return {"message": "Incident updated", "incident": incident}

@router.delete("/{incident_id}")
def delete_incident_endpoint(incident_id: int):
    deleted = delete_incident_db(incident_id)
    if not deleted:
        return {"error": "Incident not found"}
    return {"message": "Incident deleted", "id": incident_id}

@router.get("/filter")
def filter_incidents(severity: str = None, limit: int = 10, offset: int = 0):
    db = get_db()
    table = db["incidents"]

    if severity:
        rows = list(table.rows_where("severity = ?", [severity]))
    else:
        rows = list(table.rows)

    paginated = rows[offset: offset + limit]
    return paginated

@router.get("/analytics/severity")
def severity_analytics():
    db = get_db()
    rows = list(db["incidents"].rows)

    counts = {
        "low": 0,
        "medium": 0,
        "high": 0,
        "critical": 0
    }

    for row in rows:
        sev = row["severity"]
        if sev in counts:
            counts[sev] += 1

    total = sum(counts.values())
    percentages = {}

    if total > 0:
        for sev, count in counts.items():
            percentages[sev] = round((count / total) * 100, 2)

    return {
        "counts": counts,
        "percentages": percentages,
        "total": total
    }
