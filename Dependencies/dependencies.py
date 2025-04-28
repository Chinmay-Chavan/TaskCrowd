from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session
from typing import Optional

from database import get_db
from models.user import User

def get_user_id_from_cookie(request: Request) -> Optional[int]:
    """
    Fetch user_id directly from cookies.
    Assume you saved user_id in cookies at login time.
    """
    user_id = request.cookies.get("user_id")
    if user_id:
        try:
            return int(user_id)
        except ValueError:
            return None
    return None

async def get_current_user(
    request: Request,
    db: Session = Depends(get_db)) -> Optional[User]:
    """
    Fetch the current user based on user_id stored in cookies (no JWT).
    """
    user_id = get_user_id_from_cookie(request)
    if not user_id:
        return None  # Means guest user (not logged in)

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None  # User not found in database

    return user

def get_freelancer_user(
    current_user: User = Depends(get_current_user)) -> User:
    """
    Allow only freelancers to proceed.
    """
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please login first."
        )
    if current_user.role != "freelancer":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only freelancers can access this endpoint."
        )
    return current_user

def get_business_user(
    current_user: User = Depends(get_current_user)) -> User:
    """
    Allow only business users to proceed.
    """
    if not current_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Please login first."
        )
    if current_user.role != "business":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only business users can access this endpoint."
        )
    return current_user
