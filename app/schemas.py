from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class SupplierCreate(BaseModel):
    company_name: str
    email: EmailStr
    password: str

class SupplierOut(BaseModel):
    id: str
    company_name: str
    email: str
    verified: bool
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TenderOut(BaseModel):
    id: str
    ref_number: str
    title: Optional[str]
    procuring_entity: Optional[str]
    trade_agreement: Optional[str]
    procurement_mode: Optional[str]
    area_of_delivery: Optional[str]
    abc: Optional[float]
    date_published: Optional[datetime]
    closing_date: Optional[datetime]
    class Config:
        orm_mode = True

class SubmissionCreate(BaseModel):
    tender_id: str
    supplier_id: str
    total_amount: float
