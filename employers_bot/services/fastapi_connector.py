import aiohttp

from config import settings


class ConnectorDB:

    @classmethod
    async def get(cls, endpoint: str, data):
        async with aiohttp.ClientSession() as session:
            url = f"http://app:8000{endpoint}/get"
            data["bot_token"] = settings.BOT_TOKEN
            async with session.post(url, json=data, ssl=False) as resp:
                print(data)
                if resp.status != 200:
                    return
                return await resp.json()
