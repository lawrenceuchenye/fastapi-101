from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional,List

#main app instance
app=FastAPI()


users=[]

#create model for validating input
class User(BaseModel):
    email:str
    name:str
    is_valid:Optional[bool]

@app.get("/")
def index():
    return {"basuc":"UI"}

@app.get("/users",response_model=List[User])
def get_users():
    return  users

@app.post("/users")
def create_users(user:User):
    users.append(user)
    return {"name":"added"}

