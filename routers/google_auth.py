from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from pydantic import BaseModel
import logging
from database import get_db
from models import User
from .auth import create_access_token

# Set up logging
logger = logging.getLogger(__name__)

# Define router
google_auth_router = APIRouter()

# Define a model for the token request
class GoogleAuthRequest(BaseModel):
    token: str

# Google OAuth configurations
CLIENT_ID = "214889972007-ho958972b5o6mngratfret3mh7dmnfpv.apps.googleusercontent.com"

async def process_google_auth(token: str, role: str, db: Session):
    """
    Process Google authentication and create/update user with specified role
    """
    try:
        # Verify the Google ID token
        idinfo = id_token.verify_oauth2_token(
            token, google_requests.Request(), CLIENT_ID
        )
        
        # Check if email is verified
        if not idinfo.get('email_verified', False):
            raise HTTPException(status_code=400, detail="Email not verified with Google")
        
        # Get user info from the token
        email = idinfo['email']
        name = idinfo.get('name', '')
        
        # Check if user exists in your database
        user = db.query(User).filter_by(email=email).first()
        if not user:
            # Create new user
            user = User(
                email=email,
                name=name,
                password=None,  # No password for Google Auth users
                role=role
            )
            db.add(user)
            db.commit()
        elif user.role != role:
            # If the user exists but with a different role, update the role
            # Note: You might want to handle this differently based on your requirements
            user.role = role
            db.commit()
        
        # Create JWT token for your application
        token_data = {"sub": user.email, "role": user.role}
        access_token = create_access_token(data=token_data)
        
        return {"access_token": access_token, "token_type": "bearer"}
        
    except ValueError as e:
        # This exception is thrown for token verification errors
        logger.error(f"Google token verification error: {str(e)}")
        raise HTTPException(status_code=401, detail="Invalid Google token")
    except Exception as e:
        logger.error(f"Error in Google OAuth: {str(e)}")
        raise HTTPException(status_code=500, detail="Authentication process failed")

@google_auth_router.post("/auth/google/freelancer")
async def google_auth_freelancer(request_data: GoogleAuthRequest, db: Session = Depends(get_db)):
    """Endpoint for freelancer authentication via Google"""
    return await process_google_auth(request_data.token, "freelancer", db)
    
@google_auth_router.post("/auth/google/business")
async def google_auth_business(request_data: GoogleAuthRequest, db: Session = Depends(get_db)):
    """Endpoint for business authentication via Google"""
    return await process_google_auth(request_data.token, "business", db)