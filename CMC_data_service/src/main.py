from fastapi import FastAPI



from src.Client_CoinMarcetCap.http_client import CMCHTTPClient
from src.config import API_KEY_COINMARKETCAP

app = FastAPI()


cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=API_KEY_COINMARKETCAP
)


@app.get("/cryptocurrencies")
async def get_cryptocurrncies():
    print(API_KEY_COINMARKETCAP)
    parameters = {
        'start':'1',
        'limit':'1',
        'convert':'USD'
        }
    return await cmc_client.get_listings(parameters)