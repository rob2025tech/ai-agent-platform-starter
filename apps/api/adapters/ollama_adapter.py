# apps/api/adapters/ollama_adapter.py

import httpx

from ..config.settings import settings

from .base_adapter import BaseAdapter

from ..models.request_models import ExecuteRequest
from ..models.response_models import ExecuteResponse


class OllamaAdapter(BaseAdapter):
    """
    Executes prompts using a local Ollama server.
    """

    def execute(self, request: ExecuteRequest) -> ExecuteResponse:
        with httpx.Client() as client:
            response = client.post(
                f"{settings.ollama_url}/api/generate",
                json={
                    "model": settings.ollama_model,
                    "prompt": request.prompt,
                    # "prompt": request.input,
                    "stream": False,
                },
                timeout=120,
            )

        response.raise_for_status()

        result = response.json()

        return ExecuteResponse(
            status="ok",
            # backend="ollama",
            backend=request.backend,
            prompt=request.prompt,
            output=result["response"],
        )
        