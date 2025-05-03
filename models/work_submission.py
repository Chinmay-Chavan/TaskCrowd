from sqlalchemy import Column, Integer, String, Text, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base  # Adjust the import based on how you set up your Base

class WorkSubmission(Base):
    __tablename__ = "work_submissions"

    id = Column(Integer, primary_key=True, index=True)
    
    freelancer_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    project_title = Column(String(255), nullable=False)
    client_name = Column(String(255), nullable=False)
    submission_date = Column(Date, nullable=False)
    submission_title = Column(String(255), nullable=False)
    completion_status = Column(String(50), nullable=False)  # e.g., 'completed', 'in-progress'
    submission_description = Column(Text, nullable=True)
    additional_notes = Column(Text, nullable=True)
    status = Column(String(50), nullable=False)  # e.g., 'submitted', 'reviewed', etc.
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship to User
    freelancer = relationship("models.user.User", back_populates="submissions")
    # In WorkSubmission model
    files = relationship("models.submission_file.SubmissionFile", back_populates="submission", cascade="all, delete-orphan")

