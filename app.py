from flask import Flask, render_template, request, redirect, session
import mysql.connector

app = Flask(__name__)
app.secret_key = 'secretkey123'

# Database Connection
def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Root@123',   # change this to your MySQL password
        database='doctor_portal'
    )

# ---------------- LOGIN ----------------
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM UserAccount WHERE Username=%s AND Password=%s", (username, password))
        user = cur.fetchone()
        cur.close()
        conn.close()
        if user:
            session['user'] = user['Username']
            return redirect('/home')
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

# ---------------- HOME PAGE ----------------
@app.route('/home')
def home():
    if 'user' not in session:
        return redirect('/')
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM Doctor")
    doctors = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM Patient")
    patients = cur.fetchone()[0]
    cur.close()
    conn.close()
    return render_template('home.html', doctors=doctors, patients=patients)

# ---------------- DOCTORS ----------------
@app.route('/doctors')
def doctors():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Doctor")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('doctors.html', doctors=rows)

@app.route('/add_doctor', methods=['GET', 'POST'])
def add_doctor():
    if request.method == 'POST':
        name = request.form['Name']
        specialty = request.form['Specialty']
        phone = request.form['Phone']
        email = request.form['Email']
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO Doctor (Name, Specialty, Phone, Email) VALUES (%s,%s,%s,%s)", 
                    (name, specialty, phone, email))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/doctors')
    return render_template('add_doctor.html')

@app.route('/edit_doctor/<int:id>', methods=['GET', 'POST'])
def edit_doctor(id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    if request.method == 'POST':
        name = request.form['Name']
        specialty = request.form['Specialty']
        phone = request.form['Phone']
        email = request.form['Email']
        cur.execute("UPDATE Doctor SET Name=%s, Specialty=%s, Phone=%s, Email=%s WHERE DoctorID=%s",
                    (name, specialty, phone, email, id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/doctors')
    cur.execute("SELECT * FROM Doctor WHERE DoctorID=%s", (id,))
    doctor = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('edit_doctor.html', doctor=doctor)

@app.route('/delete_doctor/<int:id>')
def delete_doctor(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Doctor WHERE DoctorID=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/doctors')

# ---------------- PATIENTS ----------------
@app.route('/patients')
def patients():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Patient")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('patients.html', patients=rows)

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['Name']
        dob = request.form['DOB']
        contact = request.form['Contact']
        address = request.form['Address']
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO Patient (Name, DOB, Contact, Address) VALUES (%s,%s,%s,%s)",
                    (name, dob, contact, address))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/patients')
    return render_template('add_patient.html')

@app.route('/edit_patient/<int:id>', methods=['GET', 'POST'])
def edit_patient(id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    if request.method == 'POST':
        name = request.form['Name']
        dob = request.form['DOB']
        contact = request.form['Contact']
        address = request.form['Address']
        cur.execute("UPDATE Patient SET Name=%s, DOB=%s, Contact=%s, Address=%s WHERE PatientID=%s",
                    (name, dob, contact, address, id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/patients')
    cur.execute("SELECT * FROM Patient WHERE PatientID=%s", (id,))
    patient = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('edit_patient.html', patient=patient)

@app.route('/delete_patient/<int:id>')
def delete_patient(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Patient WHERE PatientID=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/patients')

# ---------------- APPOINTMENTS ----------------
@app.route('/appointments')
def appointments():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Appointment")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('appointments.html', appointments=rows)

@app.route('/add_appointment', methods=['GET', 'POST'])
def add_appointment():
    if request.method == 'POST':
        patient_id = request.form['PatientID']
        doctor_id = request.form['DoctorID']
        date = request.form['Date']
        time = request.form['Time']
        status = request.form['Status']
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO Appointment (PatientID, DoctorID, Date, Time, Status) VALUES (%s,%s,%s,%s,%s)",
                    (patient_id, doctor_id, date, time, status))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/appointments')
    return render_template('add_appointment.html')

@app.route('/edit_appointment/<int:id>', methods=['GET', 'POST'])
def edit_appointment(id):
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    if request.method == 'POST':
        patient_id = request.form['PatientID']
        doctor_id = request.form['DoctorID']
        date = request.form['Date']
        time = request.form['Time']
        status = request.form['Status']
        cur.execute("UPDATE Appointment SET PatientID=%s, DoctorID=%s, Date=%s, Time=%s, Status=%s WHERE AppointmentID=%s",
                    (patient_id, doctor_id, date, time, status, id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/appointments')
    cur.execute("SELECT * FROM Appointment WHERE AppointmentID=%s", (id,))
    appointment = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('edit_appointment.html', appointment=appointment)

@app.route('/delete_appointment/<int:id>')
def delete_appointment(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Appointment WHERE AppointmentID=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/appointments')

# ---------------- PRESCRIPTIONS ----------------
@app.route('/prescriptions')
def prescriptions():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Prescription")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('prescriptions.html', prescriptions=rows)

@app.route('/add_prescription', methods=['GET', 'POST'])
def add_prescription():
    if request.method == 'POST':
        appointment_id = request.form['AppointmentID']
        medication = request.form['Medication']
        dosage = request.form['Dosage']
        notes = request.form['Notes']
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO Prescription (AppointmentID, Medication, Dosage, Notes) VALUES (%s,%s,%s,%s)",
                    (appointment_id, medication, dosage, notes))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/prescriptions')
    return render_template('add_prescription.html')

@app.route('/delete_prescription/<int:id>')
def delete_prescription(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Prescription WHERE PrescriptionID=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/prescriptions')

# ---------------- BILLINGS ----------------
@app.route('/billings')
def billings():
    conn = get_connection()
    cur = conn.cursor(dictionary=True)
    cur.execute("SELECT * FROM Billing")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('billings.html', billings=rows)

@app.route('/add_billing', methods=['GET', 'POST'])
def add_billing():
    if request.method == 'POST':
        appointment_id = request.form['AppointmentID']
        amount = request.form['Amount']
        payment_status = request.form['PaymentStatus']
        date = request.form['Date']
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO Billing (AppointmentID, Amount, PaymentStatus, Date) VALUES (%s,%s,%s,%s)",
                    (appointment_id, amount, payment_status, date))
        conn.commit()
        cur.close()
        conn.close()
        return redirect('/billings')
    return render_template('add_billing.html')

@app.route('/delete_billing/<int:id>')
def delete_billing(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Billing WHERE BillID=%s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect('/billings')

# ---------------- LOGOUT ----------------
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
