from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def helloWorld():
    return {"message":"Hello World"}

@app.get("/items/", response_model=dict)
async def items():
    items = {"data":["orange","cherry","appel"]}
    return items