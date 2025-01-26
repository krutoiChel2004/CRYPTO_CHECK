from aiohttp import ClientSession

class HTTPCient:
    def __init__(self, base_url, api_key):
        self._session = ClientSession(
            base_url=base_url,
            headers={
                "Accepts": "application/json",
                "X-CMC_PRO_API_KEY": api_key
            },
            
        )

# pro-api.coinmarketcap.com

class CMCHTTPClient(HTTPCient):
    async def get_listings(self, params = None):
        async with self._session.get("/v1/cryptocurrency/listings/latest", params=params) as resp:
            result = await resp.json()
            return result["data"]