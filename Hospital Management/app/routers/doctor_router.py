from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.schemas.doctor_schema import DoctorCreate

from app.services.doctor_service import (
    add_doctor_service,
    get_doctors_service
)

from app.utils.response import success_response
from app.utils.role_checker import role_required

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)


@router.post("/add")
def add_doctor(
    data: DoctorCreate,
    db: Session = Depends(get_db),
    current_user=Depends(role_required("Admin"))
):

    doctor = add_doctor_service(db, data)

    return success_response(
        "Doctor Added Successfully",
        {
            "id": doctor.id,
            "name": doctor.name,
            "specialization": doctor.specialization,
            "experience": doctor.experience
        }
    )


@router.get("/list")
def doctor_list(
    skip: int = 0,
    limit: int = 10,
    sort_by: str = "id",
    db: Session = Depends(get_db)
):

    doctors = get_doctors_service(
        db,
        skip,
        limit,
        sort_by
    )

    doctor_data = []

    for doctor in doctors:

        doctor_data.append({
            "id": doctor.id,
            "name": doctor.name,
            "specialization": doctor.specialization,
            "experience": doctor.experience
        })

    return success_response(
        "Doctors List",
        doctor_data
    )