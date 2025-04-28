from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime

from database import get_db
from models.user import User
from models.task import Task
from models.application import Application
from schemas.application import ApplicationCreate, ApplicationResponse, ApplicationUpdate
from Dependencies.dependencies import get_current_user

router = APIRouter(
    prefix="/applications",
    tags=["applications"],
)

templates = Jinja2Templates(directory="templates")

# Apply for a task (for freelancers)

@router.post("/apply/{task_id}")
async def apply_for_task(
    task_id: int,
    request: Request,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user),
):
    # Check if user is logged in
    if not current_user:
        return JSONResponse(
            content={"error": "Please login to apply."},
            status_code=401
        )

    # Check if user is freelancer
    if current_user.role != "freelancer":
        return JSONResponse(
            content={"error": "Only freelancers can apply for tasks."},
            status_code=403
        )

    # Get task details
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return JSONResponse(
            content={"error": "Task not found. Please try again."},
            status_code=404
        )
    
    # Check if already applied
    existing_application = db.query(Application).filter(
        Application.task_id == task_id,
        Application.freelancer_id == current_user.id
    ).first()
    
    if existing_application:
        return HTMLResponse(
            content="<script>alert('You have already applied for this task.'); window.history.back();</script>",
            status_code=400
        )

    # Create new application
    new_application = Application(
        task_id=task_id,
        freelancer_id=current_user.id,
        business_email=task.business_email,
        status="pending"
    )
    
    db.add(new_application)
    db.commit()
    db.refresh(new_application)
    
    return HTMLResponse(
        content="<script>alert('Application submitted successfully'); window.history.back();</script>",
        status_code=200
    )


# View business requests (for businesses)
@router.get("/requests.html", response_class=HTMLResponse)

async def view_requests(
    request: Request, 
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user),
):
    # Check if user is logged in
    if not current_user:
        return RedirectResponse(url="/login.html")
    
    # Check if user is logged in
    print("Logged in user:", current_user.email)

    # Check if user is business
    if current_user.role != "business":
        return HTMLResponse(
            content="<script>alert('Only business users can view applications.'); window.history.back();</script>",
            status_code=403
        )

    # Get all applications for this business
    applications = db.query(Application)\
        .filter(Application.business_email == current_user.email).all()
    
    # Check if applications exist
    print("Applications for business:", len(applications))

    application_details = []
    now = datetime.now()
    
    for app in applications:
        task = db.query(Task).filter(Task.id == app.task_id).first()
        freelancer = db.query(User).filter(User.id == app.freelancer_id).first()
        
        application_details.append({
            "id": app.id,
            "status": app.status,
            "created_at": app.created_at,
            "task": {
                "id": task.id,
                "title": task.title,
                "description": task.description,
                "budget": task.budget,
                "deadline": task.deadline,
                "category": task.category,
                "required_skills": task.skills.split(",") if task and task.skills else []
            } if task else {},
            "freelancer": {
                "id": freelancer.id,
                "username": freelancer.username,
                "email": freelancer.email,
            } if freelancer else {}
        })
    
    return templates.TemplateResponse("requests.html", {
        "request": request,
        "applications": application_details,
        "now": now
    })


# Update application status (accept/reject)
@router.post("/requests/{application_id}/update", response_model=dict)
async def update_application_status(
    application_id: int,
    status: str = Form(...),
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_current_user),
):
    # Check if user is logged in
    if not current_user:
        raise HTTPException(status_code=401, detail="Please login")

    # Check if user is business
    if current_user.role != "business":
        raise HTTPException(status_code=403, detail="Only business users can update applications")

    # Get application
    application = db.query(Application)\
        .filter(Application.id == application_id)\
        .filter(Application.business_email == current_user.email).first()
    
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    # Update status
    if status not in ["accepted", "rejected"]:
        raise HTTPException(status_code=400, detail="Invalid status")
    
    application.status = status
    db.commit()
    
    return {"message": f"Application {status} successfully"}
