from sqlalchemy import Column, Integer, String
from app.config.database import Base

class FileMetadata(Base):

    __tablename__ = "files"

    id = Column(Integer, primary_key=True, index=True)

    filename = Column(String, nullable=False)

    filetype = Column(String, nullable=False)

    filesize = Column(String, nullable=False)