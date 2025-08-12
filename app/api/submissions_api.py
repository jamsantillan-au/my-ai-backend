from fastapi import APIRouter, Depends, HTTPException
from app.schemas import SubmissionCreate
from app.db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Submission

router = APIRouter()

@router.post("/api/submissions")
async def submit_quote(payload: SubmissionCreate, session: AsyncSession = Depends(get_session)):
    sub = Submission(tender_id=payload.tender_id, supplier_id=payload.supplier_id, total_amount=payload.total_amount)
    session.add(sub)
    await session.commit()
    await session.refresh(sub)
    return {"id": str(sub.id), "status": sub.status}
