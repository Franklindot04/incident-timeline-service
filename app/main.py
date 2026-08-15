from fastapi import FastAPI, Request, Body
from fastapi.exceptions import HTTPException
from time import time
from fastapi.responses import PlainTextResponse
from datetime import datetime, timezone
import uuid
from app.core.logging import logger
from app.api.incidents import router as incidents_router
from app.db.sqlite import init_db
from app.core.errors import http_error_handler, general_error_handler
from app.core.version import get_version


app = FastAPI()
init_db()


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time()
    response = await call_next(request)
    duration = round(time() - start, 4)
    logger.info(f"{request.method} {request.url.path} completed in {duration}s")
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
    return {"ip": request.client.host}
