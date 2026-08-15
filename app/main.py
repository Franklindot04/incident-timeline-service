from fastapi import FastAPI, Request, Body
from fastapi.exceptions import HTTPException
from time import time
from fastapi.responses import PlainTextResponse
from datetime import datetime, timezone
import uuid
import json
import os
import random
from app.core.logging import logger
from app.api.incidents import router as incidents_router
from app.db.sqlite import init_db
from app.core.errors import http_error_handler, general_error_handler
from app.core.version import get_version


START_TIME = time()

app = FastAPI()
init_db()


# ---------------------------------------------------------
# X-Request-ID Middleware (Correlation ID Support)
# ---------------------------------------------------------
@app.middleware("http")
async def add_request_id(request: Request, call_next):
    request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response


# ---------------------------------------------------------
# Logging Middleware
# ---------------------------------------------------------
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time()
    response = await call_next(request)
    duration = round(time() - start, 4)
    logger.info(
        f"{request.method} {request.url.path} completed in {duration}s "
        f"X-Request-ID={response.headers.get('X-Request-ID')}"
    )
    return response


# ---------------------------------------------------------
# JSON Logging Middleware + X-Duration header
# ---------------------------------------------------------
@app.middleware("http")
async def json_logging(request: Request, call_next):
    start = time()
    response = await call_next(request)
    duration = round(time() - start, 4)

    log = {
        "method": request.method,
        "path": request.url.path,
        "status": response.status_code,
        "duration": duration
    }

    print(json.dumps(log))

    response.headers["X-Duration"] = str(duration)
    return response


# ---------------------------------------------------------
# Global Headers Middleware (X-Service + X-Version)
# ---------------------------------------------------------
@app.middleware("http")
async def add_global_headers(request: Request, call_next):
    response = await call_next(request)
    response.headers["X-Service"] = "incident-timeline-service"
    response.headers["X-Version"] = get_version()
    return response


app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(Exception, general_error_handler)

app.include_router(incidents_router, prefix="/incidents")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def ready():
    try:
        init_db()  # lightweight readiness check
        return {"ready": True}
    except Exception:
        return {"ready": False}


@app.get("/ping")
def ping():
    return {"ping": "pong"}


@app.get("/version")
def version():
    return {"version": get_version()}


@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return "# metrics will be added later\n"


@app.get("/status")
def status():
    return {
        "service": "incident-timeline-service",
        "version": get_version(),
        "health": "ok",
        "ready": True,
        "ping": "pong",
    }


@app.get("/time")
def time_endpoint():
    now = datetime.now(timezone.utc)
    return {
        "iso": now.isoformat(),
        "epoch": int(now.timestamp()),
        "timezone": "UTC"
    }


@app.post("/echo")
def echo(data: dict = Body(...)):
    return {"echo": data}


@app.get("/uuid")
def uuid_endpoint():
    return {"uuid": str(uuid.uuid4())}


@app.get("/headers")
def headers_endpoint(request: Request):
    return {"headers": dict(request.headers)}


@app.get("/ip")
def ip(request: Request):
    client = request.client
    return {"ip": client.host if client else "unknown"}


@app.get("/method")
async def method(request: Request):
    return {"method": request.method}


@app.get("/query")
def query(request: Request):
    return {"query": dict(request.query_params)}


@app.get("/path")
def path(request: Request):
    return {"path": request.url.path}


# ---------------------------------------------------------
# /config Endpoint (Static Safe Config)
# ---------------------------------------------------------
@app.get("/config")
def config():
    return {
        "debug": False,
        "database": "sqlite",
        "service": "incident-timeline-service"
    }


# ---------------------------------------------------------
# /env Endpoint (Safe Environment Info)
# ---------------------------------------------------------
@app.get("/env")
def env():
    return {
        "pythonpath": os.getenv("PYTHONPATH", "unknown"),
        "environment": os.getenv("ENVIRONMENT", "unknown")
    }


# ---------------------------------------------------------
# /uptime Endpoint
# ---------------------------------------------------------
@app.get("/uptime")
def uptime():
    return {"uptime": round(time() - START_TIME, 2)}


# ---------------------------------------------------------
# /routes Endpoint
# ---------------------------------------------------------
@app.get("/routes")
def routes():
    return {"routes": [route.path for route in app.routes]}


# ---------------------------------------------------------
# /summary Endpoint
# ---------------------------------------------------------
@app.get("/summary")
def summary():
    return {
        "endpoints": len(app.routes),
        "version": get_version(),
        "status": "running"
    }


# ---------------------------------------------------------
# /random Endpoint
# ---------------------------------------------------------
@app.get("/random")
def random_number():
    return {"value": random.randint(1, 1000)}
