
from fastapi import FastAPI

import endpoints


app = FastAPI()
app.include_router(router=endpoints.router)


