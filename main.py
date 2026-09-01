from fastapi import Body, FastAPI, status, Path, Query
from fastapi import Request, Response, HTTPException
from provider import Student, students
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
@app.get("/mit/all", response_model=dict[int, Student])
def get_students():
    #model>database > data
    return students

# Path params
@app.get("/mit/student/{id}", response_model=Student)
def get_student_by_id(id : int = Path(ge=1)):
    if id not in students:
        raise HTTPException(
        status_code=400, detail=f"Student Id={id} not found"
            )
    return students[id]


# Query params
@app.get("/mit/student", response_model=list[Student])
def get_student_by_name(name : str = Query(min_length=3, max_length=20)):
    result=[s for s in students.values() if s.name == name ]
    return result



@app.post("/mit/edit/{id}", response_model=Student)
def edit_student(
    id: int= Path(ge=1),
    name: str=Query(min_length=3, max_length=20),
    age: int=Query(gt=20)
):
    print(f"The path: {id=} and query: {name=} , {age=}")

    if id not in students:
        raise HTTPException(status_code=400, detail=f"Student {id=} not found")
    
    student = students[id]
    student.name=name
    student.age=age
    return student

#DTO validation
@app.post("/mit/add", response_model=Student)
def add_student(student: Student=Body(...)):
    print(f"the req.body: {student}")

    if student.id in student:
        raise HTTPException(status_code=400, detail= f"the student id {student.id} already exists")
    students[student.id]=student
    return student