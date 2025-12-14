from fastapi import FastAPI

from app.api.routers.link import router
from app.db.models import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)