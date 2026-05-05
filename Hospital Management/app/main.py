from fastapi import FastAPI

from app.database.db import Base, engine

from app.models.user import User
from app.models.doctor import Doctor
from app.models.appointment import Appointment

from app.routers.auth_router import router as auth_router
from app.routers.doctor_router import router as doctor_router
from app.routers.appointment_router import router as appointment_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Advanced Hospital Management API"
)

app.include_router(auth_router)

app.include_router(doctor_router)

app.include_router(appointment_router)


@app.get("/")
def home():

    return {
        "message": "Hospital Management API Running"
    }