from fastapi import APIRouter, Response, status
from dependency_injector.wiring import inject
from services import IdNotFoundInDatabase, Service
from fastapi.responses import RedirectResponse


@router.get("/redirect-test", response_class=RedirectResponse)
async def redirect_fastapi():
    return RedirectResponse("https://www.facebook.com")