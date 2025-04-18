from fastapi import FastAPI, Form, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# Mount static files (CSS, JS, Images, Video)
app.mount("/static", StaticFiles(directory="static"), name="static")
# Set up templates directory
templates = Jinja2Templates(directory="templates")

# Database setup
DATABASE_URL = "mysql+pymysql://root:root@localhost/mydb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define User table
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    password = Column(String(100))
    lusername = Column(String(100))
    email = Column(String(100))
    role = Column(String(100))

# Create tables if they do not exist
Base.metadata.create_all(bind=engine)

# Route for index.html
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/index.html", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Route for about.html
@app.get("/about.html", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# Route for login.html
@app.get("/login.html", response_class=HTMLResponse)
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

# Route for register.html
@app.get("/register.html", response_class=HTMLResponse)
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

# Route for contact.html
@app.get("/contact.html", response_class=HTMLResponse)
async def contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

# Route for Admin Dashboard
@app.get("/Admin_Dashboard.html", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    return templates.TemplateResponse("Admin_DashBoard.html", {"request": request})

# Route for Freelancer Dashboard
@app.get("/Freelancer_Dashboard.html", response_class=HTMLResponse)
async def freelancer_dashboard(request: Request):
    return templates.TemplateResponse("Freelancer_DashBoard.html", {"request": request})

# Route for Business Dashboard
@app.get("/Business_Dashboard.html", response_class=HTMLResponse)
async def business_dashboard(request: Request):
    return templates.TemplateResponse("Business_DashBoard.html", {"request": request})

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

# Route for handling user registration form submission
@app.post("/submit", response_class=RedirectResponse)
async def handle_form(username: str = Form(...), email: str = Form(...), password: str = Form(...), lusername: str = Form(...),role: str = Form(...)):
    db = SessionLocal()
    # Create a new user instance
    new_user = User(username=username, email=email, password=password, lusername=lusername, role=role)
    # Add the new user to the database
    db.add(new_user)
    db.commit()
    db.close()

    #Redirect based on role
    if role == "freelancer":
        return RedirectResponse("/Freelancer_Dashboard.html", status_code=303)
    elif role == "business":
        return RedirectResponse("/Business_Dashboard.html", status_code=303)
    else:
    # Redirect back to the index page after form submission
        return RedirectResponse("/", status_code=303)

# Check if the user already exists
@app.post("/login", response_class=HTMLResponse)
async def login_user(request: Request, username: str = Form(...), password: str = Form(...)):
    # Create a new session for the DB query
    db = SessionLocal()
    
    # Query the user by username and password
    user = db.query(User).filter_by(username=username, password=password).first()
    db.close()
    
    if user and user.password == password:
        # Check the user's role and redirect accordingly
        if user.role == "freelancer":
            return RedirectResponse("/Freelancer_Dashboard.html", status_code=303)
        elif user.role == "business":
            return RedirectResponse("/Business_Dashboard.html", status_code=303)
        else:
            return templates.TemplateResponse("login.html", {"request": request, "message": "Unknown user role"})
    else:
        # If the user doesn't exist or credentials are incorrect
        return templates.TemplateResponse("login.html", {"request": request, "message": "Invalid credentials"})
