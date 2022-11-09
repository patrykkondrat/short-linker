import os
import sys

from fastapi import FastAPI

sys.path.append("/home/patryk/programowanko/python/short-linker/endpoints")

import endpoints.redirect
import endpoints.db_service


app = FastAPI()
app.include_router(router=endpoints.db_service.router)
app.include_router(router=endpoints.redirect.router2)
