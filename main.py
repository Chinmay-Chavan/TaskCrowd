from fastapi import FastAPI, Form, UploadFile, File, Request, Response, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import FastAPI, Form, Request, Response, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext # type: ignore
from jose import JWTError, jwt # type: ignore
from datetime import datetime, timedelta, date
from routers import auth, business, freelancer, applications, freelancer_dashboard_task,submit_work
from sqlalchemy.orm import Session
import smtplib 
from email.mime.text import MIMEText
from database import Base, SessionLocal, engine, User
import shutil, os
from models import Task
from pydantic import BaseModel
from typing import List, Optional
from database import get_db
from routers.google_auth import google_auth_router 

# ---------- App Setup ----------
app = FastAPI()
UPLOAD_DIR = "static/uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Routers
app.include_router(auth)
app.include_router(business)
app.include_router(freelancer)
app.include_router(business, prefix="/business", tags=["business"])
app.include_router(freelancer, prefix="/freelancer", tags=["freelancer"])
app.include_router(google_auth_router)
app.include_router(applications)
app.include_router(freelancer_dashboard_task)
app.include_router(submit_work)
  # Commented out as freelancer_Dashboard_Task is not defined
# Static & Templates
app.mount("/static", StaticFiles(directory="static"), name="static")



templates = Jinja2Templates(directory="templates")

Base.metadata.create_all(bind=engine)

