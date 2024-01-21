from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    #id: UUID
    id: int = Field(gt=0)
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=-1,lt=101)

BOOKS = []

@app.get("/")
async def readApi():
    return BOOKS

@app.get("/{name}")
async def readName(name: str):
    return {'Welcome': name}

@app.post("/")
async def createBook(book: Book):
    BOOKS.append(book)
    return book
