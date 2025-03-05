from pydantic import BaseModel


class ClassificationIn(BaseModel):
    id: int
    name: str
    description: str
    state: bool
    asset_name: str


class ClassificationOut(BaseModel):
    name: str
    description: str | None = None
    state: bool
    asset_name: str
