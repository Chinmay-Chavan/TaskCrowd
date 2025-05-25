# models.py
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.dialects.mysql import LONGTEXT

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    name = Column(String(100))
    avatar = Column(LONGTEXT, nullable=True)
    title = Column(String(100))
    bio = Column(Text)
    location = Column(String(100))
    email = Column(String(100))
    website = Column(String(200))
    project_types = Column(Text)  # you can store JSON-encoded list
    budget = Column(String(50))

    user = relationship("models.user.User", back_populates="profile")



