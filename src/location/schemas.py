from pydantic import BaseModel


class LocationIn(BaseModel):
    id: int
    name: str
    description: str
    state: bool
    platform_name: str


class LocationOut(BaseModel):
    name: str
    description: str | None = None
    state: bool
    platform_name: str