from sqlalchemy.orm import Session
from app.models.doctor import Doctor


def add_doctor_service(
    db: Session,
    data
):

    doctor = Doctor(
        name=data.name,
        specialization=data.specialization,
        experience=data.experience
    )

    db.add(doctor)

    db.commit()

    db.refresh(doctor)

    return doctor


def get_doctors_service(
    db: Session,
    skip: int,
    limit: int,
    sort_by: str
):

    doctors = db.query(Doctor) \
        .order_by(getattr(Doctor, sort_by)) \
        .offset(skip) \
        .limit(limit) \
        .all()

    return doctors