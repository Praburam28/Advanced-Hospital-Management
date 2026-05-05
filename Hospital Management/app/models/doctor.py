from sqlalchemy import Column, Integer, String
from app.database.db import Base


class Doctor(Base):

    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))

    specialization = Column(String(100))

    experience = Column(Integer)