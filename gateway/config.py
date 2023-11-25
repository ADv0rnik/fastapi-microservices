import os
from pathlib import Path
from typing import List

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


BASE_PATH = (Path(__file__) / ".." / "..").resolve()
ENV_PATH = os.path.join(BASE_PATH, ".env")


class Settings(BaseSettings):
    API_VERSION: str = "/api/v1"
    GATEWAY_NAME: str
    PROJECT_HOST: str
    GATEWAY_PORT: int

    RABBITMQ_DEFAULT_USER: str
    RABBITMQ_DEFAULT_PASS: str
    RABIT_HOST: str
    RABBIT_PORT: int

    ALLOWED_ORIGIN: List[AnyHttpUrl] = [
        "http://localhost",
        "http://127.0.0.1",
        "http://0.0.0.0"
    ]

    class Config:
        env_file = ENV_PATH
        env_file_encoding = "utf-8"
        case_sensitive = True
        extra = "ignore"


settings = Settings()
