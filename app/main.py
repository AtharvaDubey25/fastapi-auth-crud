from fastapi import FastAPI
from .schemas import User
from . import models,database
from .routers import user,auth

models.Base.metadata.create_all(database.engine) # craete a table of the class incase there isnt one and nothing if there is already one.


app = FastAPI()


app.include_router(user.router)
app.include_router(auth.router)

