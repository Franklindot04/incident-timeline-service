# Incident Timeline Service

A lightweight, production-ready FastAPI microservice for tracking incidents, their severity, timestamps, and providing rich introspection, debugging, and metadata endpoints.

Built with clean architecture, structured logging, correlation IDs, safe configuration exposure, and a fully validated incident model.

## 🚀 Features

- Incident CRUD — create and list incidents
- Severity validation — strict severity enforcement
- Correlation IDs — `X-Request-ID` middleware
- Structured JSON logging — request logs with duration
- Global service/version headers — `X-Service`, `X-Version`
- Runtime metadata endpoints — `/config`, `/env`, `/routes`, `/summary`
- Debugging utilities — `/hash`, `/reverse`, `/repeat`, `/stats`, `/checksum`, `/whoami`
- Health and readiness checks — `/health`, `/ready`, `/status`
- CLI client — create and list incidents from the terminal
- CI pipeline — pytest, flake8, and mypy

## 📡 API Endpoints Overview

### Core Incident Endpoints

- `POST /incidents/` — Create an incident
- `GET /incidents/` — List incidents

Example payload:

```json
{
  "id": 1,
  "title": "Database outage",
  "severity": "high"
}
```

## Health and Metadata

- `GET /health` — Basic health check
- `GET /ready` — Readiness probe
- `GET /status` — Combined service status
- `GET /version` — Service version
- `GET /config` — Safe static configuration
- `GET /env` — Safe environment information
- `GET /routes` — List all routes
- `GET /summary` — Service overview
- `GET /uptime` — Service uptime

## Utility Endpoints

- `GET /time` — ISO and epoch timestamp
- `GET /uuid` — Random UUID
- `GET /headers` — Request headers
- `GET /ip` — Client IP
- `GET /method` — HTTP method
- `GET /query` — Query parameters
- `GET /path` — Request path

## Text Processing

- `POST /hash` — SHA-256 hash
- `POST /reverse` — Reverse a string
- `POST /uppercase` — Convert text to uppercase
- `POST /lowercase` — Convert text to lowercase
- `GET /repeat` — Repeat text
- `POST /stats` — Text analytics
- `POST /checksum` — CRC32 checksum

## Client Introspection

- `GET /whoami` — IP address and user agent

## 🖥️ CLI Usage

### Create an Incident

```bash
python cli.py --create --id 1 --title "DB outage" --severity high
```

### List Incidents

```bash
python cli.py --list
```

## 🏗️ Architecture Overview

```text
+--------------------------------------------------+
|                  CLI Client                      |
+-------------------------+------------------------+
                          |
                          v
+--------------------------------------------------+
|                  FastAPI Service                |
|  - Incident CRUD                                |
|  - Middleware (Request ID, Logging, Headers)    |
|  - Metadata and debugging endpoints             |
+-------------------------+------------------------+
                          |
                          v
+--------------------------------------------------+
|                 Incident Model                  |
+-------------------------+------------------------+
                          |
                          v
+--------------------------------------------------+
|                 SQLite Storage                  |
+--------------------------------------------------+
```

## 📦 Tech Stack

- FastAPI
- Pydantic
- SQLite
- Structured logging
- pytest, mypy, and flake8
- Lightweight CLI client

## 🎯 Why This Project Matters

This service demonstrates real SRE and DevOps engineering practices:

- Clean API design
- Proper middleware layering
- Observability built in
- Safe metadata exposure
- Deterministic debugging utilities
- Strong validation
- CI discipline

A strong foundation for incident ingestion, monitoring, or integration into a larger SRE platform.