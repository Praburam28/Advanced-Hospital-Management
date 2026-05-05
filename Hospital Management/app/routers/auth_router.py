from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from jose import jwt

from app.database.db import get_db
from app.schemas.user_schema import UserCreate

from app.schemas.forgot_password_schema import (
    ForgotPasswordRequest,
    ResetPasswordRequest
)

from app.services.auth_service import (
    register_user,
    login_user
)

from app.models.user import User

from app.utils.auth import (
    create_reset_token,
    hash_password
)

from app.utils.response import (
    success_response,
    error_response
)

from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(
    data: UserCreate,
    db: Session = Depends(get_db)
):

    user = register_user(db, data)

    if not user:

        return error_response(
            "Email already exists"
        )

    return success_response(
        "User Registered Successfully",
        {
            "id": user.id,
            "email": user.email,
            "role": user.role
        }
    )


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    token = login_user(
        db,
        form_data.username,
        form_data.password
    )

    if not token:

        return error_response(
            "Invalid Credentials"
        )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.post("/forgot-password")
def forgot_password(
    data: ForgotPasswordRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == data.email
    ).first()

    if not user:

        return error_response(
            "Email not found"
        )

    token = create_reset_token(user.email)

    return success_response(
        "Reset Token Generated",
        {
            "reset_token": token
        }
    )


@router.post("/reset-password")
def reset_password(
    data: ResetPasswordRequest,
    db: Session = Depends(get_db)
):

    payload = jwt.decode(
        data.token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    email = payload.get("sub")

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:

        return error_response(
            "Invalid Token"
        )

    user.password = hash_password(
        data.new_password
    )

    db.commit()

    return success_response(
        "Password Reset Successful"
    )