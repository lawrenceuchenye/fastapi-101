from fastapi import FastAPI

#main app instance
app=FastAPI()

students={
    "1":{
        "name":"David",
        "department":"Computer Sci.",
        "mat":"2120/123645/regular"
    },
}


@app.get("/")
def index():
    return { "data":"started"}

@app.get("/student-info/{id}/info")
def student_info(id:int):
    return {"student":students[st(id)]}


