from fastapi import APIRouter, Depends, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.usuario import Usuario
from app.auth import get_admin, hash_senha


router = APIRouter(prefix="/usuarios", tags={"Usuários"})

templates = Jinja2Templates(directory="app/templates")

# Listar todos os usarios
@router.get("/")
def listar_usarios(
    request: Request,
    db: Session = Depends(get_db),
    admin = Depends(get_admin), # Bloqueia quem não é admin
):
    #Pegar todos os usuarios do banco de dados
    usuarios = db.query(Usuario).order_by(Usuario.nome).all()

    return templates.TemplateResponse(
        request,
        "usuarios/index.html",
        {
            "request": request,
            "admin": admin,
            "usuarios": usuarios
        }
    )