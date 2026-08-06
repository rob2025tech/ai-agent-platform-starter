from apps.api.providers.memory.evermind import EverMindMemory
from apps.api.providers.memory.mem0 import Mem0Memory


memory_providers = {
    "evermind": EverMindMemory(),
    "mem0": Mem0Memory(),
}


def get_memory_provider(name):

    return memory_providers[name]