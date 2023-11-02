from fastapi import FastAPI

#main app instance
app=FastAPI()


users=[]


@app.get("/")
def index():
    return {"basuc":"UI"}

@app.get("/users")
def get_users():
    return  users

@app.post("/users")
def create_users(user):
    users.append(user)
    return {"name":"added"}

