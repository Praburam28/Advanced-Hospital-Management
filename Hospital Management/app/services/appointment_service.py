from sqlalchemy.orm import Session
from app.models.appointment import Appointment
from datetime import datetime

VALID_TIMES = [
    "10:00",
    "11:00",
    "12:00",
    "2:00",
    "3:00"
]

def create_appointment(
    db: Session,
    appointment
):

    if appointment.appointment_time not in VALID_TIMES:
        return {
            "error": "Invalid slot"
        }

    today = datetime.now().date()

    ap_date = datetime.strptime(
        appointment.appointment_date,
        "%Y-%m-%d"
    ).date()

    if ap_date < today:
        return {
            "error": "Past date not allowed"
        }

    existing = db.query(Appointment).filter(
        Appointment.doctor_id ==
        appointment.doctor_id,

        Appointment.appointment_date ==
        appointment.appointment_date,

        Appointment.appointment_time ==
        appointment.appointment_time
    ).first()

    if existing:
        return {
            "error": "Slot already booked"
        }

    db_appointment = Appointment(
        doctor_id=appointment.doctor_id,
        patient_id=appointment.patient_id,
        appointment_date=
        appointment.appointment_date,
        appointment_time=
        appointment.appointment_time,
        status="Pending"
    )

    db.add(db_appointment)
    db.commit()

    return db_appointment