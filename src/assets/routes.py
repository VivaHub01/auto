from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import get_async_session
from src.assets.schemas import AssetOut
from src.assets.service import create_asset, get_assets, get_asset_by_name, update_asset, delete_asset


assets_router = APIRouter(prefix="/assets", tags=["Assets"])


@assets_router.post('/', response_model=AssetOut)
async def create_assets(asset: AssetOut, db: AsyncSession = Depends(get_async_session)):
    return await create_asset(asset, db)

@assets_router.get("/", response_model=list[AssetOut])
async def get_assets(db: AsyncSession = Depends(get_async_session)):
    return await get_assets(db)

@assets_router.get("/{asset_name}", response_model=AssetOut)
async def get_asset_by_name(asset_name: str, db: AsyncSession = Depends(get_async_session)):
    return await get_asset_by_name(asset_name, db)

@assets_router.put("/{asset_name}", response_model=AssetOut)
async def update_assets(asset_name: str, asset: AssetOut, db: AsyncSession = Depends(get_async_session)):
    return await update_asset(asset_name, asset, db)

@assets_router.delete("/{asset_name}", response_model=AssetOut)
async def delete_assets(asset_name: str, db: AsyncSession = Depends(get_async_session)):
    return await delete_asset(asset_name, db)
