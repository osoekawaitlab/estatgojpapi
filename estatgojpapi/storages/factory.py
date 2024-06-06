from ..settings import StorageSettings, StorageType
from .base import BaseStorage
from .memory import MemoryStorage


def create_storage(settings: StorageSettings) -> BaseStorage:
    if settings.type == StorageType.MEMORY:
        return MemoryStorage()
    raise ValueError(f"Unsupported storage type: {settings.type}")
