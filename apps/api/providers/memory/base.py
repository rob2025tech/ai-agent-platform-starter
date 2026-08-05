from abc import ABC, abstractmethod


class MemoryProvider(ABC):

    @abstractmethod
    async def remember(self, data):
        pass

    @abstractmethod
    async def search(self, query):
        pass