from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json

from schemas.profile import ProfileCreate, ProfileRead
from Dependencies.dependencies import get_db, get_current_user
from models.profile import Profile

router = APIRouter()

# CRUD functions (included here for self-containment)

def get_profile_by_user(db: Session, user_id: int):
    return db.query(Profile).filter(Profile.user_id == user_id).first()

def create_or_update_profile(db: Session, user_id: int, profile_in: ProfileCreate):
    profile = get_profile_by_user(db, user_id)
    data = profile_in.dict()
    if data.get("project_types") is not None:
        data["project_types"] = json.dumps(data["project_types"])
    if profile:
        for key, value in data.items():
            setattr(profile, key, value)
    else:
        profile = Profile(user_id=user_id, **data)
        db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

# API routes

@router.get("/api/profile", response_model=ProfileRead)
def read_profile(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    profile = get_profile_by_user(db, current_user.id)
    if not profile:
        return ProfileRead(
            id=0,
            user_id=current_user.id,
            name="",
            avatar="",
            title="",
            bio="",
            location="",
            email=current_user.email,
            website="",
            project_types=[],
            budget=""
        )
    profile.project_types = json.loads(profile.project_types or "[]")
    return profile

@router.post("/api/profile", response_model=ProfileRead)
def update_profile(
    profile_in: ProfileCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    profile = create_or_update_profile(db, current_user.id, profile_in)
    profile.project_types = json.loads(profile.project_types or "[]")
    return profile
