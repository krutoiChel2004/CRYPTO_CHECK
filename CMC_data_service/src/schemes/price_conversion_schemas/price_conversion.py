from pydantic import BaseModel

class PriceConversion(BaseModel):
    amount: float
    id: str
    convert: str