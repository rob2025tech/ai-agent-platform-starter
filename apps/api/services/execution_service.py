# apps/api/services/execution_service.py

from ..models.request_models import ExecuteRequest


def execute_agent(request: ExecuteRequest) -> dict:
    """
    Main execution pipeline.

    Later this becomes:

    Request
      ↓
    Skill selection
      ↓
    Backend adapter
      ↓
    Memory
      ↓
    Response
    """

    # return {
    #     "status": "ok",
    #     "mode": "mock",
    #     "input": request.message,
    #     "output": "hello from execution service",
    # }
    return {
        "status": "ok",
        "backend": request.backend,
        "input": request.input,
        "output": f"hello from {request.backend} backend",
    }