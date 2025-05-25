from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional

class FreelancerProfileBase(BaseModel):
    name: Optional[str]
    avatar: Optional[str]
    title: Optional[str]
    bio: Optional[str]
    location: Optional[str]
    email: Optional[EmailStr]
    website: Optional[HttpUrl]
    skills: Optional[List[str]]
    hourly_rate: Optional[str]

class FreelancerProfileCreate(FreelancerProfileBase):
    pass

class FreelancerProfileRead(FreelancerProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
