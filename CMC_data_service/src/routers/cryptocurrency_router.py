from fastapi import APIRouter

from src.schemes.cryptocurrency_schemas.list_currencies import (ListCurrencies)
from src.schemes.cryptocurrency_schemas.currency import (Currency)

from src.Client_CoinMarcetCap.http_client import CMCHTTPClient
from src.config import API_KEY_COINMARKETCAP

router = APIRouter(
    prefix="/cryptocurrencies",
    tags=["Cryptocurrencies"]
) 

cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=API_KEY_COINMARKETCAP
)

@router.post("/")
async def get_listings(params: ListCurrencies):
    
    return await cmc_client.get_listings(params)

@router.post("/currency")
async def get_currency(params: Currency):
    
    return await cmc_client.get_currency(params)