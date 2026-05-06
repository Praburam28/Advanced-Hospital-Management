from sqlalchemy import Column, Integer, String
from app.config.database import Base

class Appointment(Base):

    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True)

    doctor_id = Column(Integer)
    patient_id = Column(Integer)

    appointment_date = Column(String)
    appointment_time = Column(String)

    status = Column(
        String,
        default="Pending"
    )