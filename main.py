from fastapi import FastAPI
from fastapi import Request, Response
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