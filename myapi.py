from fastapi import FastAPI

#main app instance
app=FastAPI()

@app.get("/")
def index():
    return { "data":"started"}
