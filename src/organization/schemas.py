from pydantic import BaseModel


class OrganizationIn(BaseModel):
    id: int
    name: str
    description: str


class OrganizationOut(BaseModel):
    name: str
    description: str | None = None