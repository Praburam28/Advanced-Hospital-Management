from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Depends
)

from sqlalchemy.orm import Session

from app.models.file import FileMetadata

from app.core.dependencies import get_db

router = APIRouter(
    prefix="/files",
    tags=["Files"]
)

# ALLOWED TYPES

ALLOWED_TYPES = [
    "image/png",
    "image/jpeg",
    "application/pdf"
]

# MAX SIZE = 2MB

MAX_SIZE = 2 * 1024 * 1024

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    # FILE TYPE VALIDATION

    if file.content_type not in ALLOWED_TYPES:

        return {
            "success": False,
            "message": "Invalid file type"
        }

    content = await file.read()

    # FILE SIZE VALIDATION

    if len(content) > MAX_SIZE:

        return {
            "success": False,
            "message": "File too large"
        }

    # SAVE FILE

    path = f"uploads/{file.filename}"

    with open(path, "wb") as f:

        f.write(content)

    # STORE METADATA

    metadata = FileMetadata(
        filename=file.filename,
        filetype=file.content_type,
        filesize=str(len(content))
    )

    db.add(metadata)

    db.commit()

    db.refresh(metadata)

    return {
        "success": True,
        "message": "File Uploaded",
        "data": {
            "id": metadata.id,
            "filename": metadata.filename,
            "filetype": metadata.filetype,
            "filesize": metadata.filesize
        }
    }