# Student & Teacher Management System

A desktop application built with Python for managing students, teachers, lessons, and schedules using role-based authentication and a MySQL database.

## Features
- Role-based login system (Admin / Teacher / Student)
- Admin can add, update, and delete students and teachers
- Teachers can upload lessons in PDF format
- Students can view lessons and schedules
- Schedule management
- PDF report generation

## Technologies
- Python
- Tkinter
- MySQL
- mysql-connector-python

## Authentication Design
This project focuses on role-based authentication (Admin / Teacher / Student).

User account creation (Sign-up) is intentionally excluded from the UI.
Users are pre-created in the database by the administrator.

This design choice was made to:
- Simplify the system for educational purposes
- Focus on authentication, roles, and permissions
- Simulate a controlled academic environment

## Test Credentials

To test the application:
1. Insert a user manually into the database (Student / Teacher / Admin)
2. Use the inserted credentials to log in

Example accounts:

**Student**
- Email: student@test.com
- Password: test123

**Teacher**
- Username: teacher
- Password: test123

**Admin**
- Username: admin
- Password: test123

### Prerequisites
- Python 3.10+
- MySQL or MariaDB

## Setup
1. Clone repository:
  - git clone https://github.com/amarabadou/students_teachers_management-.git
  - cd students_teachers_management-
3. update your local credentials in the connection file **src/connect.py** ( DB host , DB username , DB password , DB name )
4. create a database and import the schema
5. Install dependencies
6. Run the application (python src/main.py)

## Project Previews (Screenshots)

### Authentication & Main Entry
| Main Login Screen | Admin Login | Student Login |
| :---: | :---: | :---: |
| <img src="Screenshots/login.png" width="250"> | <img src="Screenshots/Admin Login.png" width="250"> | <img src="Screenshots/student_login.png" width="250"> |

### Dashboards
| Admin Dashboard | Teacher Dashboard | Student Dashboard |
| :---: | :---: | :---: |
| <img src="Screenshots/Admin_dashboard.png" width="250"> | <img src="Screenshots/teacher_dashboard.png" width="250"> | <img src="Screenshots/student_dashboard.png" width="250"> |

### Lesson Management
| Lesson Uploader | View Lessons | Weekly Schedule |
| :---: | :---: | :---: |
| <img src="Screenshots/lessons_uploader.png" width="250"> | <img src="Screenshots/view_lessons.png" width="250"> | <img src="Screenshots/shcedule.png" width="250"> |


## Author
Ammar Abadou  
Computer Science Student  

