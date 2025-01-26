from pydantic import BaseModel

class Currency(BaseModel):
    # id: str = None
    symbol: str = None