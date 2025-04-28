from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class ApplicationBase(BaseModel):
    task_id: int
    freelancer_id: int
    business_email: str

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(BaseModel):
    status: str

class ApplicationResponse(ApplicationBase):
    id: int
    status: str
    created_at: datetime
    
    class Config:
        from_attributes = True  # Changed from orm_mode = True

# For nested responses showing detailed application info
class FreelancerInfo(BaseModel):
    id: int
    name: str
    email: str
    skills: List[str]

class TaskInfo(BaseModel):
    id: int
    title: str
    description: str
    category: str
    budget: float
    deadline: datetime
    required_skills: List[str]

class ApplicationDetailResponse(BaseModel):
    id: int
    status: str
    created_at: datetime
    task: TaskInfo
    freelancer: FreelancerInfo

    class Config:
        from_attributes = True  