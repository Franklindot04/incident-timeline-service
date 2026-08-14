from fastapi import HTTPException


def validate_incident(incident):
    if incident.severity not in ["low", "medium", "high", "critical"]:
        raise HTTPException(status_code=400, detail="Invalid severity")
