from fastapi import FastAPI
from pydantic import BaseModel

#main app instance
app=FastAPI()


users=[]


class User(BaseModel):
    email:str
    name:str
    is_valid:bool
    is_active:bool

@app.get("/")
def index():
    return {"basuc":"UI"}

@app.get("/users")
def get_users():
    return  users

@app.post("/users")
def create_users(user:User):
    users.append(user)
    return {"name":"added"}

