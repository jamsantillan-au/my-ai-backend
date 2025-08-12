from sqlalchemy import Column, String, Text, Boolean, Numeric, DateTime, Date, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
import sqlalchemy as sa
import uuid
from datetime import datetime
from app.db import Base

def gen_uuid():
    return str(uuid.uuid4())

class Supplier(Base):
    __tablename__ = "suppliers"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    company_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    phone = Column(String)
    address = Column(Text)
    philgeps_status = Column(String)
    verified = Column(Boolean, default=False)
    tier = Column(String, default='free')
    hashed_password = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class SupplierProduct(Base):
    __tablename__ = "supplier_products"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    supplier_id = Column(UUID(as_uuid=True), ForeignKey("suppliers.id", ondelete="CASCADE"))
    name = Column(String)
    description = Column(Text)
    unit_price = Column(Numeric)
    uom = Column(String)
    unspsc_code = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Tender(Base):
    __tablename__ = "tenders"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    ref_number = Column(String, unique=True)
    title = Column(Text)
    procuring_entity = Column(String)
    trade_agreement = Column(String)
    procurement_mode = Column(String)
    area_of_delivery = Column(String)
    abc = Column(Numeric)
    date_published = Column(Date)
    closing_date = Column(DateTime)
    raw_html = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Match(Base):
    __tablename__ = "matches"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tender_id = Column(UUID(as_uuid=True), ForeignKey("tenders.id", ondelete="CASCADE"))
    supplier_id = Column(UUID(as_uuid=True), ForeignKey("suppliers.id", ondelete="CASCADE"))
    score = Column(Numeric)
    reason = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    tender_id = Column(UUID(as_uuid=True), ForeignKey("tenders.id"))
    supplier_id = Column(UUID(as_uuid=True), ForeignKey("suppliers.id"))
    total_amount = Column(Numeric)
    files = Column(JSONB)
    status = Column(String, default='submitted')
    created_at = Column(DateTime, default=datetime.utcnow)
