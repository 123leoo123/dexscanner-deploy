from fastapi import FastAPI
from threading import Thread
from src.coleta.runner import run_loop

app = FastAPI()

@app.on_event("startup")
def start_background_task():
    Thread(target=run_loop, daemon=True).start()

@app.get("/ping")
def ping():
    return {"status": "🟢 DexScanner Coletando!"}
