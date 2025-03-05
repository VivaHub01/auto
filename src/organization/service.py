from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi import HTTPException
from src.organization.models import Organization
from src.organization.schemas import OrganizationOut


async def create_organization(org: OrganizationOut, db: AsyncSession):
    db_org = Organization(name=org.name, description=org.description)
    db.add(db_org)
    await db.commit()
    await db.refresh(db_org)
    return db_org


async def get_organizations(db: AsyncSession):
    result = await db.execute(select(Organization))
    return result.scalars().all()


async def get_organization_by_name(org_name: str, db: AsyncSession):
    result = await db.execute(select(Organization).filter(Organization.name == org_name))
    db_org = result.scalar_one_or_none()
    if db_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    return db_org


async def update_organization(org_name: str, org: OrganizationOut, db: AsyncSession):
    result = await db.execute(select(Organization).filter(Organization.name == org_name))
    db_org = result.scalar_one_or_none()
    if db_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    
    db_org.name = org.name
    db_org.description = org.description
    await db.commit()
    await db.refresh(db_org)
    return db_org


async def delete_organization(org_name: str, db: AsyncSession):
    result = await db.execute(select(Organization).filter(Organization.name == org_name))
    db_org = result.scalar_one_or_none()
    if db_org is None:
        raise HTTPException(status_code=404, detail="Organization not found")
    
    await db.delete(db_org)
    await db.commit()
    return db_org
