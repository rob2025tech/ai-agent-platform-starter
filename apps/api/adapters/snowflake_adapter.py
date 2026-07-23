from .base_adapter import BaseAdapter

from ..models.request_models import ExecuteRequest
from ..models.response_models import ExecuteResponse


class SnowflakeAdapter(BaseAdapter):
    """
    Executes prompts using Snowflake Cortex.
    """

    def execute(self, request: ExecuteRequest) -> ExecuteResponse:
        raise NotImplementedError("Snowflake adapter has not been implemented yet.")
