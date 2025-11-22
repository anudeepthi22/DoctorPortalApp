# Doctor Portal CRUD Application

## Overview

The **Doctor Portal** is a full-stack CRUD web application built using **Flask** and **MySQL**. It allows administrators to manage doctors, patients, appointments, prescriptions, and billing records in a healthcare environment. The system provides authentication, database connectivity, and user-friendly pages with consistent styling.

---

## Features

* **User Authentication**: Secure login using credentials stored in the database.
* **CRUD Operations**:

  * Add, edit, update, and delete records for Doctors, Patients, Appointments, Prescriptions, and Billings.
* **Relational Database Integration**: MySQL database (`doctor_portal`) used for data persistence.
* **Dashboard Summary**: Displays total number of doctors and patients.
* **Dynamic Frontend**: HTML templates styled with CSS for a clean and modern UI.

---

## Tech Stack

**Frontend:** HTML, CSS
**Backend:** Python (Flask)
**Database:** MySQL
**Version Control:** Git, GitHub

---

## Project Structure

```
DoctorPortalApp/
│
├── app.py                  # Main Flask application
├── db_config.py            # MySQL database configuration
├── static/
│   └── style.css           # Global stylesheet
├── templates/              # HTML pages
│   ├── login.html
│   ├── home.html
│   ├── doctors.html
│   ├── add_doctor.html
│   ├── patients.html
│   ├── appointments.html
│   ├── prescriptions.html
│   ├── billings.html
│   └── base.html
├── venv/                   # Virtual environment (not committed)
└── README.md               # Project documentation
```

---

## Database Setup

1. Open MySQL Workbench or Command Prompt.
2. Create the database:

   ```sql
   CREATE DATABASE doctor_portal;
   ```
3. Use the database:

   ```sql
   USE doctor_portal;
   ```
4. Create the required tables (Doctor, Patient, Appointment, Prescription, Billing, UserAccount).

---

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/DoctorPortalApp.git
   ```
2. Navigate into the folder:

   ```bash
   cd DoctorPortalApp
   ```
3. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   venv\Scripts\activate     # For Windows
   ```
4. Install dependencies:

   ```bash
   pip install flask mysql-connector-python flask-cors
   ```
5. Run the application:

   ```bash
   python app.py
   ```
6. Open in browser:

   ```
   http://127.0.0.1:5000
   ```

---

## Git Workflow

To track and push your changes:

```bash
git add .
git commit -m "Meaningful commit message here"
git push
```

---

## Author

**Anudeepthi Chirumamilla**
Master of Science in Data Science, Wichita State University
Project for CS 665: Database Systems

---

## License

This project is for **academic and learning purposes** only. All rights reserved.
