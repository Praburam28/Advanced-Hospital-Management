from fastapi import FastAPI

from app.config.database import Base, engine

from app.routers.auth_router import router as auth_router
from app.routers.doctor_router import router as doctor_router
from app.routers.appointment_router import router as appointment_router
from app.routers.file_router import router as file_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Hospital Management System")

app.include_router(auth_router)
app.include_router(doctor_router)
app.include_router(appointment_router)
app.include_router(file_router)

@app.get("/")
def home():
    return {
        "message": "API Running Successfully"
    }