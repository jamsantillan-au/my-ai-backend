import asyncio
from app.db import engine
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Supplier, Tender
from datetime import datetime, timedelta
import uuid

async def seed():
    async with AsyncSession(engine) as session:
        s1 = Supplier(company_name="Acme Supplies", email="acme@example.com", verified=True)
        s2 = Supplier(company_name="Beta Traders", email="beta@example.com", verified=False)
        session.add_all([s1, s2])
        t1 = Tender(ref_number="TND-001", title="Office chairs", procuring_entity="Agency A", trade_agreement="Local", procurement_mode="Small Value Procurement", abc=50000, date_published=datetime.utcnow().date(), closing_date=datetime.utcnow()+timedelta(days=10))
        t2 = Tender(ref_number="TND-002", title="Canned goods", procuring_entity="Agency B", trade_agreement="Local", procurement_mode="Shopping", abc=150000, date_published=datetime.utcnow().date(), closing_date=datetime.utcnow()+timedelta(days=7))
        session.add_all([t1, t2])
        await session.commit()

if __name__ == "__main__":
    asyncio.run(seed())
