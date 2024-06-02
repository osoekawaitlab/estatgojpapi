from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings as PydanticBaseSettings
from pydantic_settings import SettingsConfigDict


class BaseSettings(PydanticBaseSettings):
    model_config = SettingsConfigDict(env_file_encoding="utf-8", env_nested_delimiter="__", env_prefix="ESTATGOJPAPI_")


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    app_id: str
    base_url: AnyHttpUrl = AnyHttpUrl("https://api.e-stat.go.jp/rest/3.0/app/json/")
