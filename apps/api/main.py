from fastapi import FastAPI

# @app.get("/health")
# def health():
#     return {"status": "ok"}

# from routers.health import router as health_router
from .routers.health import router as health_router

# @app.post("/execute")
# def execute(payload: dict):
#     return {
#         "status": "ok",
#         "mode": "mock",
#         "input": payload,
#         "output": "hello from agent platform",
#     }
# from routers.execute import router as execute_router
from .routers.execute import router as execute_router
from .routers import butterbase


app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Agent Platform Starter"}

app.include_router(health_router)
app.include_router(execute_router)
app.include_router(
    butterbase.router
)
