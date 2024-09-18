from typing import Annotated

from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from .core.database import session_manager
from .endpoint import user
from .exception.entity import EntityError

# create FastAPI APP
app = FastAPI()

# include Endpoints to main App
app.include_router(user.router)


# add Exception Handler
@app.exception_handler(EntityError)
async def entity_not_found_exception_handler(request: Request, exc: EntityError):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": f"{exc.detail}"}
    )


# bind SQL tables to App
@app.on_event("startup")
def on_startup():
    session_manager.create_db_and_tables()
