from pydantic import BaseModel

class AppointmentSchema(BaseModel):

    doctor_id: int

    patient_id: int

    appointment_date: str

    appointment_time: str