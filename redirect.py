from fastapi import APIRouter
from dependency_injector.wiring import inject
from fastapi.responses import RedirectResponse
from services import session
import model
router2 = APIRouter()

@router2.get('{long_link}')
@inject
async def redirect_page(long_link):
    with session:
        linker = session.query(model.Links).filter(model.Links.long_link == long_link).first()
    return linker
