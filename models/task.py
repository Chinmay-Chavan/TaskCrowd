from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey
from datetime import datetime
from database import Base
from sqlalchemy.orm import relationship

class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    budget = Column(Float, nullable=False)
    category = Column(String(100), nullable=False)
    deadline = Column(String(100), nullable=False)
    skills = Column(Text, nullable=False)  # Store as comma-separated string
    created_at = Column(DateTime, default=datetime.utcnow)
    file_path = Column(String(255), nullable=True)
        
    # Foreign key to users table using email (not id)
    business_email = Column(String, ForeignKey("users.email"))

    # Relationships with simplified paths
    applications = relationship("models.application.Application", back_populates="task")
    business = relationship("models.user.User", back_populates="tasks_created", foreign_keys=[business_email])