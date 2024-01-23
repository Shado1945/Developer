from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()

class Books(BaseModel):
    id: int = Field(gt=0)
    title: str = Field(min_length = 1)
    author: str = Field(min_length = 1)
    description: str = Field(min_length = 1)

#fake database
books_read = [
    {"id":1, "title":"Rohan Learning Api", "author":"Rohan Viljoen", "description":"This is way to learn api programing"},
    {"id":2, "title":"Roxy is funny", "author":"Roxanne de le rosa", "description":"My girl is so funny"}
]

@router.get("/books", tags=["Books"])
async def getBooks():
    return {"message": books_read}

@router.post("/books", tags=["Books"])
async def postBooks(book: Books):
    books_read.append(book)
    return book

@router.put("/books/{bookId}", tags=["Books"])
async def putBooks(bookId: int, book: Books):
    for i, x in enumerate(books_read):
        if x.id == bookId:
            books_read[i] = book 
            return books_read[i]
    raise HTTPException(
        status_code = 404,
        detail = f"ID {bookId}, does not exist"
    )

@router.delete("/books/{bookId}", tags=["Books"])
async def delBooks(bookId: int):
    for i, x in enumerate(books_read):
        if x.id == bookId:
            del books_read[i]
            return f"ID {bookId} is delete"
    raise HTTPException(
        status_code = 404,
        detail = f"ID {bookId}, does not exist"
    )