from contextlib import asynccontextmanager
from fastapi import FastAPI

import settings
from public import api as public_api
from database import create_db_and_tables


# The first part of the function, before the yield, will
# be executed before the application starts.
# https://fastapi.tiangolo.com/advanced/events/#lifespan-function
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables..")
    create_db_and_tables()
    yield

def create_app(settings=settings):
    app = FastAPI(
        docs_url="/",
        lifespan=lifespan
        )
    
    app.include_router(public_api)

    return app



       







