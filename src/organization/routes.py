from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import get_async_session
from src.organization.schemas import OrganizationOut
from src.organization.service import create_organization, get_organizations, get_organization_by_name, update_organization, delete_organization


organization = APIRouter(prefix="/organizations", tags=["Organization"])


@organization.post('/', response_model=OrganizationOut)
async def create_organization_route(org: OrganizationOut, db: AsyncSession = Depends(get_async_session)):
    return await create_organization(org, db)

@organization.get("/", response_model=list[OrganizationOut])
async def get_organizations_route(db: AsyncSession = Depends(get_async_session)):
    return await get_organizations(db)

@organization.get("/{org_name}", response_model=OrganizationOut)
async def get_organization_by_name_route(org_name: str, db: AsyncSession = Depends(get_async_session)):
    return await get_organization_by_name(org_name, db)

@organization.put("/{org_name}", response_model=OrganizationOut)
async def update_organization_route(org_name: str, org: OrganizationOut, db: AsyncSession = Depends(get_async_session)):
    return await update_organization(org_name, org, db)

@organization.delete("/{org_name}", response_model=OrganizationOut)
async def delete_organization_route(org_name: str, db: AsyncSession = Depends(get_async_session)):
    return await delete_organization(org_name, db)
