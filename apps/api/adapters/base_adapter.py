from abc import ABC, abstractmethod

from ..models.request_models import ExecuteRequest
from ..models.response_models import ExecuteResponse


class BaseAdapter(ABC):
    """
    Base class for all AI backend adapters.

    Every backend (Mock, Snowflake, OpenAI, Ollama, etc.)
    must implement execute().
    """

    @abstractmethod
    def execute(self, request: ExecuteRequest) -> ExecuteResponse:
        """
        Execute a request against the backend.

        Returns:
            ExecuteResponse
        """
        pass
