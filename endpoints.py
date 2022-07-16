from xml.etree.ElementInclude import include
from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from .services import Service


router = APIRouter()


@router.get('/get/all/')
@include
async def get_them_all():
    return Service.get_links()


@router.get(f'/get/{_id}')
@include
async def get_by_id(_id: int):
    try:
        return Service.get_link_by_id()
    except IdFoundInDatabase:
        return Response(status_code=status.HTTP_404_NOT_FOUND)


@router.post(f'post/{id}/{long_link}')
@include
async def do_something(id, long_link):
