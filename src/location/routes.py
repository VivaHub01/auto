from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import get_async_session
from src.location.schemas import LocationOut
from src.location.service import create_location, get_locations, get_location_by_name, update_location, delete_location


location_router = APIRouter(prefix="/locations", tags=["Location"])


@location_router.post('/', response_model=LocationOut)
async def create_location_view(location: LocationOut, db: AsyncSession = Depends(get_async_session)):
    return await create_location(location, db)


@location_router.get("/", response_model=list[LocationOut])
async def get_locations_view(db: AsyncSession = Depends(get_async_session)):
    return await get_locations(db)


@location_router.get("/{location_name}", response_model=LocationOut)
async def get_location_by_name_view(location_name: str, db: AsyncSession = Depends(get_async_session)):
    return await get_location_by_name(location_name, db)


@location_router.put("/{location_name}", response_model=LocationOut)
async def update_location_view(location_name: str, location: LocationOut, db: AsyncSession = Depends(get_async_session)):
    return await update_location(location_name, location, db)


@location_router.delete("/{location_name}", response_model=LocationOut)
async def delete_location_view(location_name: str, db: AsyncSession = Depends(get_async_session)):
    return await delete_location(location_name, db)
