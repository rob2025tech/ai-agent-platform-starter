# apps/api/services/agent_service.py

from apps.api.config.settings import settings

from apps.api.providers.memory.registry import get_memory_provider
# from apps.api.providers.llm.registry import get_llm_provider
# from apps.api.providers.storage.registry import get_storage_provider
# from apps.api.providers.analytics.registry import get_analytics_provider


class AgentService:

    def __init__(self):

        self.memory = get_memory_provider(settings.memory_provider)
        # self.llm = get_llm_provider(settings.llm_provider)
        # self.storage = get_storage_provider(settings.storage_provider)
        # self.analytics = get_analytics_provider(settings.analytics_provider)

    async def execute(
        self,
        user_id: str,
        prompt: str,
    ):

        memories = await self.memory.search(
            user_id=user_id,
            query=prompt,
        )

        # response = await self.llm.generate(
        #     prompt=prompt,
        #     memories=memories,
        # )

        await self.memory.save(
            user_id=user_id,
            data={
                "prompt": prompt,
                # "response": response,
                "response": prompt,
            },
        )

        # await self.storage.save_conversation(
        #     user_id=user_id,
        #     prompt=prompt,
        #     response=response,
        # )

        # await self.analytics.record_request(
        #     provider=settings.llm_provider,
        #     prompt=prompt,
        #     response=response,
        # )

        return {
            "status": "ok",
            # "output": response,
            "output": "Memory provider executed",
            "memory_count": len(memories),
        }