from fastapi import APIRouter

router = APIRouter()

@router.post("/execute")
def execute(payload: dict):
    return {
        "status": "ok",
        "mode": "mock",
        "input": payload,
        "output": "hello from agent platform",
    }