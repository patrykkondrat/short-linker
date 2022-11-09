from fastapi import APIRouter
from dependency_injector.wiring import inject
from fastapi.responses import RedirectResponse

from service import services

router2 = APIRouter()
serv = services.Service()
@router2.get("/{id}", response_class=RedirectResponse)
@inject
async def redirect_fastapi(id):
    redirect_link = serv.get_by_id(id)
    return RedirectResponse(redirect_link.long_link, status_code=301)