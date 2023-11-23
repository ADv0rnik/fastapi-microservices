import os
import asyncio

from pathlib import Path
from dotenv import load_dotenv

from aio_pika import connect_robust
from aio_pika.patterns import RPC


BASE_PATH = (Path(__file__) / ".." / "..").resolve()
ENV_PATH = os.path.join(BASE_PATH, ".env")

load_dotenv(ENV_PATH)
RABBIT_HOST = os.getenv("RABIT_HOST")
RABBIT_PORT = os.getenv("RABBIT_PORT")
RABBITMQ_DEFAULT_USER = os.getenv("RABBIT_DEFAULT_USER")
RABBITMQ_DEFAULT_PASS = os.getenv("RABBIT_DEFAULT_PASS")

RMQ_URL = f"amqp://{RABBITMQ_DEFAULT_USER}:{RABBITMQ_DEFAULT_PASS}@{RABBIT_HOST}:{RABBIT_PORT}"


async def server() -> None:
    connection = await connect_robust(RMQ_URL)

    async with connection:
        channel = await connection.channel()
        rpc = await RPC.create(channel)
