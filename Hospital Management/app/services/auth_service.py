from sqlalchemy.orm import Session
from app.models.user import User

from app.utils.auth import (
    hash_password,
    verify_password,
    create_access_token
)



def register_user(db: Session, data):

    existing_user = db.query(User).filter(
        User.email == data.email
    ).first()

    if existing_user:
        return None

    user = User(
        name=data.name,
        email=data.email,
        password=hash_password(data.password),
        role=data.role
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user



def login_user(db: Session, email, password):

    user = db.query(User).filter(
        User.email == email
    ).first()

    if not user:
        return None

    if not verify_password(password, user.password):
        return None

    token = create_access_token(
        {
            "id": user.id,
            "email": user.email,
            "role": user.role
        }
    )

    return token