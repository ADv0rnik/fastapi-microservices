import aiohttp
from config import PROJECT_HOST, PROJECT_PORT

from typing import Tuple


async def resolve(
        method: str,
        path: str,
        params: dict = None,
        data: dict = None,
        headers: dict = None
) -> Tuple[dict, int]:

    _, service_name, *_ = path.split("/")
    host = f"{PROJECT_HOST}:{PROJECT_PORT}"
    url = f"http://{host}{path}"
    response, status_code = await make_request(
        url=url, method=method, params=params, data=data, headers=headers
    )
    return response, status_code


async def make_request(
        url: str,
        method: str,
        params: dict = None,
        data: dict = None,
        headers: dict = None
) -> Tuple[dict, int]:

    async with aiohttp.ClientSession() as session:
        request = getattr(session, method)
        async with await request(url, params=params, json=data, headers=headers) as response:
            response_data = await response.json()
            return response_data, response.status
