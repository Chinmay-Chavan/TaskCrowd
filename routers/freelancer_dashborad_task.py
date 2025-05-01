from fastapi import APIRouter, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import get_db
from Dependencies.dependencies import get_current_user  # your cookie-based auth dependency
from models import Application, Task, User

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/freelancer/dashboard")
def freelancer_dashboard(
    request: Request,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # Fetch accepted applications for this freelancer
    accepted_apps = (
        db.query(Application)
          .filter(
              Application.freelancer_id == current_user.id,
              Application.status == "accepted",
          )
          .all()
    )

    # Build context list, splitting comma-separated skills
    tasks = []
    for app in accepted_apps:
        task = db.query(Task).get(app.task_id)
        if not task:
            continue

        # comma-separated fields → Python lists
        freelancer_skills = []
        required_skills = [
            s.strip() for s in (task.skills or "").split(",") if s.strip()
        ]

        tasks.append({
            "freelancer_name": current_user.username,
            "freelancer_email": current_user.email,
            "freelancer_skills": [],
            "title": task.title,
            "category": task.category,
            "budget": task.budget,
            "deadline": task.deadline.strftime("%B %d, %Y"),
            "description": task.description,
            "required_skills": required_skills,
        })

    # Render with the same Jinja loop you already have
    return templates.TemplateResponse(
        "Freelancer_DashBoard.html",
        {"request": request, "tasks": tasks},
    )


@router.get("/freelancer/dashboard/debug")
def freelancer_dashboard_debug(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    # 1️⃣ All apps for this freelancer
    all_apps = (
        db.query(Application)
          .filter(Application.freelancer_id == current_user.id)
          .all()
    )

    # 2️⃣ Case-sensitive accepted
    exact_accepted = [
        a.status for a in all_apps if a.status == "accepted"
    ]

    # 3️⃣ Case-insensitive accepted
    ci_accepted = (
        db.query(Application)
          .filter(
              Application.freelancer_id == current_user.id,
              Application.status.ilike("accepted"),
          )
          .all()
    )

    return {
        "current_user_id": current_user.id,
        "total_applications": len(all_apps),
        "statuses_all_apps": [a.status for a in all_apps],
        "exactly_'accepted'": len(exact_accepted),
        "case_insensitive_'accepted'": len(ci_accepted),
    }