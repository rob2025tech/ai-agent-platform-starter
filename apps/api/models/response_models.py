from pydantic import BaseModel

class ExecuteResponse(BaseModel):
    status: str
    backend: str
    output: str