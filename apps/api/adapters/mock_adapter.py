from .base_adapter import BaseAdapter

from ..models.request_models import ExecuteRequest
from ..models.response_models import ExecuteResponse


class MockAdapter(BaseAdapter):
    """
    Fake backend used during development.

    This allows the entire execution pipeline to be tested
    without any external AI provider.
    """

    def execute(self, request: ExecuteRequest) -> ExecuteResponse:

        return ExecuteResponse(
            status="ok",
            backend="mock",
            input=request.input,
            output="hello from mock backend",
        )