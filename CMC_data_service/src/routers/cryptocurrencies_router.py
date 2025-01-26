from fastapi import APIRouter

from src.schemes.cryptocurrencies_schemas.list_currencies import (ListCurrencies)

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
async def get_cryptocurrncies(params: ListCurrencies):
    
    return await cmc_client.get_listings(params)
