from fastapi import FastAPI
from app.api import users, items
from app.db.session import engine
from app.db import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(items.router, prefix="/items", tags=["items"])
