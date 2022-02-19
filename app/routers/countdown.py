from fastapi import Request, APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.library.SolveBoard import cleanSolutions

templates = Jinja2Templates(directory="templates")

router = APIRouter()

@router.get("/countdown", response_class=HTMLResponse)
async def countdown_get(request: Request):

    return templates.TemplateResponse("countdown.html", {"request": request})

@router.post("/countdown_solved", response_class=HTMLResponse)
def countdown_post(request: Request, target: int = Form(...), number1: int = Form(...), number2: int = Form(...), number3: int = Form(...), number4: int = Form(...), number5: int = Form(...), number6: int = Form(...)):
    solutions = cleanSolutions([number1,number2,number3,number4,number5,number6],target)
    bestSolution = "\n".join(solutions[0])
    #result = [5]
    return templates.TemplateResponse('countdown.html', context={'request': request, 'solution': bestSolution, 'target': target, 'number1': number1, 'number2': number2, 'number3': number3, 'number4': number4, 'number5': number5, 'number6': number6})
