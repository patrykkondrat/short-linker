
from fastapi import FastAPI

import endpoints.endpoints as endpoints
import endpoints.redirect as redirect


app = FastAPI()
app.include_router(router=endpoints.router)
app.include_router(router=redirect.router2)

