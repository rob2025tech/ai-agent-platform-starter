from .base import LLMProvider


class OllamaProvider(LLMProvider):

    async def execute(self,prompt):

        # call local Ollama

        return response