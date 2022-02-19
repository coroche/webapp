from fastapi import Request, APIRouter, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import Optional
from app.library.wordleLogic import returnWordList

templates = Jinja2Templates(directory="templates")

router = APIRouter() 

def parseColours(results):
    results = [['g' if x == '#6aaa64' else x for x in result] for result in results]
    results = [['o' if x == '#c9b458' else x for x in result] for result in results]
    results = [[x if x in ['g','o'] else '.' for x in result] for result in results]
    results = [''.join(result) for result in results]
    return results

@router.get("/wordle", response_class=HTMLResponse)
async def wordle_get(request: Request):

    return templates.TemplateResponse("wordle.html", context={"request": request, 'colour11': '#ffffff', 'colour12': '#ffffff', 'colour13': '#ffffff', 'colour14': '#ffffff', 'colour15': '#ffffff', 'colour21': '#ffffff', 'colour22': '#ffffff', 'colour23': '#ffffff', 'colour24': '#ffffff', 'colour25': '#ffffff', 'colour31': '#ffffff', 'colour32': '#ffffff', 'colour33': '#ffffff', 'colour34': '#ffffff', 'colour35': '#ffffff', 'colour41': '#ffffff', 'colour42': '#ffffff', 'colour43': '#ffffff', 'colour44': '#ffffff', 'colour45': '#ffffff', 'colour51': '#ffffff', 'colour52': '#ffffff', 'colour53': '#ffffff', 'colour54': '#ffffff', 'colour55': '#ffffff'})

@router.post("/wordle_guess", response_class=HTMLResponse)
def wordle_post(request: Request, letter11: Optional[str] = Form(''), letter12: Optional[str] = Form(''), letter13: Optional[str] = Form(''), letter14: Optional[str] = Form(''), letter15: Optional[str] = Form(''),  letter21: Optional[str] = Form(''), letter22: Optional[str] = Form(''), letter23: Optional[str] = Form(''), letter24: Optional[str] = Form(''), letter25: Optional[str] = Form(''),  letter31: Optional[str] = Form(''), letter32: Optional[str] = Form(''), letter33: Optional[str] = Form(''), letter34: Optional[str] = Form(''), letter35: Optional[str] = Form(''),  letter41: Optional[str] = Form(''), letter42: Optional[str] = Form(''), letter43: Optional[str] = Form(''), letter44: Optional[str] = Form(''), letter45: Optional[str] = Form(''),  letter51: Optional[str] = Form(''), letter52: Optional[str] = Form(''), letter53: Optional[str] = Form(''), letter54: Optional[str] = Form(''), letter55: Optional[str] = Form(''),  colour11: Optional[str] = Form(''), colour12: Optional[str] = Form(''), colour13: Optional[str] = Form(''), colour14: Optional[str] = Form(''), colour15: Optional[str] = Form(''),  colour21: Optional[str] = Form(''), colour22: Optional[str] = Form(''), colour23: Optional[str] = Form(''), colour24: Optional[str] = Form(''), colour25: Optional[str] = Form(''),  colour31: Optional[str] = Form(''), colour32: Optional[str] = Form(''), colour33: Optional[str] = Form(''), colour34: Optional[str] = Form(''), colour35: Optional[str] = Form(''),  colour41: Optional[str] = Form(''), colour42: Optional[str] = Form(''), colour43: Optional[str] = Form(''), colour44: Optional[str] = Form(''), colour45: Optional[str] = Form(''),  colour51: Optional[str] = Form(''), colour52: Optional[str] = Form(''), colour53: Optional[str] = Form(''), colour54: Optional[str] = Form(''), colour55: Optional[str] = Form('') ):
    guesses = [letter11 + letter12 + letter13 + letter14 + letter15, letter21 + letter22 + letter23 + letter24 + letter25, letter31 + letter32 + letter33 + letter34 + letter35, letter41 + letter42 + letter43 + letter44 + letter45, letter51 + letter52 + letter53 + letter54 + letter55]
    guesses = [guess for guess in guesses if guess != '']
    
    results = [[colour11, colour12, colour13, colour14, colour15], [ colour21, colour22, colour23, colour24, colour25], [ colour31, colour32, colour33, colour34, colour35], [ colour41, colour42, colour43, colour44, colour45], [ colour51, colour52, colour53, colour54, colour55]]
    results = parseColours(results)

    wordList = returnWordList(guesses, results)
    wordList = "\n".join(wordList)
    print(wordList)
    return templates.TemplateResponse('wordle.html', context={'request': request, 'wordList': wordList, 'letter11': letter11, 'letter12': letter12, 'letter13': letter13, 'letter14': letter14, 'letter15': letter15, 'letter21': letter21, 'letter22': letter22, 'letter23': letter23, 'letter24': letter24, 'letter25': letter25, 'letter31': letter31, 'letter32': letter32, 'letter33': letter33, 'letter34': letter34, 'letter35': letter35, 'letter41': letter41, 'letter42': letter42, 'letter43': letter43, 'letter44': letter44, 'letter45': letter45, 'letter51': letter51, 'letter52': letter52, 'letter53': letter53, 'letter54': letter54, 'letter55': letter55, 'colour11': colour11, 'colour12': colour12, 'colour13': colour13, 'colour14': colour14, 'colour15': colour15, 'colour21': colour21, 'colour22': colour22, 'colour23': colour23, 'colour24': colour24, 'colour25': colour25, 'colour31': colour31, 'colour32': colour32, 'colour33': colour33, 'colour34': colour34, 'colour35': colour35, 'colour41': colour41, 'colour42': colour42, 'colour43': colour43, 'colour44': colour44, 'colour45': colour45, 'colour51': colour51, 'colour52': colour52, 'colour53': colour53, 'colour54': colour54, 'colour55': colour55})
