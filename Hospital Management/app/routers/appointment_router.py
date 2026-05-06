from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    BackgroundTasks
)

from sqlalchemy.orm import Session

from app.models.appointment import Appointment

from app.schemas.appointment_schema import (
    AppointmentSchema
)

from app.services.appointment_service import (
    create_appointment
)

from app.core.dependencies import (
    get_db,
    role_required
)

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)

VALID_STATUS = [
    "Pending",
    "Approved",
    "Rejected",
    "Completed"
]

# BACKGROUND TASK

def send_notification(email):

    print(f"Notification sent to {email}")

# CREATE APPOINTMENT

@router.post("/")
def book_appointment(
    appointment: AppointmentSchema,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    user=Depends(
        role_required(["Patient"])
    )
):

    result = create_appointment(
        db,
        appointment
    )

    background_tasks.add_task(
        send_notification,
        "patient@gmail.com"
    )

    return result

# FILTER APPOINTMENTS

@router.get("/")
def get_appointments(
    appointment_date: str = None,
    status: str = None,
    patient_id: int = None,
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):

    query = db.query(Appointment)

    # FILTER BY DATE
    if appointment_date:

        query = query.filter(
            Appointment.appointment_date ==
            appointment_date
        )

    # FILTER BY STATUS
    if status:

        query = query.filter(
            Appointment.status == status
        )

    # FILTER BY USER/PATIENT
    if patient_id:

        query = query.filter(
            Appointment.patient_id ==
            patient_id
        )

    appointments = query.offset(skip).limit(limit).all()

    return {
        "success": True,
        "count": len(appointments),
        "data": appointments
    }

# UPDATE STATUS

@router.patch("/{appointment_id}/status")
def update_status(
    appointment_id: int,
    status: str,
    db: Session = Depends(get_db),
    user=Depends(
        role_required(["Admin", "Doctor"])
    )
):

    if status not in VALID_STATUS:

        raise HTTPException(
            status_code=400,
            detail="Invalid Status"
        )

    appointment = db.query(
        Appointment
    ).filter(
        Appointment.id == appointment_id
    ).first()

    if not appointment:

        raise HTTPException(
            status_code=404,
            detail="Appointment Not Found"
        )

    appointment.status = status

    db.commit()
    db.refresh(appointment)

    return {
        "success": True,
        "message": "Status Updated",
        "data": appointment
    }