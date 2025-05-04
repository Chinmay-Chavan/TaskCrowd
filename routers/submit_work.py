# routers/submit_work.py

from fastapi import APIRouter, Depends, Form, UploadFile, File, status
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import datetime
import os

from database import get_db
from Dependencies.dependencies import get_current_user
from models import WorkSubmission, SubmissionFile, User  

router = APIRouter()


@router.post("/submit-work")
async def submit_work(
    projectTitle: str                = Form(...),
    clientName: str                  = Form(...),
    submissionDate: str              = Form(...),   
    submissionTitle: str             = Form(...),
    completionStatus: str            = Form(...),
    submissionDescription: str       = Form(...),
    additionalNotes: Optional[str]   = Form(None),
    status: str           = Form(...),   
    files: List[UploadFile]          = File(None),
    db: Session                      = Depends(get_db),
    current_user: User               = Depends(get_current_user),
):
    # 1) Create the WorkSubmission record
    submission = WorkSubmission(
        freelancer_id=current_user.id,
        project_title=projectTitle,
        client_name=clientName,
        submission_date=datetime.strptime(submissionDate, "%Y-%m-%d").date(),
        submission_title=submissionTitle,
        completion_status=completionStatus,
        submission_description=submissionDescription,
        additional_notes=additionalNotes,
        status=status,
        created_at=datetime.utcnow(),
    )
    db.add(submission)
    db.commit()
    db.refresh(submission)

    # 2) Ensure upload directory exists
    upload_dir = os.path.join("uploads", "submissions", str(submission.id))
    os.makedirs(upload_dir, exist_ok=True)

    # 3) Save each uploaded file and record it
    for upload in files or []:
        # unique filename to avoid clashes
        dest_path = os.path.join(upload_dir, upload.filename)
        with open(dest_path, "wb") as f:
            content = await upload.read()
            f.write(content)

        # record it in a SubmissionFile table (if you have one)
        file_record = SubmissionFile(
            submission_id=submission.id,
            file_name=upload.filename,
            file_path=dest_path,
            uploaded_at=datetime.utcnow(),
        )
        db.add(file_record)

    db.commit()

    # 4) Redirect back to the freelancer dashboard
    return RedirectResponse(
        url="/freelancer/dashboard",
        status_code=status.HTTP_303_SEE_OTHER
    )
