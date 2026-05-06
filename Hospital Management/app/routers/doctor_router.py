from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import or_

from app.models.doctor import Doctor
from app.schemas.doctor_schema import DoctorSchema
from app.core.dependencies import get_db, role_required

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)

# ADD DOCTOR (ADMIN ONLY)

@router.post("/")
def add_doctor(
    doctor: DoctorSchema,
    db: Session = Depends(get_db),
    user=Depends(role_required(["Admin"]))
):

    db_doctor = Doctor(**doctor.dict())

    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)

    return {
        "success": True,
        "message": "Doctor Added",
        "data": {
            "id": db_doctor.id,
            "name": db_doctor.name,
            "specialization": db_doctor.specialization,
            "experience": db_doctor.experience
        }
    }

# GET ALL + SEARCH DOCTORS (IMPORTANT FEATURE)

@router.get("/")
def search_doctors(
    search: str = "",
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Doctor)

    # SEARCH by name OR specialization
    if search:

        query = query.filter(
            or_(
                Doctor.name.ilike(f"%{search}%"),
                Doctor.specialization.ilike(f"%{search}%")
            )
        )

    doctors = query.offset(skip).limit(limit).all()

    return {
        "success": True,
        "count": len(doctors),
        "data": doctors
    }