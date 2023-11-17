from typing import Annotated

from fastapi import FastAPI

from .core.database import create_db_and_tables
from .endpoint import user

# create FastAPI APP
app = FastAPI()

# include Endpoints to main App
app.include_router(user.router)


# bind SQL tables to App
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
