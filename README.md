🏥 Advanced Hospital Management System
🚀 FastAPI + MySQL Backend Project
📌 Project Overview

The Advanced Hospital Management System is a backend application developed using FastAPI and MySQL.

This project demonstrates:

✅ Authentication & Authorization
✅ Appointment Management
✅ RBAC (Role-Based Access Control)
✅ File Upload Handling
✅ Pagination & Filtering
✅ Service Layer Architecture
✅ Exception Handling
✅ JWT Security
✅ MySQL Database Integration

✨ Features Implemented
🔐 1. Advanced Authentication System
✅ JWT Authentication
✅ Password Hashing using bcrypt
✅ Login & Registration
✅ Forgot Password API
✅ Reset Password Token
👥 2. Role-Based Access Control (RBAC)
Supported Roles
Role	Access
👨‍💼 Admin	Full Access
👨‍⚕️ Doctor	Appointment Access
🧑 Patient	Appointment Booking
📅 3. Appointment Management
Features
✅ Create Appointment
✅ Prevent Double Booking
✅ Appointment Status
✅ Time Slot Validation
✅ Appointment Filtering
Appointment Statuses
🟡 Pending
🟢 Approved
🔴 Rejected
🔵 Completed
🔍 4. Search & Filtering
Doctor Search
Search by name
Search by specialization
Appointment Filters
Filter by date
Filter by status
Filter by patient
📄 5. Pagination & Sorting

Implemented for all listing APIs.

Example
/doctors/list?skip=0&limit=5
🧱 6. Service Layer Architecture

Project follows clean architecture.

routers → services → models → database

All business logic moved to service layer.

📁 7. Enhanced File Handling
Supported Formats
📄 PDF
🖼️ JPG
🖼️ PNG
Features
File validation
File size validation
Metadata storage
⚡ 8. Background Tasks

Implemented using FastAPI BackgroundTasks.

Used for:

Email simulation
Forgot password processing
Async tasks
📦 9. Standard API Response
{
  "success": true,
  "message": "Operation Successful",
  "data": {}
}
❌ 10. Global Exception Handling

Handled:

Validation Errors
Database Errors
Unauthorized Access
Internal Server Errors
🧪 11. Unit Testing

Implemented using:

pytest
🗂️ Project Structure
advanced-hospital-management/
│
├── app/
│   ├── main.py
│   │
│   ├── database/
│   │   └── db.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   ├── doctor.py
│   │   ├── patient.py
│   │   ├── appointment.py
│   │   └── file.py
│   │
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── doctor_schema.py
│   │   ├── patient_schema.py
│   │   └── appointment_schema.py
│   │
│   ├── routers/
│   │   ├── auth_router.py
│   │   ├── doctor_router.py
│   │   └── appointment_router.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── doctor_service.py
│   │   └── appointment_service.py
│   │
│   ├── utils/
│   │   ├── auth.py
│   │   ├── response.py
│   │   ├── exceptions.py
│   │   └── file_handler.py
│   │
│   ├── static/
│   └── templates/
│
├── tests/
├── requirements.txt
├── README.md
└── .env
⚙️ Installation & Setup
🔹 Step 1 — Create Virtual Environment
python -m venv venv
🔹 Step 2 — Activate Environment
Windows
venv\Scripts\activate
🔹 Step 3 — Install Requirements
pip install -r requirements.txt
🛢️ Database Setup
Create MySQL Database
CREATE DATABASE hospital_db;
🔑 Configure .env
SECRET_KEY=mysecretkey
ALGORITHM=HS256
DATABASE_URL=mysql+pymysql://root:password@localhost/hospital_db

Replace:

password

with your MySQL password.

▶️ Run Application
python -m uvicorn app.main:app --reload
🌐 Swagger API Documentation

Open:

http://127.0.0.1:8000/docs
🔗 API Endpoints
🔐 Authentication APIs
Method	Endpoint	Description
POST	/auth/register	Register User
POST	/auth/login	Login User
POST	/auth/forgot-password	Forgot Password
POST	/auth/reset-password	Reset Password
👨‍⚕️ Doctor APIs
Method	Endpoint	Description
POST	/doctors/add	Add Doctor
GET	/doctors/list	Get Doctors
📅 Appointment APIs
Method	Endpoint	Description
POST	/appointments/create	Create Appointment
GET	/appointments/list	Get Appointments
🔐 Authentication Flow
Step 1 — Register
{
  "name": "Admin",
  "email": "admin@gmail.com",
  "password": "admin123",
  "role": "Admin"
}
Step 2 — Login

Use:

username: admin@gmail.com
password: admin123
Step 3 — Copy JWT Token

Example:

Bearer eyJhbGciOiJIUzI1NiIs...
Step 4 — Authorize Swagger

Click:

Authorize

Paste token.

📅 Sample Appointment Request
{
  "doctor_name": "Guru",
  "patient_name": "Prabu",
  "appointment_date": "2026-05-06",
  "appointment_time": "11:00 AM"
}
🛡️ Security Features

✅ JWT Authentication
✅ Password Hashing
✅ Role-Based Access
✅ Protected APIs
✅ Secure Token Handling

🚀 Future Improvements
📧 Email Integration
⚡ Redis Caching
🐳 Docker Deployment
🌐 React Frontend
🔔 Notification System
💳 Payment Integration
📸 Output Screenshots

Add:

Swagger UI Screenshot
Login API Screenshot
Appointment API Screenshot
Database Screenshot
🎯 Assignment Deliverables Covered
Requirement	Status
JWT Authentication	✅
Password Hashing	✅
Forgot Password	✅
RBAC	✅
Appointment Management	✅
Double Booking Prevention	✅
Search & Filtering	✅
Pagination	✅
Service Layer Architecture	✅
File Upload Validation	✅
Background Tasks	✅
API Standardization	✅
Exception Handling	✅
Unit Testing	✅
👨‍💻 Developed By
Prabu Ram

Backend Developer — FastAPI Project

⭐ Conclusion

This project demonstrates real-world backend development using:

FastAPI
SQLAlchemy
JWT Security
RBAC
MySQL
Clean Architecture
Business Logic Implementation
API Validation
Production-style Backend Structure
🎉 Thank You

⭐ Advanced Hospital Management System ⭐
