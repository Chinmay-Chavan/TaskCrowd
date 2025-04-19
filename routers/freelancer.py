from fastapi import APIRouter, Request, Depends
from fastapi.responses import RedirectResponse
from routers.auth import get_current_user
from database import User

router = APIRouter()

@router.get("/freelancer_dashboard")
async def freelancer_dashboard(request: Request, current_user: User = Depends(get_current_user)):
    if current_user.role.lower() == "freelancer":
        return {"message": f"Welcome Freelancer {current_user.username}"}
    return RedirectResponse("/login.html")
