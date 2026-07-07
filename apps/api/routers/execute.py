# apps/api/routers/execute.py

from fastapi import APIRouter
# from httpcore import request

from ..models.request_models import ExecuteRequest
from ..models.response_models import ExecuteResponse
from ..services.execution_service import execute_agent

router = APIRouter()

# @router.post("/execute")
# def execute(payload: dict):
#     return {
#         "status": "ok",
#         "mode": "mock",
#         "input": payload,
#         "output": "hello from agent platform",
#     }


@router.post(
    "/execute",
    response_model=ExecuteResponse,
)
def execute(request: ExecuteRequest):
    # return {
    #     "status": "ok",
    #     "mode": "mock",
    #     "input": request,
    #     "output": "hello from agent platform",
    # }
    return execute_agent(request)