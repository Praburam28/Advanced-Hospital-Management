from sqlalchemy import Column, Integer, String
from app.config.database import Base

class User(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

    # Admin Doctor Patient
    role = Column(String)