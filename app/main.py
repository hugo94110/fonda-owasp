from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
import psycopg
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def index():
    return "<h1>test</h1>"

###################

@app.get("/health")
def health():
    try:
        with psycopg.connect(os.environ["DATABASE_URL"], connect_timeout=3) as conn:
            conn.execute("SELECT 1")
        return {"status": "ok", "db": "ok"}
    except Exception:
        return JSONResponse(status_code=503, content={"status": "error", "db": "unreachable"})