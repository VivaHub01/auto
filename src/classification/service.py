from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from src.assets.models import Asset
from src.classification.models import Classification
from src.classification.schemas import ClassificationOut


async def create_classification(classification: ClassificationOut, db: AsyncSession):
    db_asset = await db.execute(select(Asset).filter(Asset.name == classification.asset_name))
    db_asset = db_asset.scalar_one_or_none()
    if db_asset is None:
        raise HTTPException(status_code=404, detail="Asset not found")
    db_classification = Classification(name=classification.name, description=classification.description, asset_name=classification.asset_name)
    db.add(db_classification)
    await db.commit()
    await db.refresh(db_classification)
    return db_classification


async def get_classifications(db: AsyncSession):
    result = await db.execute(select(Classification))
    return result.scalars().all()


async def get_classification_by_name(classification_name: str, db: AsyncSession):
    result = await db.execute(select(Classification).filter(Classification.name == classification_name))
    db_classification = result.scalar_one_or_none()
    if db_classification is None:
        raise HTTPException(status_code=404, detail="Classification not found")
    return db_classification


async def update_classification(classification_name: str, classification: ClassificationOut, db: AsyncSession):
    result = await db.execute(select(Classification).filter(Classification.name == classification_name))
    db_classification = result.scalar_one_or_none()
    if db_classification is None:
        raise HTTPException(status_code=404, detail="Classification not found")
    db_classification.name = classification.name
    db_classification.description = classification.description
    await db.commit()
    await db.refresh(db_classification)
    return db_classification


async def delete_classification(classification_name: str, db: AsyncSession):
    result = await db.execute(select(Classification).filter(Classification.name == classification_name))
    db_classification = result.scalar_one_or_none()
    if db_classification is None:
        raise HTTPException(status_code=404, detail="Classification not found")
    await db.delete(db_classification)
    await db.commit()
    return db_classification
