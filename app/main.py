from fastapi import FastAPI
from app.api.incidents import router as incidents_router

app = FastAPI()

app.include_router(incidents_router, prefix="/incidents")

@app.get("/health")
def health():
    return {"status": "ok"}
