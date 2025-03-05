from pydantic import BaseModel

class AssetIn(BaseModel):
    id: int
    name: str
    description: str
    state: bool
    location_name: str

class AssetOut(BaseModel):
    name: str
    description: str | None = None
    state: bool
    location_name: str
