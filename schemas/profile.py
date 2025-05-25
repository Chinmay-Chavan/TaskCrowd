from pydantic import BaseModel, HttpUrl, EmailStr
from typing import List, Optional

class ProfileBase(BaseModel):
    name: Optional[str]
    avatar: Optional[str]
    title: Optional[str]
    bio: Optional[str]
    location: Optional[str]
    email: Optional[EmailStr]
    website: Optional[HttpUrl]
    project_types: Optional[List[str]]
    budget: Optional[str]

class ProfileCreate(ProfileBase):
    pass

class ProfileRead(ProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
