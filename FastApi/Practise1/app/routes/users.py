from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter()

class Users(BaseModel):
    id: int = Field(gt=0)
    fullname: str = Field(min_length = 1)
    name: str = Field(min_length = 1)
    surname: str = Field(min_length = 1)

#fake database
users_read = [
    {"id":1, "fullname":"Rohan Viljoen", "name":"Rohan", "surname":"Viljoen"},
    {"id":2, "fullname":"Roxanne de le rosa", "author":"Roxanne", "surname":"Viljoen"}
]

@router.get("/user", tags=["Users"])
async def getUser():
    return {"message":users_read}

@router.post("/user", tags=["Users"])
async def postUser(user: Users):
    users_read.append(user)
    return user

@router.put("/user/{userId}", tags=["Users"])
async def putUser(userId: int, user: Users):
    for i,x in enumerate(users_read):
        if x.id == userId:
            users_read[i] = user
            return users_read[i]
    raise HTTPException(
        status_code = 404,
        detail = f"User Id {userId}, does not exist" 
    )

@router.delete("/user/{userId}", tags=["Users"])
async def deleteUser(userId: int):
    for i,x in enumerate(users_read):
        if x == userId:
            del userId[i]
            return f"User id of {userId} is deleted"
    raise HTTPException(
        status_code = 404,
        detail = f"User Id of {userId}, does not exist"
    )