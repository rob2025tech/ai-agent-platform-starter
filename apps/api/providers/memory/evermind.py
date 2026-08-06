from apps.api.providers.memory.base import MemoryProvider


class EverMindMemory(MemoryProvider):

    def __init__(self):
        # initialize EverMind client here later
        pass


    async def save(
        self,
        user_id: str,
        data: dict
    ):

        # TODO:
        # send memory to EverMind

        pass


    async def search(
        self,
        user_id: str,
        query: str
    ):

        # TODO:
        # search EverMind memories

        pass