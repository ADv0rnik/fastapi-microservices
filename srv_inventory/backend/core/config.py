import os

from pathlib import Path
from typing import List

from pydantic import AnyHttpUrl
from pydantic_settings import BaseSettings


BASE_DIR = (Path(__file__) / ".." / ".." / ".." / "..").resolve()
ENV_PATH = os.path.join(BASE_DIR, ".env")


class Settings(BaseSettings):
    API_VERSION: str = "/api/v1"
    PROJECT_NAME: str
    PROJECT_VERSION: str
    PROJECT_HOST: str
    PORT: int

    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_HOST: str
    DB_PORT: int

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

INIT_PRODUCT = [
    {"name": "Cellphone", "amount": 10, "price": 199.99, "category_id": 1},
    {"name": "Tablet", "amount": 5, "price": 299.99, "category_id": 1}
]

INIT_CATEGORY = {
    "name": "electronics"
}
