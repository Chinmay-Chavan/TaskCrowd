from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String)
    username = Column(String, nullable=True)  # "worker", "requester", "admin"

    # Relationships with simplified paths
    tasks_created = relationship("models.task.Task", back_populates="business", foreign_keys="models.task.Task.business_email")
    business_applications = relationship("models.application.Application", back_populates="business", foreign_keys="models.application.Application.business_email")
    freelancer_applications = relationship("models.application.Application", back_populates="freelancer", foreign_keys="models.application.Application.freelancer_id")
    submissions = relationship("models.work_submission.WorkSubmission", back_populates="freelancer") 