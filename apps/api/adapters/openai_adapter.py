from .base_adapter import BaseAdapter

from ..models.request_models import ExecuteRequest
from ..models.response_models import ExecuteResponse


class OpenAIAdapter(BaseAdapter):
    """
    Executes prompts using the OpenAI API.
    """

    def execute(self, request: ExecuteRequest) -> ExecuteResponse:
        raise NotImplementedError("OpenAI adapter has not been implemented yet.")
