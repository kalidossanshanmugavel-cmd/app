from datetime import datetime, timedelta, timezone
from typing import Optional

from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from database import get_db
from repository.user_repository import UserRepository

# ==============================
# JWT Configuration
# ==============================

SECRET_KEY = "your_secret_key_change_this_in_production"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# ==============================
# Password Hashing
# ==============================

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ==============================
# Password Functions
# ==============================

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password
) -> bool:
    return pwd_context.verify(plain_password, str(hashed_password))


# ==============================
# Create JWT Token
# ==============================

def create_access_token(data: dict) -> str:
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({"exp": expire})

    return jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# ==============================
# Verify JWT Token
# ==============================

def get_current_user(
    request: Request,
    db: Session = Depends(get_db),
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
        headers={"WWW-Authenticate": "Bearer"},
    )

    # Read JWT from HttpOnly Cookie
    token = request.cookies.get("access_token")

    if token is None:
        raise credentials_exception

    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username: Optional[str] = payload.get("sub")

        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    repository = UserRepository()

    user = repository.get_user_by_username(
        db,
        username
    )

    if user is None:
        raise credentials_exception

    return user