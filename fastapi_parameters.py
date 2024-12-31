from fastapi import FastAPI

app = FastAPI()


@app.get("/hello/{msg}/bye")
def hello(name: str, age: int, msg: str):
    return {"name": name, "age": age, "msg": msg}