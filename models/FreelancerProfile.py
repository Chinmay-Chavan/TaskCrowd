from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.orm import relationship
from database import Base

class FreelancerProfile(Base):
    __tablename__ = "freelancer_profiles"

    id          = Column(Integer, primary_key=True, index=True)
    user_id     = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    name        = Column(String(100))
    avatar      = Column(LONGTEXT, nullable=True)      # base64 or URL
    title       = Column(String(100))
    bio         = Column(Text)
    location    = Column(String(100))
    email       = Column(String(100))
    website     = Column(String(200))
    skills      = Column(Text)      # JSON-encoded list
    hourly_rate = Column(String(50))

    user = relationship("models.user.User", back_populates="freelancer_profile")


