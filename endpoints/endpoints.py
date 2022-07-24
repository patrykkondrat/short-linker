import sys, os
sys.path.append(os.getcwd())
from fastapi import APIRouter, Response, status
from dependency_injector.wiring import inject
from services import IdNotFoundInDatabase, Service
from fastapi.responses import RedirectResponse
from services import Service

router = APIRouter()

service = Service()

@router.get("/get")
@inject
async def get_them_all():
    return service.get_links()


@router.get("/get/{id}")
@inject
async def get_by_id(id: int):
    try:
        return service.get_link_by_id(id)
    except IdNotFoundInDatabase:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post("/post/{id}/{long_link}")
@inject
async def do_something(id: int, long_link: str):
    return service.create_link(id, long_link)


@router.delete("/del/{id}")
@inject
async def remove(id: int):
    try:
        service.delete_link_by_id(id)
        return {'del': id}
    except IdNotFoundInDatabase:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/status")
@inject
async def _status():
    return {"status": "GIT"}


@router.get("/redirect-test", response_class=RedirectResponse)
async def redirect_fastapi():
    return RedirectResponse("https://www.facebook.com")