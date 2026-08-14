from fastapi import FastAPI
from app.api.incidents import router as incidents_router
from app.db.sqlite import init_db


app = FastAPI()
init_db()

app.include_router(incidents_router, prefix="/incidents")

@app.get("/health")
def health():
    return {"status": "ok"}
