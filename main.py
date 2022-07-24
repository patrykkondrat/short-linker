
from fastapi import FastAPI

import endpoints
import redirect


app = FastAPI()
app.include_router(router=endpoints.router)
app.include_router(router=redirect.router2)

