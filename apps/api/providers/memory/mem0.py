from apps.api.providers.memory.base import MemoryProvider
from apps.api.providers.memory.clients.mem0_client import Mem0Client


class Mem0Memory(MemoryProvider):

    def __init__(self):
        self.client = Mem0Client()


    async def save(
        self,
        user_id,
        data
    ):

        return await self.client.add(
            user_id=user_id,
            data=data
        )


    async def load(
        self,
        user_id
    ):

        return await self.client.search(
            user_id=user_id,
            query=""
        )