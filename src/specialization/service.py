from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from src.specialization.models import Specialization, ClassificationLevel
from src.specialization.schemas import (
    SpecializationIn,
    ClassificationLevelIn,
)

async def create_specialization(specialization: SpecializationIn, db: AsyncSession):
    result = await db.execute(select(Specialization).filter(Specialization.name == specialization.name))
    if result.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Specialization with this name already exists")
    db_specialization = Specialization(
        name=specialization.name,
        description=specialization.description,
        bid=specialization.bid,
        classification_name=specialization.classification_name,
    )
    db.add(db_specialization)
    await db.commit()
    await db.refresh(db_specialization)
    return db_specialization

async def get_specializations(db: AsyncSession):
    result = await db.execute(select(Specialization))
    return result.scalars().all()

async def get_specialization_by_name(specialization_name: str, db: AsyncSession):
    result = await db.execute(select(Specialization).filter(Specialization.name == specialization_name))
    db_specialization = result.scalar_one_or_none()
    if db_specialization is None:
        raise HTTPException(status_code=404, detail="Specialization not found")
    return db_specialization

async def update_specialization(specialization_name: str, specialization: SpecializationIn, db: AsyncSession):
    result = await db.execute(select(Specialization).filter(Specialization.name == specialization_name))
    db_specialization = result.scalar_one_or_none()
    if db_specialization is None:
        raise HTTPException(status_code=404, detail="Specialization not found")

    db_specialization.name = specialization.name
    db_specialization.description = specialization.description
    db_specialization.bid = specialization.bid
    db_specialization.classification_name = specialization.classification_name
    await db.commit()
    await db.refresh(db_specialization)
    return db_specialization

async def delete_specialization(specialization_name: str, db: AsyncSession):
    result = await db.execute(select(Specialization).filter(Specialization.name == specialization_name))
    db_specialization = result.scalar_one_or_none()
    if db_specialization is None:
        raise HTTPException(status_code=404, detail="Specialization not found")
    await db.delete(db_specialization)
    await db.commit()
    return db_specialization

async def create_classification_level(classification_level: ClassificationLevelIn, db: AsyncSession):
    db_classification_level = ClassificationLevel(
        level_name=classification_level.level_name,
        description=classification_level.description,
        classification_level_rank=classification_level.classification_level_rank,
        specialization_name=classification_level.specialization_name,
    )
    db.add(db_classification_level)
    await db.commit()
    await db.refresh(db_classification_level)
    return db_classification_level

async def get_classification_levels(db: AsyncSession):
    result = await db.execute(select(ClassificationLevel))
    return result.scalars().all()

async def get_classification_level_by_name(level_name: str, db: AsyncSession):
    result = await db.execute(select(ClassificationLevel).filter(ClassificationLevel.level_name == level_name))
    db_classification_level = result.scalar_one_or_none()
    if db_classification_level is None:
        raise HTTPException(status_code=404, detail="Classification level not found")
    return db_classification_level

async def update_classification_level(level_name: str, classification_level: ClassificationLevelIn, db: AsyncSession):
    result = await db.execute(select(ClassificationLevel).filter(ClassificationLevel.level_name == level_name))
    db_classification_level = result.scalar_one_or_none()
    if db_classification_level is None:
        raise HTTPException(status_code=404, detail="Classification level not found")

    db_classification_level.level_name = classification_level.level_name
    db_classification_level.description = classification_level.description
    db_classification_level.classification_level_rank = classification_level.classification_level_rank
    db_classification_level.specialization_name = classification_level.specialization_name
    await db.commit()
    await db.refresh(db_classification_level)
    return db_classification_level

async def delete_classification_level(level_name: str, db: AsyncSession):
    result = await db.execute(select(ClassificationLevel).filter(ClassificationLevel.level_name == level_name))
    db_classification_level = result.scalar_one_or_none()
    if db_classification_level is None:
        raise HTTPException(status_code=404, detail="Classification level not found")
    await db.delete(db_classification_level)
    await db.commit()
    return db_classification_level