import asyncio

from tinkoff.invest import AsyncClient

class Client:
    def __init__(self, api_key):
        self._session = AsyncClient(api_key)
         

class TInvestClient(Client):
    async def get_accounts(self):
        async with self._session as client:
            return await client.users.get_accounts()