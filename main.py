from fastapi import FastAPI
from fastapi import Request, Response, HTTPException
from provider import students
"""FastAPI uses Starlette Framework by default"""

print("\n Backend server is running \n")

app=FastAPI(title='landing FastAPI soil project')


@app.get("/")

async def get_greeting(request: Request) -> str :
    print("request:", request)
    return "Hello from starlette"

@app.get("/message", response_model=dict)
async def get_message():
    return {"message" : "Hi, MIT"}


#FastAPI handler JSON
@app.get("/mit/all", response_model=dict[int, dict])
def get_students():
    #model>database > data
    return students

# Path params
@app.get("/mit/student/{id}", response_model=dict)
def get_student_by_id(id : int):
    if id not in students:
        raise HTTPException(
        status_code=400, detail=f"Student Id={id} not found"
            )
    return students[id]


# Query params
@app.get("/mit/student", response_model=list[dict])
def get_student_by_name(name : str):
    result=[s for s in students.values() if s["name"] == name ]
    return result