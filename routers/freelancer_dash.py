from fastapi import APIRouter, Depends, Request, HTTPException
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from database import SessionLocal, get_db
from models import Task, User
from fastapi.responses import JSONResponse
from datetime import date

# Import your JWT constants from main.py
SECRET_KEY = "MpdpKskAi4f7v489-bqjhYJpqf6oGbsb0yPWEBqwvtc"
ALGORITHM = "HS256"

router = APIRouter(
    prefix="/api/freelancer",
    tags=["freelancer"]
)

# Dependency to get the current freelancer user
def get_current_freelancer(request: Request, db: Session = Depends(get_db)):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        role = payload.get("role")
        
        if role != "freelancer":
            raise HTTPException(status_code=403, detail="Not authorized")
            
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

# Get all available tasks for freelancers
@router.get("/available-tasks")
async def get_available_tasks(
    current_user: User = Depends(get_current_freelancer),
    db: Session = Depends(get_db)
):
    # Here you might want to filter out tasks that the freelancer has already applied to
    # or tasks that are already completed
    tasks = db.query(Task).all()
    
    task_data = [{
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "budget": task.budget,
        "category": task.category,
        "deadline": task.deadline.isoformat() if isinstance(task.deadline, date) else str(task.deadline),
        "skills": task.skills.split(",") if task.skills else [],
        # Potentially hide business_email for privacy, or provide business name instead
    } for task in tasks]
    
    return task_data

# You can add more freelancer-specific endpoints below
# For example: apply to task, view applied tasks, etc.