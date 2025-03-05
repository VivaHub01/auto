from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from src.organization.models import Organization
from src.platform.models import Platform
from src.platform.schemas import PlatformOut


async def create_platform(platform: PlatformOut, db: AsyncSession):
    db_organization = await db.execute(select(Organization).filter(Organization.name == platform.organization_name))
    db_organization = db_organization.scalar_one_or_none()
    if db_organization is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    db_platform = Platform(name=platform.name, description=platform.description, organization_name=platform.organization_name)
    db.add(db_platform)
    await db.commit()
    await db.refresh(db_platform)
    return db_platform



async def get_platforms(db: AsyncSession):
    result = await db.execute(select(Platform))
    return result.scalars().all()


async def get_platform_by_name(platform_name: str, db: AsyncSession):
    result = await db.execute(select(Platform).filter(Platform.name == platform_name))
    db_platform = result.scalar_one_or_none()
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    return db_platform


async def update_platform(platform_name: str, platform: PlatformOut, db: AsyncSession):
    result = await db.execute(select(Platform).filter(Platform.name == platform_name))
    db_platform = result.scalar_one_or_none()
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    db_platform.name = platform.name
    db_platform.description = platform.description
    await db.commit()
    await db.refresh(db_platform)
    return db_platform


async def delete_platform(platform_name: str, db: AsyncSession):
    result = await db.execute(select(Platform).filter(Platform.name == platform_name))
    db_platform = result.scalar_one_or_none()
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    await db.delete(db_platform)
    await db.commit()
    return db_platform
