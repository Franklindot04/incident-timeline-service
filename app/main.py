from fastapi import FastAPI, Request
from fastapi.exceptions import HTTPException
from time import time
from fastapi.responses import PlainTextResponse
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


@app.get("/version")
def version():
    return {"version": get_version()}


@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return "# metrics will be added later\n"
