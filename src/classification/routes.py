from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from src.db.database import get_async_session
from src.classification.schemas import ClassificationOut
from src.classification.service import create_classification, get_classifications, get_classification_by_name, update_classification, delete_classification


classification_router = APIRouter(prefix="/classifications", tags=["Classification"])


@classification_router.post('/', response_model=ClassificationOut)
async def create_classification(classification: ClassificationOut, db: AsyncSession = Depends(get_async_session)):
    return await create_classification(classification, db)

@classification_router.get("/", response_model=list[ClassificationOut])
async def get_classifications(db: AsyncSession = Depends(get_async_session)):
    return await get_classifications(db)

@classification_router.get("/{classification_name}", response_model=ClassificationOut)
async def get_classification_by_name(classification_name: str, db: AsyncSession = Depends(get_async_session)):
    return await get_classification_by_name(classification_name, db)

@classification_router.put("/{classification_name}", response_model=ClassificationOut)
async def update_classification(classification_name: str, classification: ClassificationOut, db: AsyncSession = Depends(get_async_session)):
    return await update_classification(classification_name, classification, db)

@classification_router.delete("/{classification_name}", response_model=ClassificationOut)
async def delete_classification(classification_name: str, db: AsyncSession = Depends(get_async_session)):
    return await delete_classification(classification_name, db)
