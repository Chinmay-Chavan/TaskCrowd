from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base  # Adjust based on your structure

class SubmissionFile(Base):
    __tablename__ = "submission_files"

    id = Column(Integer, primary_key=True, index=True)
    
    submission_id = Column(Integer, ForeignKey("work_submissions.id"), nullable=False)
    file_name = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)  # Full or relative path to the uploaded file
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    # Relationship back to submission
    submission = relationship("models.work_submission.WorkSubmission", back_populates="files")
