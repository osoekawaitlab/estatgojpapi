from enum import Enum
from typing import Annotated, Literal, Union

from pydantic import AnyHttpUrl, DirectoryPath, Field, NewPath
from pydantic_settings import BaseSettings as PydanticBaseSettings
from pydantic_settings import SettingsConfigDict

NewOrExistingDirectoryPath = Union[NewPath, DirectoryPath]


class BaseSettings(PydanticBaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="utf-8", env_nested_delimiter="__", env_prefix="ESTATGOJPAPI_")


class StorageType(str, Enum):
    MEMORY = "MEMORY"
    LOCAL_FILE = "LOCAL_FILE"


class BaseStorageSettings(BaseSettings):
    type: StorageType


class MemoryStorageSettings(BaseStorageSettings):
    type: Literal[StorageType.MEMORY] = StorageType.MEMORY


class LocalFileStorageSettings(BaseStorageSettings):
    type: Literal[StorageType.LOCAL_FILE] = StorageType.LOCAL_FILE
    path: NewOrExistingDirectoryPath


StorageSettings = Annotated[
    Union[MemoryStorageSettings, LocalFileStorageSettings],
    Field(discriminator="type"),
]


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    app_id: str
    base_url: AnyHttpUrl = AnyHttpUrl("https://api.e-stat.go.jp/rest/3.0/app/json/")
    storage_settings: StorageSettings = MemoryStorageSettings()
