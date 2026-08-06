from apps.api.providers.memory.registry import get_memory_provider


class AgentService:

    def __init__(self):

        self.memory = get_memory_provider("evermind")


    async def process_message(
        self,
        user_id,
        message
    ):

        await self.memory.save(
            user_id=user_id,
            data={
                "fact": message
            }
        )

        # later:
        # call LLM
        # retrieve memories
        # calculate tokens
        # record analytics

        return {
            "status": "ok"
        }