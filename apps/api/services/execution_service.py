# apps/api/services/execution_service.py

from ..adapters.registry import registry

from ..models.request_models import ExecuteRequest
from ..models.response_models import ExecuteResponse


def execute_agent(request: ExecuteRequest) -> ExecuteResponse:
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

    adapter = registry.get(request.backend)
    return adapter.execute(request)

    