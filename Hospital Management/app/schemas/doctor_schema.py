from pydantic import BaseModel

class DoctorSchema(BaseModel):
    name: str
    specialization: str
    experience: int