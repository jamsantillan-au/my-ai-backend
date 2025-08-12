from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import SupplierCreate, Token, SupplierOut
from app.db import get_session
from app.crud import create_supplier, get_supplier_by_email
from app.auth import hash_password, create_access_token, verify_password
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Body

router = APIRouter(prefix="/api/auth")

@router.post("/signup", response_model=SupplierOut)
async def signup(payload: SupplierCreate, session: AsyncSession = Depends(get_session)):
    existing = await get_supplier_by_email(session, payload.email)
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed = hash_password(payload.password)
    supplier = await create_supplier(session, payload.company_name, payload.email, hashed)
    token = create_access_token(str(supplier.id))
    return supplier

@router.post("/login", response_model=Token)
async def login(payload: SupplierCreate, session: AsyncSession = Depends(get_session)):
    supplier = await get_supplier_by_email(session, payload.email)
    if not supplier or not verify_password(payload.password, supplier.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(str(supplier.id))
    return {"access_token": token, "token_type": "bearer"}
