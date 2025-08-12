from fastapi import APIRouter, Depends, HTTPException
from app.db import get_session
from app.models import Tender, Supplier, Match, SupplierProduct
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

router = APIRouter()

@router.post("/api/match/run")
async def run_match(tender_ref: str, session: AsyncSession = Depends(get_session)):
    # load tender
    q = await session.execute(select(Tender).filter_by(ref_number=tender_ref))
    tender = q.scalar_one_or_none()
    if not tender:
        raise HTTPException(404, "Tender not found")

    q = await session.execute(select(Supplier))
    suppliers = q.scalars().all()
    inserted = 0
    for s in suppliers:
        score = 0
        reasons = []
        # simplistic rules - refine later
        # check unspsc match via products
        q2 = await session.execute(select(SupplierProduct).filter_by(supplier_id=s.id))
        prods = q2.scalars().all()
        if prods:
            score += 20; reasons.append("Has product")
        # region match placeholder
        # price match placeholder
        if s.verified:
            score += 20; reasons.append("PhilGEPS verified")
        match = Match(tender_id=tender.id, supplier_id=s.id, score=score, reason=";".join(reasons))
        session.add(match)
        inserted += 1
    await session.commit()
    return {"inserted": inserted}
