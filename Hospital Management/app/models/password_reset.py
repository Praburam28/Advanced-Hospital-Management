from sqlalchemy import Column, Integer, String
from app.config.database import Base

class PasswordReset(Base):

    __tablename__ = "password_resets"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    token = Column(String)