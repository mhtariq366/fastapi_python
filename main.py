from fastapi import FastAPI

app = FastAPI()

subjects = {
    'pre-medical': ["Biology", "Chemistry", "Physics"],
    'pre-engineering': ["Maths", "Chemistry", "Physics"],
    'arts' : ["English", "History"]
}

@app.get("/get_subject/{name}")
async def get_subject(name):
    if name not in subjects.keys():
        return f'Please select only from {subjects.keys()}'
    return subjects.get(name)

