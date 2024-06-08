from ..settings import StorageSettings, StorageType
from .base import BaseStorage
from .local_file import LocalFileStorage
from .memory import MemoryStorage


def create_storage(settings: StorageSettings) -> BaseStorage:
    if settings.type == StorageType.MEMORY:
        return MemoryStorage()
    elif settings.type == StorageType.LOCAL_FILE:
        return LocalFileStorage(settings.path)
    raise ValueError(f"Unsupported storage type: {settings.type}")
