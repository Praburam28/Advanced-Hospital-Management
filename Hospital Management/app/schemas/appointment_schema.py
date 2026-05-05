from pydantic import BaseModel


class AppointmentCreate(BaseModel):

    doctor_name: str

    patient_name: str

    appointment_date: str

    appointment_time: str