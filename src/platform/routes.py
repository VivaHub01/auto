from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import get_async_session
from src.platform.schemas import PlatformOut
from src.platform.service import create_platform, get_platforms, get_platform_by_name, update_platform, delete_platform


platform = APIRouter(prefix="/platforms", tags=["Platform"])


@platform.post('/', response_model=PlatformOut)
async def create_organization(platform: PlatformOut, db: AsyncSession = Depends(get_async_session)):
    return await create_platform(platform, db)

@platform.get("/", response_model=list[PlatformOut])
async def get_organizations(db: AsyncSession = Depends(get_async_session)):
    return await get_platforms(db)

@platform.get("/{platform_name}", response_model=PlatformOut)
async def get_organization_by_name(platform_name: str, db: AsyncSession = Depends(get_async_session)):
    return await get_platform_by_name(platform_name, db)

@platform.put("/{platform_name}", response_model=PlatformOut)
async def update_organization(platform_name: str, org: PlatformOut, db: AsyncSession = Depends(get_async_session)):
    return await update_platform(platform_name, org, db)

@platform.delete("/{platform_name}", response_model=PlatformOut)
async def delete_organization(platform_name: str, db: AsyncSession = Depends(get_async_session)):
    return await delete_platform(platform_name, db)
