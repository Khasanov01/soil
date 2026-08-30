from fastapi import FastAPI
from fastapi import Request, Response
"""FastAPI uses Starlette Framework by default"""

print("\n Backend server is running \n")

app=FastAPI(title='landing FastAPI soil project')


@app.get("/")

async def get_greeting(request: Request, response: Response ):
    print("request:", request)
    response.status_code=200
    response.body= b"Hello from starlette"
    print("response", response)
    return response