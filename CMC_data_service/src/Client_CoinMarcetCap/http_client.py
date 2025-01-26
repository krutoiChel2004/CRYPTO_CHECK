from aiohttp import ClientSession

from src.schemes.cryptocurrency_schemas.list_currencies import (ListCurrencies)
from src.schemes.cryptocurrency_schemas.currency import (Currency)

class HTTPCient:
    def __init__(self, base_url, api_key):
        self._session = ClientSession(
            base_url=base_url,
            headers={
                "Accepts": "application/json",
                "X-CMC_PRO_API_KEY": api_key
            },
            
        )


class CMCHTTPClient(HTTPCient):
    async def get_listings(self, params: ListCurrencies = None):

        async with self._session.get(
            "/v1/cryptocurrency/listings/latest", 
            params=params.model_dump()
        ) as resp:
            
            result = await resp.json()
            return result["data"]
        
    async def get_currency(self, params: Currency = None):

        async with self._session.get(
            "/v2/cryptocurrency/quotes/latest", 
            params=params.model_dump()
        ) as resp:
            
            result = await resp.json()
            return result["data"]