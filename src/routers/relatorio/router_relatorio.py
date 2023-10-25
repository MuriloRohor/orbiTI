from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="./src/public/templates")

router = APIRouter()

@router.get('/', response_class=HTMLResponse)
def relatorio_main(request: Request):
    titulo_page = "Dashboard"
    return templates.TemplateResponse("relatorio/main.html", {"request": request, "titulo": titulo_page})

@router.get('/estoque', response_class=HTMLResponse)
def relatorio_main(request: Request):
    titulo_page = "Dashboard Estoque"
    return templates.TemplateResponse("relatorio/estoque.html", {"request": request, "titulo":titulo_page})
