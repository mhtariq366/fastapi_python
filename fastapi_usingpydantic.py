from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Greeting(BaseModel):
    first :str
    last :str


@app.post("/")
async def greet(greetings: Greeting):
    return {"first": greetings.first, "last":greetings.last}