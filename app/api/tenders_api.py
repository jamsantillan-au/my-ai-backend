from fastapi import APIRouter, Depends, Query
from app.db import get_session
from app.crud import list_tenders
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()

@router.get("/api/tenders")
async def get_tenders(trade_agreement: str = None, procurement_mode: str = None, page: int = 1, limit: int = 20, session: AsyncSession = Depends(get_session)):
    offset = (page - 1) * limit
    filters = {"trade_agreement": trade_agreement, "procurement_mode": procurement_mode}
    items = await list_tenders(session, filters, limit=limit, offset=offset)
    return {"items": items, "total": len(items)}
