from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static files (CSS, JS, Images, Video)
app.mount("/static", StaticFiles(directory="static"), name="static")



# Set up templates directory
templates = Jinja2Templates(directory="templates")

# Route for index.html
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

# Route for dashboards and task pages
@app.get("/Admin_Dashboard.html", response_class=HTMLResponse)
async def admin_dashboard(request: Request):
    return templates.TemplateResponse("Admin_DashBoard.html", {"request": request})

@app.get("/Freelancer_Dashboard.html", response_class=HTMLResponse)
async def freelancer_dashboard(request: Request):
    return templates.TemplateResponse("Freelancer_DashBoard.html", {"request": request})

@app.get("/Business_Dashboard.html", response_class=HTMLResponse)
async def business_dashboard(request: Request):
    return templates.TemplateResponse("Business_DashBoard.html", {"request": request})

@app.get("/Browse_Task.html", response_class=HTMLResponse)
async def browse_task(request: Request):
    return templates.TemplateResponse("Browse_Task.html", {"request": request})

@app.get("/post_task.html", response_class=HTMLResponse)
async def post_task(request: Request):
    return templates.TemplateResponse("post_task.html", {"request": request})

@app.get("/manage_task.html", response_class=HTMLResponse)
async def manage_task(request: Request):
    return templates.TemplateResponse("manage_task.html", {"request": request})

@app.get("/profile.html", response_class=HTMLResponse)
async def profile(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})