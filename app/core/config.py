from pydantic import Field
from pydantic_settings import BaseSettings
from pathlib import Path
from functools import lru_cache


class AppConfig(BaseSettings):
    host: str = "localhost"
    port: int = 8000
    project_name: str = "Phone Address API"
    api_prefix: str = "/api/v1"
    version: str = "1.0.0"
    openapi_url: str = "/docs/v1/openapi.json"
    docs_url: str = "/docs/v1/"
    debug: bool = True

    redis_url: str = Field(..., alias="REDIS_URL")
    phone_address_db: int = Field(..., alias="PHONE_ADDRESS_DB")

    class Config:
        env_file = Path(__file__).parent.parent / ".env"


@lru_cache()
def get_config():
    return AppConfig()