# ---------- Password Hashing ----------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# ---------- JWT Config ----------
SECRET_KEY = "MpdpKskAi4f7v489-bqjhYJpqf6oGbsb0yPWEBqwvtc"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# ---------- Routes ----------
@app.get("/", response_class=HTMLResponse)
@app.get("/index.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about.html", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/aboutb.html", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("aboutb.html", {"request": request})

@app.get("/aboutf.html", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("aboutf.html", {"request": request})

@app.get("/login.html", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register.html", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/contact.html", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/contactb.html", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contactb.html", {"request": request})

@app.get("/contactf.html", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contactf.html", {"request": request})

@app.get("/Admin_Dashboard.html", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    return templates.TemplateResponse("Admin_Dashboard.html", {"request": request})

# Route for Freelancer Dashboard
@app.get("/Freelancer_Dashboard.html", include_in_schema=False)
async def redirect_dashboard():
    return RedirectResponse(url="/freelancer/dashboard")

# Route for Business Dashboard
@app.get("/Business_Dashboard.html", response_class=HTMLResponse)
async def business_dashboard(request: Request):
    return templates.TemplateResponse("Business_Dashboard.html", {"request": request})


# Route for Browse Task page
@app.get("/requests.html", response_class=HTMLResponse)
async def browse_task(request: Request):
    return templates.TemplateResponse("requests.html", {"request": request})

# Route for post task page
@app.get("/post_task.html", response_class=HTMLResponse)
async def post_task(request: Request):
    return templates.TemplateResponse("post_task.html", {"request": request})

# Route for manage task page
@app.get("/manage_task.html", response_class=HTMLResponse)
async def manage_task(request: Request):
    return templates.TemplateResponse("manage_task.html", {"request": request})

# Route for profile page
@app.get("/profileb.html", response_class=HTMLResponse)
async def profile(request: Request):
    return templates.TemplateResponse("profileb.html", {"request": request})

@app.get("/profilef.html", response_class=HTMLResponse)
async def profile(request: Request):
    return templates.TemplateResponse("profilef.html", {"request": request})

# Route for submit_work page
@app.get("/submit_work.html", response_class=HTMLResponse)
async def submit(request: Request):
    return templates.TemplateResponse("submit_work.html", {"request": request})

# Route for forgot password page
@app.get("/forgot-password.html", response_class=HTMLResponse)
async def forgot_password_get(request: Request):
    return templates.TemplateResponse("forgot-password.html", {"request": request})

# Route for Browse_Task page
@app.get("/Browse_Task.html", response_class=HTMLResponse)
async def browse_task(request: Request, db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return templates.TemplateResponse("Browse_task.html", {
        "request": request,
        "tasks": tasks,
        "file_base_url": "static/uploaded_files/"
    })

# Route for reset password page
@app.get("/reset_password.html", response_class=HTMLResponse)
async def reset_password_get(request: Request, token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return templates.TemplateResponse("reset_password.html", {
            "request": request, "token": token
        })
    except JWTError:
        return templates.TemplateResponse("reset_password.html", {
            "request": request, "error": "Invalid or expired token."
        })
    
@app.get("/submit-work", response_class=HTMLResponse)
async def show_submit_form(request: Request):
    return templates.TemplateResponse("submit_work.html", {"request": request})

#---------- API to fetch tasks ----------
'''@app.get("/api/tasks")
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()  # Fetch all tasks from the database
    
    task_data = [{
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "budget": task.budget,
        "category": task.category,
        "deadline": task.deadline.isoformat() if isinstance(task.deadline, date) else str(task.deadline),  # Ensure date is serialized
        "skills": task.skills.split(",") if task.skills else [],
        "file_path": task.file_path
    } for task in tasks]

    return JSONResponse(content=task_data)'''
# ---------- Logout ----------
@app.get("/logout")
def logout():
    response = RedirectResponse(url="/login.html", status_code=302)
    response.delete_cookie("access_token")
    return response

# ---------- Registration ----------
@app.post("/submit", response_class=HTMLResponse)
async def handle_form(
    request: Request,
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    lusername: str = Form(...),
    role: str = Form(...),
    db: Session = Depends(get_db)
):
    existing_user = db.query(User).filter_by(email=email).first()
    if existing_user:
        return templates.TemplateResponse("register.html", {
            "request": request,
            "message": "Email already registered. Please login."
        })

    hashed_password = get_password_hash(password)
    new_user = User(username=username, email=email, password=hashed_password, lusername=lusername, role=role)
    db.add(new_user)
    db.commit()

    token_data = {"sub": new_user.email, "role": new_user.role}
    access_token = create_access_token(data=token_data)

    response = RedirectResponse(
        url=f"/{new_user.role.capitalize()}_Dashboard.html", status_code=303
    )
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        max_age=ACCESS_TOKEN_EXPIRE_MINUTES * 60
    )
    return response

# ---------- Login ----------

@app.post("/login", response_class=HTMLResponse)
async def login_user(
    request: Request,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter_by(email=email).first()

    if not user or not verify_password(password, user.password):
        return templates.TemplateResponse("login.html", {
            "request": request,
            "message1": "Invalid credentials"
        })

    # Create token with consistent data structure
    token_data = {"sub": user.email, "role": user.role}
    access_token = create_access_token(data=token_data, expires_delta=timedelta(hours=1))

    response = RedirectResponse(
        url=f"/{user.role.capitalize()}_Dashboard.html", status_code=303
    )
    
    # Set the access_token cookie
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,
        samesite="lax",
        path="/",
        max_age=3600
    )

    # Set user_id cookie separately (for cookie-based parts like apply task)
    response.set_cookie(
        key="user_id",
        value=str(user.id),
        httponly=True,
        secure=False,
        samesite="lax",
        path="/",
        max_age=3600
    )
    
    return response
# ---------- Forgot Password ----------
@app.post("/forgot-password", response_class=HTMLResponse)
async def forgot_password_post(
    request: Request,
    email: str = Form(...),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter_by(email=email).first()
    msg = "If that email is registered, you’ll receive a link."
    if user:
        token = create_access_token(
            data={"sub": user.email},
            expires_delta=timedelta(hours=1)
        )
        reset_link = f"http://localhost:8000/reset_password.html?token={token}"
        send_reset_email(user.email, reset_link)

    return templates.TemplateResponse("forgot-password.html", {
        "request": request,
        "message": msg
    })

def send_reset_email(to_email: str, link: str):
    try:
        msg = MIMEText(f"Click to reset: {link}")
        msg["Subject"] = "Reset link"
        msg["From"] = "taskcrowd121@gmail.com"
        msg["To"] = to_email

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp:
            smtp.starttls()
            smtp.login("taskcrowd121@gmail.com", "hobg zdew rsqs yisg")
            smtp.send_message(msg)
    except Exception as e:
        print("⚠️ send_reset_email failed:", e)

# ---------- Reset Password ----------
@app.post("/reset_password", response_class=HTMLResponse)
async def reset_password_post(
    request: Request,
    token: str = Form(...),
    new_password: str = Form(...),
    db: Session = Depends(get_db),
):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        user = db.query(User).filter_by(email=email).first()
        if not user:
            raise JWTError()
    except JWTError:
        return templates.TemplateResponse("reset_password.html", {
            "request": request, "error": "Invalid or expired token."
        })

    user.password = get_password_hash(new_password)
    db.commit()
    return RedirectResponse("/login.html?reset=success", status_code=303)


# ---------- Post Task ----------
@app.post("/post-task", response_class=HTMLResponse)
async def post_task_submit(
    request: Request,
    title: str = Form(...),
    description: str = Form(...),
    budget: float = Form(...),
    category: str = Form(...),
    deadline: str = Form(...),
    skills: str = Form(...),
    file: UploadFile = File(None),
    db: Session = Depends(get_db)
):
    # Get user from token(Business email fetching to store in db)
    token = request.cookies.get("access_token")
    
    # Add token validation check
    if not token:
        return templates.TemplateResponse("login.html", {
            "request": request,
            "message": "Your session has expired. Please login again."
        })
        
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub") 
        role = payload.get("role") # Extract email from token
        
        if not email:
            return templates.TemplateResponse("login.html", {
                "request": request,
                "message": "Invalid session. Please login again."
            })
            
        if role != "business":
            return templates.TemplateResponse("login.html", {
                "request": request,
                "message": "You are not authorized to post tasks."
            })
    except JWTError as e:
        print(f"JWT Error: {str(e)}")
        return templates.TemplateResponse("login.html", {
            "request": request,
            "message": "Your session is invalid. Please login again."
        })
    
    try:
        # Ensure upload directory exists
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        file_path = None

        if file:
            if file.content_type.startswith("text/") or file.content_type.startswith("application/") or file.content_type.startswith("image/"):
                # Save file to static/uploads
                file_location = os.path.join(UPLOAD_DIR, file.filename)

                # Prevent large file uploads (>1 GB)
                file.file.seek(0, os.SEEK_END)
                file_size = file.file.tell()
                file.file.seek(0)

                if file_size > 1024 * 1024 * 1024:
                    return templates.TemplateResponse("post_task.html", {
                        "request": request,
                        "message": "File too large. Max 1GB allowed."
                    })

                with open(file_location, "wb") as buffer:
                    shutil.copyfileobj(file.file, buffer)

                # Store relative path to access via /static
                file_path = file.filename

        # Save task to DB
        new_task = Task(
            title=title,
            description=description,
            budget=budget,
            category=category,
            deadline=deadline,
            skills=skills,
            file_path=file_path,
            business_email=email  # Store the email of the user who posted the task
        )
        db.add(new_task)
        db.commit()
        return RedirectResponse("Business_Dashboard.html", status_code=303)

    except Exception as e:
        print(f"Error posting task: {str(e)}")
        return templates.TemplateResponse("post_task.html", {
            "request": request,
            "message": f"There was an error posting your task: {str(e)}"
        })

@app.get("/api/tasks")
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()  # Fetch all tasks from the database
    
    task_data = [{
        "id": task.id,
        "title": task.title,
        "description": task.description,
        "budget": task.budget,
        "category": task.category,
        "deadline": task.deadline.isoformat() if isinstance(task.deadline, date) else str(task.deadline),  # Ensure date is serialized
        "skills": task.skills.split(",") if task.skills else [],
        "file_path": task.file_path
    } for task in tasks]

    return JSONResponse(content=task_data)


