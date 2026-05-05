from sqlalchemy import Column, Integer, String
from app.database.db import Base


class FileMetadata(Base):

    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String(255))

    content_type = Column(String(100))

    size = Column(String(100))