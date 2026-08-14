from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from app.api.incidents import router as incidents_router
from app.db.sqlite import init_db
from app.core.errors import http_error_handler, general_error_handler

app = FastAPI()
init_db()

app.add_exception_handler(HTTPException, http_error_handler)
app.add_exception_handler(Exception, general_error_handler)

app.include_router(incidents_router, prefix="/incidents")

@app.get("/health")
def health():
    return {"status": "ok"}
