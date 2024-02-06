from fastapi import FastAPI
from app.routes import index, dogs

app = FastAPI()

app.include_router(index.router)
app.include_router(dogs.router)