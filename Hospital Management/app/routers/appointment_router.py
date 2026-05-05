from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.db import get_db

from app.schemas.appointment_schema import (
    AppointmentCreate
)

from app.services.appointment_service import (
    create_appointment_service,
    get_appointments_service
)

from app.utils.response import (
    success_response,
    error_response
)

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)


@router.post("/create")
def create_appointment(
    data: AppointmentCreate,
    db: Session = Depends(get_db)
):

    appointment = create_appointment_service(
        db,
        data
    )

    if appointment == "INVALID_TIME":

        return error_response(
            "Invalid Time Format. Use HH:MM AM/PM"
        )

    if appointment == "ALREADY_BOOKED":

        return error_response(
            "Appointment slot already booked"
        )

    return success_response(
        "Appointment Created Successfully",
        {
            "id": appointment.id,
            "doctor_name": appointment.doctor_name,
            "patient_name": appointment.patient_name,
            "appointment_date": appointment.appointment_date,
            "appointment_time": appointment.appointment_time,
            "status": appointment.status
        }
    )


@router.get("/list")
def appointment_list(
    status: str = None,
    db: Session = Depends(get_db)
):

    appointments = get_appointments_service(
        db,
        status
    )

    appointment_data = []

    for appointment in appointments:

        appointment_data.append({
            "id": appointment.id,
            "doctor_name": appointment.doctor_name,
            "patient_name": appointment.patient_name,
            "appointment_date": appointment.appointment_date,
            "appointment_time": appointment.appointment_time,
            "status": appointment.status
        })

    return success_response(
        "Appointments List",
        appointment_data
    )