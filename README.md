# SchoolManagementSystem
School Management System using Django REST Framework, MySQL and JWT Authentication
Project Name:
School Management System

Technology:
- Python
- Django
- Django REST Framework
- MySQL
- JWT Authentication

Modules:
1. Authentication
2. Students
3. Teachers
4. Subjects
5. Attendance
6. Results
7. Dashboard

API Endpoints:
- /api/login/
- /api/profile/
- /api/students/
- /api/teachers/
- /api/subjects/
- /api/attendance/
- /api/results/
- /api/dashboard/

WORKFLOW DIAGRAM:
Admin
  │
  ▼
Authentication
  │
  ▼
Students ───► Attendance ◄─── Subjects
   │                         ▲
   │                         │
   └──────── Results ────────┘
             ▲
             │
         Teachers

Dashboard
   │
   ▼
Reports & Statistics

Project Report
1. Introduction
2. Objectives
3. Technologies Used
4. System Architecture
5. Database Design
6. API Endpoints
7. Modules Implemented
8. Testing
9. Conclusion
