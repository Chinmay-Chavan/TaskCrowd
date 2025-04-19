
from fastapi import FastAPI, Form, Request, Response, Depends, HTTPException, status
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from routers import auth, business, freelancer
from sqlalchemy.orm import Session
import smtplib 
from email.mime.text import MIMEText
from jose import JWTError
from database import Base, SessionLocal, engine, User

# ---------- App Setup ----------
app = FastAPI()

# Routers
app.include_router(auth.router)
app.include_router(business.router)
app.include_router(freelancer.router)

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

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------- Routes ----------
@app.get("/", response_class=HTMLResponse)
@app.get("/index.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about.html", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/login.html", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/register.html", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/contact.html", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/Admin_Dashboard.html", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    return templates.TemplateResponse("Admin_Dashboard.html", {"request": request})

# Route for Freelancer Dashboard
@app.get("/Freelancer_Dashboard.html", response_class=HTMLResponse)
async def freelancer_dashboard(request: Request):
    return templates.TemplateResponse("Freelancer_Dashboard.html", {"request": request})

# Route for Business Dashboard
@app.get("/Business_Dashboard.html", response_class=HTMLResponse)
async def business_dashboard(request: Request):
    return templates.TemplateResponse("Business_Dashboard.html", {"request": request})

# Route for Browse Task page
@app.get("/Browse_Task.html", response_class=HTMLResponse)
async def browse_task(request: Request):
    return templates.TemplateResponse("Browse_Task.html", {"request": request})

# Route for post task page
@app.get("/post_task.html", response_class=HTMLResponse)
async def post_task(request: Request):
    return templates.TemplateResponse("post_task.html", {"request": request})

# Route for manage task page
@app.get("/manage_task.html", response_class=HTMLResponse)
async def manage_task(request: Request):
    return templates.TemplateResponse("manage_task.html", {"request": request})

# Route for profile page
@app.get("/profile.html", response_class=HTMLResponse)
async def profile(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})


@app.get("/forgot-password.html", response_class=HTMLResponse)
async def forgot_password_get(request: Request):
    return templates.TemplateResponse("forgot-password.html", {"request": request})

# show form, verifying token first
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

    # After successful registration, generate JWT and redirect to respective dashboard
    token_data = {"sub": new_user.email, "role": new_user.role}
    access_token = create_access_token(data=token_data)

    response = RedirectResponse(
        url=f"/{new_user.role.capitalize()}_Dashboard.html", status_code=303
    )
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,  # change to True in production with HTTPS
        samesite="lax",
        max_age=1800
    )
    return response

# ---------- Login ----------
@app.post("/login", response_class=HTMLResponse)
async def login_user(
    request: Request,
    response: Response,
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    user = db.query(User).filter_by(email=email).first()

    if not user or not verify_password(password, user.password):
        return templates.TemplateResponse("login.html", {"request": request, "message": "Invalid credentials"})

    # Generate JWT
    token_data = {"sub": user.email, "role": user.role}
    access_token = create_access_token(data=token_data)

    # Set JWT in cookie
    response = RedirectResponse(
        url=f"/{user.role.capitalize()}_Dashboard.html", status_code=303
    )
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,  # change to True in production with HTTPS
        samesite="lax",
        max_age=1800
    )
    return response

#--------------Forgot-password------------------

@app.post("/forgot-password", response_class=HTMLResponse)
async def forgot_password_post(
    request: Request,
    email: str = Form(...),
    db: Session = Depends(get_db),
):
    user = db.query(User).filter_by(email=email).first()
    # Never reveal existence:
    msg = "If that email is registered, you’ll receive a link."
    if user:
        # Create a 1‑hour reset token
        token = create_access_token(
            data={"sub": user.email},
            expires_delta=timedelta(hours=1)
        )
        reset_link = f"{request.url.scheme}://{request.url.hostname}/reset-password.html?token={token}"
        send_reset_email(user.email, reset_link)

    return templates.TemplateResponse("forgot-password.html", {
        "request": request,
        "message": msg
    })

def send_reset_email(to_email: str, link: str):
    try:
        msg = MIMEText(f"Click to reset: {link}")
        msg["Subject"] = "Reset link"
        msg["From"] = "no-reply@taskcrowd.com"
        msg["To"] = to_email

        with smtplib.SMTP("smtp.gmail.com", 587, timeout=5) as smtp:
            smtp.starttls()
            smtp.login("smtp_user", "smtp_pass")
            smtp.send_message(msg)
    except Exception as e:
        print("⚠️ send_reset_email failed:", e)

# handle new password
@app.post("/reset-password", response_class=HTMLResponse)
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
