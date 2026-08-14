from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_create_incident():
    payload = {
        "id": 1,
        "title": "Database outage",
        "severity": "high"
    }
    response = client.post("/incidents/", json=payload)
    assert response.status_code == 200
    assert response.json()["incident"]["title"] == "Database outage"

def test_list_incidents():
    response = client.get("/incidents/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
