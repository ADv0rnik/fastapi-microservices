import asyncio
from resolver import resolve
from config import RMQ_URL

from aio_pika import connect_robust
from aio_pika.patterns import RPC

print(RMQ_URL)


async def server() -> None:
    connection = await connect_robust(RMQ_URL)

    async with connection:
        channel = await connection.channel()
        rpc = await RPC.create(channel)
        await rpc.register(resolve.__name__, resolve, auto_delete=True)

        try:
            await asyncio.Future()
        finally:
            await connection.close()


if __name__ == '__main__':
    asyncio.run(server())
