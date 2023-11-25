import os
from pathlib import Path
from dotenv import load_dotenv


BASE_PATH = (Path(__file__) / ".." / "..").resolve()
ENV_PATH = os.path.join(BASE_PATH, ".env")

load_dotenv(ENV_PATH)
RABBIT_HOST = os.getenv("RABIT_HOST")
RABBIT_PORT = os.getenv("RABBIT_PORT")
RABBITMQ_DEFAULT_USER = os.getenv("RABBITMQ_DEFAULT_USER")
RABBITMQ_DEFAULT_PASS = os.getenv("RABBITMQ_DEFAULT_USER")

PROJECT_HOST = os.getenv("PROJECT_HOST")
PROJECT_PORT = os.getenv("PORT")

RMQ_URL = f"amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@{RABBIT_HOST}:{RABBIT_PORT}"
