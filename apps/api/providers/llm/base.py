from abc import ABC, abstractmethod


class LLMProvider(ABC):

    @abstractmethod
    async def execute(
        self,
        prompt: str,
    ):
        pass