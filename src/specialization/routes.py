from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from src.specialization.service import (
    create_specialization,
    get_specializations,
    get_specialization_by_name,
    update_specialization,
    delete_specialization,
    create_classification_level,
    get_classification_levels,
    get_classification_level_by_name,
    update_classification_level,
    delete_classification_level,
)
from src.specialization.schemas import (
    SpecializationIn,
    SpecializationOut,
    ClassificationLevelIn,
    ClassificationLevelOut,
)
from src.db.database import get_async_session

specialization_router = APIRouter(prefix="/specializations", tags=["specializations"])

@specialization_router.post("/", response_model=SpecializationOut)
async def create_specialization_route(
    specialization: SpecializationIn,
    db: AsyncSession = Depends(get_async_session)
):
    new_specialization = await create_specialization(specialization, db)
    return new_specialization

@specialization_router.get("/", response_model=List[SpecializationOut])
async def get_specializations_route(db: AsyncSession = Depends(get_async_session)):
    return await get_specializations(db)

@specialization_router.get("/{specialization_name}", response_model=SpecializationOut)
async def get_specialization_by_name_route(specialization_name: str, db: AsyncSession = Depends(get_async_session)):
    return await get_specialization_by_name(specialization_name, db)

@specialization_router.put("/{specialization_name}", response_model=SpecializationOut)
async def update_specialization_route(specialization_name: str, specialization: SpecializationIn, db: AsyncSession = Depends(get_async_session)):
    return await update_specialization(specialization_name, specialization, db)

@specialization_router.delete("/{specialization_name}", response_model=SpecializationOut)
async def delete_specialization_route(specialization_name: str, db: AsyncSession = Depends(get_async_session)):
    return await delete_specialization(specialization_name, db)

@specialization_router.post("/classification-levels/", response_model=ClassificationLevelOut)
async def create_classification_level_route(
    classification_level: ClassificationLevelIn,
    db: AsyncSession = Depends(get_async_session)
):
    db_classification_level = await create_classification_level(classification_level, db)
    return db_classification_level

@specialization_router.get("/classification-levels/", response_model=List[ClassificationLevelOut])
async def get_classification_levels_route(db: AsyncSession = Depends(get_async_session)):
    return await get_classification_levels(db)

@specialization_router.get("/classification-levels/{level_name}", response_model=ClassificationLevelOut)
async def get_classification_level_by_name_route(level_name: str, db: AsyncSession = Depends(get_async_session)):
    return await get_classification_level_by_name(level_name, db)

@specialization_router.put("/classification-levels/{level_name}", response_model=ClassificationLevelOut)
async def update_classification_level_route(level_name: str, classification_level: ClassificationLevelIn, db: AsyncSession = Depends(get_async_session)):
    return await update_classification_level(level_name, classification_level, db)

@specialization_router.delete("/classification-levels/{level_name}", response_model=ClassificationLevelOut)
async def delete_classification_level_route(level_name: str, db: AsyncSession = Depends(get_async_session)):
    return await delete_classification_level(level_name, db)