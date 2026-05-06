from fastapi import (
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from app.config.database import (
    SessionLocal
)

from app.core.security import (
    oauth2_scheme,
    verify_token
)

# DATABASE

def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()

# CURRENT USER

def get_current_user(
    token: str = Depends(
        oauth2_scheme
    )
):

    payload = verify_token(token)

    return payload

# ROLE CHECK

def role_required(roles: list):

    def checker(
        user=Depends(
            get_current_user
        )
    ):

        if user["role"] not in roles:

            raise HTTPException(
                status_code=403,
                detail="Access Denied"
            )

        return user

    return checker