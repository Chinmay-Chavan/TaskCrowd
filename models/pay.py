from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from sqlalchemy.sql import func
from database import Base  # your existing Base from SQLAlchemy

class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True, index=True)
    razorpay_order_id = Column(String(100), nullable=False)
    razorpay_payment_id = Column(String(100), nullable=False)
    razorpay_signature = Column(String(255), nullable=False)
    customer_name = Column(String(100))
    customer_email = Column(String(100))
    customer_mobile = Column(String(15))
    customer_address = Column(Text)
    amount = Column(Float)
    currency = Column(String(10))
    status = Column(String(20), default="success")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
