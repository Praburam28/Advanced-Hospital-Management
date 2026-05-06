from fastapi import (
    APIRouter,
    Depends
)

from fastapi.security import (
    OAuth2PasswordRequestForm
)

from sqlalchemy.orm import Session

from app.schemas.auth_schema import (
    RegisterSchema,
    ForgotPasswordSchema,
    ResetPasswordSchema
)

from app.services.auth_service import (
    register_user,
    login_user,
    forgot_password,
    reset_password
)

from app.core.dependencies import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# REGISTER

@router.post("/register")
def register(
    user: RegisterSchema,
    db: Session = Depends(get_db)
):

    result = register_user(
        db,
        user
    )

    return result

# LOGIN

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):

    # CONVERT FORM DATA

    class LoginData:

        email = form_data.username

        password = form_data.password

    result = login_user(
        db,
        LoginData
    )

    return result

# FORGOT PASSWORD

@router.post("/forgot-password")
def forgot(
    request: ForgotPasswordSchema,
    db: Session = Depends(get_db)
):

    result = forgot_password(
        db,
        request.email
    )

    return result

# RESET PASSWORD

@router.post("/reset-password")
def reset(
    request: ResetPasswordSchema,
    db: Session = Depends(get_db)
):

    result = reset_password(
        db,
        request.token,
        request.new_password
    )

    return result