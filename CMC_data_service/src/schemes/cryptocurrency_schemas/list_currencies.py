from pydantic import BaseModel

class ListCurrencies(BaseModel):
    start: str
    limit: str
    convert: str