from fastapi import FastAPI

app = FastAPI(title="Bot Webhook")

@app.get("/healthz")
def healthz():
    return {"status": "ok"}
