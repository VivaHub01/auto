from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from src.location.models import Location
from src.assets.models import Asset
from src.assets.schemas import AssetOut


async def create_asset(asset: AssetOut, db: AsyncSession):
    db_location = await db.execute(select(Location).filter(Location.name == asset.location_name))
    db_location = db_location.scalar_one_or_none()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    db_asset = Asset(name=asset.name, description=asset.description, location_name=asset.location_name)
    db.add(db_asset)
    await db.commit()
    await db.refresh(db_asset)
    return db_asset


async def get_assets(db: AsyncSession):
    result = await db.execute(select(Asset))
    return result.scalars().all()


async def get_asset_by_name(asset_name: str, db: AsyncSession):
    result = await db.execute(select(Asset).filter(Asset.name == asset_name))
    db_asset = result.scalar_one_or_none()
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    return db_asset


async def update_asset(asset_name: str, asset: AssetOut, db: AsyncSession):
    result = await db.execute(select(Asset).filter(Asset.name == asset_name))
    db_asset = result.scalar_one_or_none()
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    db_asset.name = asset.name
    db_asset.description = asset.description
    await db.commit()
    await db.refresh(db_asset)
    return db_asset


async def delete_asset(asset_name: str, db: AsyncSession):
    result = await db.execute(select(Asset).filter(Asset.name == asset_name))
    db_asset = result.scalar_one_or_none()
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    await db.delete(db_asset)
    await db.commit()
    return db_asset
