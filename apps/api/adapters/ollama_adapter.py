from .base_adapter import BaseAdapter

from ..models.request_models import ExecuteRequest
from ..models.response_models import ExecuteResponse


class OllamaAdapter(BaseAdapter):
    """
    Executes prompts using a local Ollama server.
    """

    def execute(self, request: ExecuteRequest) -> ExecuteResponse:
        raise NotImplementedError(
            "Ollama adapter has not been implemented yet."
        )