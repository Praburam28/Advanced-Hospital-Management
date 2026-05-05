from sqlalchemy import Column, Integer, String
from app.database.db import Base


class Appointment(Base):

    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    doctor_name = Column(String(100))

    patient_name = Column(String(100))

    appointment_date = Column(String(100))

    appointment_time = Column(String(100))

    status = Column(String(50), default="Pending")