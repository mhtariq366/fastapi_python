from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class AvailableSubjects(str, Enum):
    medical = 'pre-medical'
    engineering = 'pre-engineering'
    arts = 'arts'

subjects = {
    'medical': ["Biology", "Chemistry", "Physics"],
    'engineering': ["Maths", "Chemistry", "Physics"],
    'arts' : ["English", "History"]
}

@app.get("/get_subject/{name}")
async def get_subject(name: AvailableSubjects):
    return subjects.get(name)

