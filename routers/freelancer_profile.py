from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json

from models.FreelancerProfile import FreelancerProfile
from schemas.freelancer_profile import (
    FreelancerProfileCreate,
    FreelancerProfileRead
)
from Dependencies.dependencies import get_db, get_current_user

router = APIRouter()

# CRUD utilities

def get_freelancer_profile(db: Session, user_id: int):
    """Retrieve a freelancer profile by user_id."""
    return (
        db.query(FreelancerProfile)
          .filter(FreelancerProfile.user_id == user_id)
          .first()
    )


def upsert_freelancer_profile(
    db: Session,
    user_id: int,
    data_in: FreelancerProfileCreate
):
    """Create or update a freelancer profile for the given user."""
    prof = get_freelancer_profile(db, user_id)
    payload = data_in.dict()
    # JSON-encode skills list
    if payload.get("skills") is not None:
        payload["skills"] = json.dumps(payload["skills"])

    if prof:
        for key, value in payload.items():
            setattr(prof, key, value)
    else:
        prof = FreelancerProfile(user_id=user_id, **payload)
        db.add(prof)

    db.commit()
    db.refresh(prof)
    return prof

# API endpoints

@router.get(
    "/api/freelancer/profile",
    response_model=FreelancerProfileRead,
    summary="Get current user's freelancer profile"
)
def read_freelancer_profile(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    prof = get_freelancer_profile(db, current_user.id)
    if not prof:
        # return defaults if none exists
        return FreelancerProfileRead(
            id=0,
            user_id=current_user.id,
            name="",
            avatar="",
            title="",
            bio="",
            location="",
            email=current_user.email,
            website="",
            skills=[],
            hourly_rate=""
        )
    # decode skills JSON
    prof.skills = json.loads(prof.skills or "[]")
    return prof

@router.post(
    "/api/freelancer/profile",
    response_model=FreelancerProfileRead,
    summary="Create or update current user's freelancer profile"
)
def upsert_freelancer_profile_endpoint(
    payload: FreelancerProfileCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    prof = upsert_freelancer_profile(db, current_user.id, payload)
    # decode skills JSON
    prof.skills = json.loads(prof.skills or "[]")
    return prof
