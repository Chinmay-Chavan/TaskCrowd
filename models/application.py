from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
from database import Base
from sqlalchemy.orm import relationship

class Application(Base):
    __tablename__ = "applications"
    
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id"), nullable=False)
    freelancer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    business_email = Column(String(100), ForeignKey("users.email"), nullable=False)  # Changed from business_email
    status = Column(Enum("pending", "accepted", "rejected", name="application_status"), default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    task = relationship("models.task.Task", back_populates="applications")
    freelancer = relationship("models.user.User", foreign_keys=[freelancer_id], back_populates="freelancer_applications")
    business = relationship("models.user.User", foreign_keys=[business_email], back_populates="business_applications")