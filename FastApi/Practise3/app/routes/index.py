from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

@router.get("/")
async def indexMethod(request: Request):
    return templates.TemplateResponse("index.html",{"request": request, "header":"This is the home page"})