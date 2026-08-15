"""
# Incident Timeline Service

A lightweight, production‑ready FastAPI microservice for tracking incidents, their severity, timestamps, and providing rich introspection, debugging, and metadata endpoints.
Built with clean architecture, structured logging, correlation IDs, safe configuration exposure, and a fully validated incident model.

---

## 🚀 Features
- Incident CRUD — create & list incidents
- Severity validation — strict severity enforcement
- Correlation IDs — X-Request-ID middleware
- Structured JSON logging — request logs with duration
- Global service/version headers — X-Service, X-Version
- Runtime metadata endpoints — /config, /env, /routes, /summary
- Debugging utilities — /hash, /reverse, /repeat, /stats, /checksum, /whoami
- Health & readiness checks — /health, /ready, /status
- CLI client — create/list incidents from terminal
- CI pipeline — pytest + flake8 + mypy

---

## 📡 API Endpoints Overview

### Core Incident Endpoints
`POST /incidents/` — Create incident  
`GET /incidents/` — List incidents  

Example payload:
```json
{
  "id": 1,
  "title": "Database outage",
  "severity": "high"
}
```
---

## Health & Metadata
`GET /health` — basic health  
`GET /ready` — readiness probe  
`GET /status` — combined service status  
`GET /version` — service version  
`GET /config` — safe static config  
`GET /env` — safe environment info  
`GET /routes` — list all routes  
`GET /summary` — service overview  
`GET /uptime` — service uptime  

---

## Utility Endpoints
`GET /time` — ISO + epoch timestamp  
`GET /uuid` — random UUID  
`GET /headers` — request headers  
`GET /ip` — client IP  
`GET /method` — HTTP method  
`GET /query` — query params  
`GET /path` — request path  

---

## Text Processing
`POST /hash` — SHA‑256  
`POST /reverse` — reverse string  
`POST /uppercase` — uppercase  
`POST /lowercase` — lowercase  
`GET /repeat` — repeat text  
`POST /stats` — text analytics  
`POST /checksum` — CRC32 checksum  

---

## Client Introspection
`GET /whoami` — IP + User‑Agent  

---

## 🖥️ CLI Usage

### Create Incident
python cli.py --create --id 1 --title "DB outage" --severity high

### List Incidents
python cli.py --list

---

## 🏗️ Architecture Overview

+--------------------------------------------------+
|                  CLI Client                      |
+-------------------------+------------------------+
                          |
                          v
+--------------------------------------------------+
|                  FastAPI Service                 |
|  - Incident CRUD                                   |
|  - Middleware (Request ID, Logging, Headers)       |
|  - Metadata & Debugging Endpoints                  |
+-------------------------+------------------------+
                          |
                          v
+--------------------------------------------------+
|                 Incident Model                    |
+-------------------------+------------------------+
                          |
                          v
+--------------------------------------------------+
|                 SQLite Storage                    |
+--------------------------------------------------+

---

## 📦 Tech Stack
- FastAPI  
- Pydantic  
- SQLite  
- Structured logging  
- pytest + mypy + flake8  
- Lightweight CLI client  

---

## 🎯 Why This Project Matters

This service demonstrates real SRE/DevOps engineering practices:

- Clean API design  
- Proper middleware layering  
- Observability baked in  
- Safe metadata exposure  
- Deterministic debugging utilities  
- Strong validation  
- CI discipline  

A perfect foundation for incident ingestion, monitoring, or integration into a larger SRE platform.
"""
