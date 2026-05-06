from jose import jwt, JWTError

from datetime import (
    datetime,
    timedelta
)

from passlib.context import CryptContext

from fastapi.security import (
    OAuth2PasswordBearer
)

from fastapi import HTTPException

SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60

# SWAGGER AUTH

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

# PASSWORD HASHING

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# HASH PASSWORD

def hash_password(password: str):

    return pwd_context.hash(password)

# VERIFY PASSWORD

def verify_password(
    plain_password,
    hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )

# CREATE TOKEN

def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# VERIFY TOKEN

def verify_token(token: str):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid or Expired Token"
        )