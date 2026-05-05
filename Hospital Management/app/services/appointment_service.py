from sqlalchemy.orm import Session
from app.models.appointment import Appointment
from datetime import datetime


def create_appointment_service(
    db: Session,
    data
):

    try:

        datetime.strptime(
            data.appointment_time,
            "%I:%M %p"
        )

    except:

        return "INVALID_TIME"

    existing = db.query(Appointment).filter(
        Appointment.doctor_name == data.doctor_name,
        Appointment.appointment_date == data.appointment_date,
        Appointment.appointment_time == data.appointment_time
    ).first()

    if existing:

        return "ALREADY_BOOKED"

    appointment = Appointment(
        doctor_name=data.doctor_name,
        patient_name=data.patient_name,
        appointment_date=data.appointment_date,
        appointment_time=data.appointment_time,
        status="Pending"
    )

    db.add(appointment)

    db.commit()

    db.refresh(appointment)

    return appointment


def get_appointments_service(
    db: Session,
    status=None
):

    query = db.query(Appointment)

    if status:

        query = query.filter(
            Appointment.status == status
        )

    appointments = query.all()

    return appointments