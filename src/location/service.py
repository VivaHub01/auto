from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from src.platform.models import Platform
from src.location.models import Location
from src.location.schemas import LocationOut



async def create_location(location: LocationOut, db: AsyncSession):
    db_platform = await db.execute(select(Platform).filter(Platform.name == location.platform_name))
    db_platform = db_platform.scalar_one_or_none()
    if db_platform is None:
        raise HTTPException(status_code=404, detail="Platform not found")
    db_location = Location(name=location.name, description=location.description, platform_id=db_platform.id)
    db.add(db_location)
    await db.commit()
    await db.refresh(db_location)
    return db_location



async def get_locations(db: AsyncSession):
    result = await db.execute(select(Location))
    return result.scalars().all()



async def get_location_by_name(location_name: str, db: AsyncSession):
    result = await db.execute(select(Location).filter(Location.name == location_name))
    db_location = result.scalar_one_or_none()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location


async def update_location(location_name: str, location: LocationOut, db: AsyncSession):
    result = await db.execute(select(Location).filter(Location.name == location_name))
    db_location = result.scalar_one_or_none()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    db_location.name = location.name
    db_location.description = location.description
    await db.commit()
    await db.refresh(db_location)
    return db_location


async def delete_location(location_name: str, db: AsyncSession):
    result = await db.execute(select(Location).filter(Location.name == location_name))
    db_location = result.scalar_one_or_none()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    await db.delete(db_location)
    await db.commit()
    return db_location
