# app/main.py

from fastapi import FastAPI
from routers import users

app = FastAPI()

# Include routers
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the API"}