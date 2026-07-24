# apps/api/services/execution_service.py

from ..memory.memory_manager import memory
from ..skills.router import select
from ..adapters.registry import registry

from ..models.request_models import ExecuteRequest
from ..models.response_models import ExecuteResponse


def execute_agent(request: ExecuteRequest) -> ExecuteResponse:
    """
    Main execution pipeline.

    Later this becomes:

    Request
      ↓
    Load Context
      ↓
    Choose Skill
      ↓
    Choose Tools
      ↓
    Choose Backend
      ↓
    Backend adapter
      ↓
    Run LLM
      ↓
    Store Conversation
    Memory
      ↓
    Return/Response
    """

    # adapter = registry.get(request.backend)
    # return adapter.execute(request)

    # context = memory.load(request.user_id)
    # TODO:
    # Pass context into the adapter once adapters support memory.

    skill = select(request)
    backend = request.backend or skill.backend
    # backend = skill.backend if skill.backend else request.backend

    adapter = registry.get(backend)
    # adapter = registry.get(skill.backend)

    result = adapter.execute(request)

    memory.save(
        request.user_id,
        request.prompt,
        result,
    )

    return result
