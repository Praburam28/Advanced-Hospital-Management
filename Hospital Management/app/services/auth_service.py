import uuid

from sqlalchemy.orm import Session

from app.models.user import User
from app.models.password_reset import PasswordReset

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

# REGISTER USER

def register_user(
    db: Session,
    user
):

    # CHECK DUPLICATE EMAIL

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:

        return {
            "success": False,
            "message": "Email already registered"
        }

    # CREATE USER

    db_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(
            user.password
        ),
        role=user.role
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return {
        "success": True,
        "message": "User Registered Successfully",
        "data": {
            "id": db_user.id,
            "name": db_user.name,
            "email": db_user.email,
            "role": db_user.role
        }
    }

# LOGIN USER

def login_user(
    db: Session,
    user
):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    # USER NOT FOUND

    if not db_user:

        return {
            "success": False,
            "message": "Invalid Email"
        }

    # INVALID PASSWORD

    if not verify_password(
        user.password,
        db_user.password
    ):

        return {
            "success": False,
            "message": "Invalid Password"
        }

    # GENERATE TOKEN

    token = create_access_token({
        "sub": db_user.email,
        "role": db_user.role
    })

    return {
    "success": True,
    "message": "Login Successful",
    "access_token": token,
    "token_type": "bearer",
    "user": {
        "id": db_user.id,
        "name": db_user.name,
        "email": db_user.email,
        "role": db_user.role
    }

}

# FORGOT PASSWORD

def forgot_password(
    db: Session,
    email: str
):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:

        return {
            "success": False,
            "message": "Email not found"
        }

    # GENERATE RESET TOKEN

    token = str(uuid.uuid4())

    reset = PasswordReset(
        email=email,
        token=token
    )

    db.add(reset)

    db.commit()

    return {
        "success": True,
        "message": "Password Reset Token Generated",
        "reset_token": token
    }

# RESET PASSWORD

def reset_password(
    db: Session,
    token: str,
    new_password: str
):

    reset = db.query(
        PasswordReset
    ).filter(
        PasswordReset.token == token
    ).first()

    # INVALID TOKEN

    if not reset:

        return {
            "success": False,
            "message": "Invalid Reset Token"
        }

    # FIND USER

    user = db.query(User).filter(
        User.email == reset.email
    ).first()

    if not user:

        return {
            "success": False,
            "message": "User Not Found"
        }

    # UPDATE PASSWORD

    user.password = hash_password(
        new_password
    )

    db.commit()

    return {
        "success": True,
        "message": "Password Reset Successful"
    }