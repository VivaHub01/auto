from pydantic import BaseModel


class PlatformIn(BaseModel):
    id: int
    name: str
    description: str
    organization_name: str


class PlatformOut(BaseModel):
    name: str
    description: str | None = None
    organization_name: str