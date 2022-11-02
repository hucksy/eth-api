from functools import lru_cache
from pydantic import BaseSettings


class EnvConfigs(BaseSettings):
    """config stuff validated with pydantic"""
    APP_KEY: str
    INFURA_ENDPOINT: str
    ENVIRONMENT: str
    DATABASE_URL: str
    DATABASE_URL_TEST: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf8'


@lru_cache()
def get_env_configs() -> EnvConfigs:
    return EnvConfigs()
