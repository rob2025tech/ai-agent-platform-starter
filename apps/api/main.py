from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/execute")
def execute(payload: dict):
    return {
        "status": "ok",
        "mode": "mock",
        "input": payload,
        "output": "hello from agent platform",
    }