from fastapi import APIRouter, Depends, HTTPException, status, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from database import get_db
from schemas.user_schema import UserCreate, UserResponse
from services.user_service import UserService
from auth import create_access_token, get_current_user

router = APIRouter()
service = UserService()

@router.post("/register", response_model=UserResponse)
def register(request: UserCreate, db: Session = Depends(get_db)):
    user = service.register_user(db, request)

    if user is None:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    return user

@router.post("/login")
def login(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = service.authenticate_user(
        db,
        form_data.username,
        form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={"sub": user.username}
    )

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,      # Change to True when using HTTPS in production
        samesite="lax",
        max_age=1800
    )

    return {
        "message": "Login successful"
    }

@router.get("/me")
def read_users_me(current_user = Depends(get_current_user)):
    return current_user

@router.post("/logout")
def logout(response: Response):

    response.delete_cookie(
        key="access_token",
        httponly=True,
        samesite="lax"
    )

    return {
        "message": "Logged out successfully"
    }