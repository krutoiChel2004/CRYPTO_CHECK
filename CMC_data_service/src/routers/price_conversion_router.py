from fastapi import APIRouter

from src.schemes.price_conversion_schemas.price_conversion import PriceConversion


from src.Client_CoinMarcetCap.http_client import CMCHTTPClient
from src.config import API_KEY_COINMARKETCAP

router = APIRouter(
    prefix="/price_conversion",
    tags=["Price conversion"]
) 

cmc_client = CMCHTTPClient(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=API_KEY_COINMARKETCAP
)

@router.post("/")
async def price_conversion(params: PriceConversion):
    
    return await cmc_client.price_conversion(params)
