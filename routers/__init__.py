# routers/__init__.py
from fastapi import APIRouter
from .auth import router as auth
from .business import router as business
from .applications import router as applications
from .freelancer import router as freelancer
from .freelancer_dashborad_task import router as freelancer_dashboard_task
from .submit_work import router as submit_work
from .business_dashboard_task import router as business_dashboard_task  
from .profile import router as profile
from .freelancer_profile import router as freelancer_profile
from .pay import router as pay

# Create a router without a prefix - the prefix will be added in the main app

