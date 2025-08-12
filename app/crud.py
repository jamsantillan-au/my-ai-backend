from sqlalchemy.future import select
from app.models import Supplier, Tender, Submission, Match, SupplierProduct
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

async def create_supplier(session: AsyncSession, company_name, email, hashed_password):
    supplier = Supplier(company_name=company_name, email=email, hashed_password=hashed_password)
    session.add(supplier)
    await session.commit()
    await session.refresh(supplier)
    return supplier

async def get_supplier_by_email(session: AsyncSession, email):
    q = await session.execute(select(Supplier).filter_by(email=email))
    return q.scalar_one_or_none()

async def list_tenders(session: AsyncSession, filters: dict, limit: int = 20, offset: int = 0):
    q = select(Tender)
    if filters.get('trade_agreement'):
        q = q.filter(Tender.trade_agreement == filters['trade_agreement'])
    if filters.get('procurement_mode'):
        q = q.filter(Tender.procurement_mode == filters['procurement_mode'])
    q = q.offset(offset).limit(limit)
    res = await session.execute(q)
    return res.scalars().all()

# add other crud functions similarly...
