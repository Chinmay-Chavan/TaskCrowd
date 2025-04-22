from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String)  # "worker", "requester", "admin"
    # In your User model
    # Add this field to track which business posted the task

#posted_tasks = relationship("Task", back_populates="business")
