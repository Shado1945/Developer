from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates")

DOGS = [{"name":"Filo", "type":"Jack Russel", "color":"Brown"}, {"name":"Max", "type":"German Shephard", "color":"Dark Brown"}]

@router.get("/dogs")
async def dogsArray(request: Request):
    return templates.TemplateResponse("dogs.html",{"request": request, "dogs":DOGS})