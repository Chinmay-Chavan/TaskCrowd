from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from database import SessionLocal, get_db
from models import Task, User
from fastapi.responses import JSONResponse
from datetime import date
import os

# Import your JWT constants from main.py
SECRET_KEY = "MpdpKskAi4f7v489-bqjhYJpqf6oGbsb0yPWEBqwvtc"
ALGORITHM = "HS256"

router = APIRouter(
    prefix="/api/business",
    tags=["business"]
)

# Dependency to get the current business user
def get_current_business(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        role = payload.get("role")
        
        if role != "business":
            raise HTTPException(status_code=403, detail="Not authorized")
            
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Get tasks posted by the business
@router.get("/tasks")
async def get_business_tasks(
    current_user: User = Depends(get_current_business),
    db: Session = Depends(get_db)
):
    tasks = db.query(Task).filter(Task.business_email == current_user.email).all()
    
    task_data = [{
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "budget": task.budget,
        "category": task.category,
        "deadline": task.deadline.isoformat() if isinstance(task.deadline, date) else str(task.deadline),
        "skills": task.skills.split(",") if task.skills else [],
        "file_path": task.file_path,
        # You can add more fields here as needed
    } for task in tasks]
    
    return task_data

# Add more business-specific endpoints below
# For example: update task, delete task, view applications, etc.