🏥 Hospital Management System API


📌 Project Overview

This is a FastAPI-based Hospital Management System Backend that handles:

👨‍⚕️ Doctor Management
🧑 Patient Management
📅 Appointment Scheduling
🔐 JWT Authentication
🛡️ Role-Based Access Control (Admin / Doctor / Patient)
📂 File Upload System
🔍 Advanced Search & Filtering
📊 Pagination & Sorting
⏳ Background Tasks
🔁 Password Reset System
🚀 Features
🔐 Authentication
User Registration
Secure Login (JWT Token)
Password Hashing (bcrypt)
Forgot Password & Reset Password
👥 Role-Based Access Control (RBAC)
Admin → Full access
Doctor → Manage appointments
Patient → Book appointments
👨‍⚕️ Doctor Module
Add doctor (Admin only)
Search doctors by name/specialization
Pagination & sorting
📅 Appointment Module
Book appointments
Prevent double booking
Status tracking:
Pending
Approved
Rejected
Completed
Filter by date, status, patient
📂 File Upload
Upload medical reports
File type validation (PDF, PNG, JPG)
File size validation (2MB limit)
Store metadata in database
⚡ Advanced Features
Background tasks (notifications)
Global error handling
Clean architecture (Service Layer)
API response standardization
🏗️ Project Structure
advanced-hospital-management/
│
├── app/
│   ├── main.py
│   ├── config/
│   │   └── database.py
│   ├── core/
│   │   ├── security.py
│   │   └── dependencies.py
│   ├── models/
│   │   ├── user.py
│   │   ├── doctor.py
│   │   ├── appointment.py
│   │   └── file.py
│   ├── schemas/
│   │   ├── auth_schema.py
│   │   ├── doctor_schema.py
│   │   └── appointment_schema.py
│   ├── routers/
│   │   ├── auth_router.py
│   │   ├── doctor_router.py
│   │   ├── appointment_router.py
│   │   └── file_router.py
│   ├── services/
│   │   ├── auth_service.py
│   │   └── appointment_service.py
│
├── uploads/
├── requirements.txt
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the project
git clone https://github.com/your-username/hospital-management.git
cd hospital-management
2️⃣ Create virtual environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Run the project
uvicorn app.main:app --reload
5️⃣ Open API Docs
http://127.0.0.1:8000/docs
🔐 Authentication Flow
Register User
POST /auth/register
Login
POST /auth/login

Response:

{
  "access_token": "JWT_TOKEN",
  "token_type": "bearer"
}
🔒 Swagger Authorization

Click Authorize in Swagger UI:

Bearer YOUR_JWT_TOKEN
👨‍⚕️ Doctor API
Add Doctor
POST /doctors
Search Doctor
GET /doctors?search=cardiology
📅 Appointment API
Book Appointment
POST /appointments
Filter Appointments
GET /appointments?status=Pending
GET /appointments?appointment_date=2026-05-07
📂 File Upload API
POST /files/upload

Supported:

PNG
JPG
PDF

Max size:

2 MB
🧪 Testing Tools
Swagger UI → /docs
Postman
FastAPI auto-generated docs
⚠️ Error Handling
Error	Meaning
401	Unauthorized
403	Access Denied (RBAC)
422	Validation Error
500	Server Error
📊 Example Workflow
Register Admin
Login → get JWT
Authorize Swagger
Add Doctor
Register Patient
Book Appointment
Update Status
Upload File
🧠 Tech Stack
⚡ FastAPI
🐍 Python
🗄️ SQLAlchemy
🗃️ SQLite
🔐 JWT Authentication
🔒 Passlib (bcrypt)
📌 Future Improvements
Email notifications 📧
Frontend UI (React/Next.js) 🎨
Docker deployment 🐳
Cloud hosting ☁️
Redis caching ⚡


👨‍💻 Author

Prabu Ram
