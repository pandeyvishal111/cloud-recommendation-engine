from fastapi import APIRouter, HTTPException

from app.schemas import UserLogin, UserRegistration
from app.services.auth_service import AuthService

router = APIRouter(tags=["auth"])


@router.post("/register")
def register_user(user: UserRegistration):
    try:
        saved = AuthService.register_user(user.email, user.password, user.full_name, user.company)
        return {
            "message": "User registered successfully.",
            "user": saved,
        }
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.post("/login")
def login_user(user: UserLogin):
    authenticated = AuthService.authenticate_user(user.email, user.password)
    if authenticated is None:
        raise HTTPException(status_code=401, detail="Invalid email or password.")
    return {
        "message": "Login successful.",
        "user": authenticated,
    }
