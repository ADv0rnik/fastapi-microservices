from config import Settings

from aio_pika import connect_robust
from aio_pika.patterns import RPC


settings = Settings()
RMQ_URL = f"amqp://{settings.RABBITMQ_DEFAULT_USER}:{settings.RABBITMQ_DEFAULT_PASS}@{settings.RABIT_HOST}:{settings.RABBIT_PORT}"


async def send_request_to_queue(
        message: dict
):
    connection = await connect_robust(RMQ_URL)

    async with connection:
        channel = await connection.channel()
        rpc = await RPC.create(channel)
        result, status_code = await rpc.proxy.resolve(**message)
        return result, status_code
