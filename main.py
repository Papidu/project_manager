from contextlib import asynccontextmanager

import uvicorn
from core.models import Base, db_helper
from fastapi import FastAPI
from api_v1 import router as router_v1
from users.views import router as router_user


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(lifespan=lifespan, debug=True)
app.include_router(router=router_v1, prefix="/api/v1")
app.include_router(router=router_user, prefix="/user")


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
