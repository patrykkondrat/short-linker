from fastapi import APIRouter, Response, status
from dependency_injector.wiring import inject
from services import NotFoundId, Service, NotFoundId


router = APIRouter()

Service = Service()

@router.get("/get/all")
@inject
async def get_them_all():
    return Service.get_links()


@router.get("/get/{id}")
@inject
async def get_by_id(id: int):
    return Service.get_link_by_id(id)


@router.post("post/{id}/{long_link}")
@inject
async def do_something(id, long_link):
    return Service.create_link(id,long_link)


@router.delete("del/{id}")
@inject
async def remove(id):
    Service.delete_link_by_id(id)

@router.get("/status")
async def status():
    return {"status": "GIT"}