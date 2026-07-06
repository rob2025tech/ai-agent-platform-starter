from pydantic import BaseModel

class ExecuteRequest(BaseModel):
    input: str
    backend: str = "mock"