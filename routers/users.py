# app/routers/users.py

from fastapi import APIRouter

router = APIRouter()

users = []

@router.get("/")
def get_users():
    return {"users": users}

@router.post("/")
def create_user(user: dict):
    users.append(user)
    return {"message": "User created successfully", "user": user}
