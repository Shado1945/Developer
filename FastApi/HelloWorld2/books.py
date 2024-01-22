from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
#from uuid import UUID

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

@app.put("/{bookId}")
async def updateBook(bookId: int, book: Book):
    for i, x in enumerate(BOOKS):
        if x.id == bookId:
            BOOKS[i] = book
            return BOOKS[i]
    raise HTTPException(
        status_code = 404,
        detail=f"ID {bookId} : Does not exist"
    )

@app.delete("/{bookId}")
async def deleteBook(bookId: int):
    for i, x in enumerate(BOOKS):
        if x.id == bookId:
            del BOOKS[i]
            return f"ID: {bookId} is deleted"
    raise HTTPException(
        status_code = 404,
        detail=f"ID {bookId} : Does not exist"
    )

