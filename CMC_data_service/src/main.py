from fastapi import FastAPI

from src.routers.cryptocurrency_router import router as cryptocurrencies_router
from src.routers.price_conversion_router import router as price_conversion_router


from src.Client_CoinMarcetCap.http_client import CMCHTTPClient
from src.config import API_KEY_COINMARKETCAP

app = FastAPI()


cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=API_KEY_COINMARKETCAP
)

app.include_router(cryptocurrencies_router)
app.include_router(price_conversion_router)
