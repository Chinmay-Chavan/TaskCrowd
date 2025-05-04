from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session, joinedload
from models import WorkSubmission,SubmissionFile,User  # your SQLAlchemy models: Submission, SubmissionFile, User
from Dependencies.dependencies import  get_current_user
from database import get_db  # your database session dependency

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/business/dashboard")
def business_dashboard(request: Request,
                       db: Session = Depends(get_db),
                       current_user: User = Depends(get_current_user)):
    # Fetch all submissions addressed to this business user
    submissions = (
        db.query(WorkSubmission)
          .filter(WorkSubmission.client_name == current_user.username)
          .options(
            # eager‑load related files and freelancer info
            joinedload(WorkSubmission.files),
            joinedload(WorkSubmission.freelancer),
          )
          .all()
    )
    return templates.TemplateResponse(
        "Business_Dashboard.html",
        {"request": request, "submissions": submissions}
    )

@router.get("/download/{file_id}")
def download_file(file_id: int, db: Session = Depends(get_db)):
    file = db.query(SubmissionFile).get(file_id)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(
        path=file.file_path,
        media_type="application/octet-stream",
        filename=file.file_name
    )
