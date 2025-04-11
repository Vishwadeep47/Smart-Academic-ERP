import os
import logging
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models import User, Course, Attendance, Grade, Fee

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")

# In-memory storage for users (would be replaced with database in production)
users = {}
courses = {}
attendance_records = {}
grades = {}
fees = {}

# Sample data for demonstration
def initialize_sample_data():
    # Add a test user
    users["123456"] = {
        "enrollment": "123456",
        "password": generate_password_hash("password"),
        "name": "Vishwadeep Choudhary",
        "email": "vishwadeep.choudhary@example.com",
        "department": "Computer Science",
        "year": "3rd Year",
        "semester": "6th Semester"
    }

    # Add sample courses
    courses["CS101"] = Course("CS101", "Introduction to Programming", "Professor", 3)
    courses["CS102"] = Course("CS102", "Data Structures", "Professor", 4)
    courses["CS103"] = Course("CS103", "Database Systems", "Professor", 3)
    courses["CS104"] = Course("CS104", "Computer Networks", "Professor", 4)
    courses["CS105"] = Course("CS105", "Software Engineering", "Professor", 3)

    # Add sample attendance
    attendance_records["123456"] = {
        "CS101": Attendance("CS101", 85),
        "CS102": Attendance("CS102", 92),
        "CS103": Attendance("CS103", 78),
        "CS104": Attendance("CS104", 88),
        "CS105": Attendance("CS105", 95)
    }

    # Add sample grades
    grades["123456"] = {
        "CS101": Grade("CS101", "A", 90),
        "CS102": Grade("CS102", "A+", 95),
        "CS103": Grade("CS103", "B+", 85),
        "CS104": Grade("CS104", "A-", 88),
        "CS105": Grade("CS105", "A", 91)
    }

    # Add sample fees
    fees["123456"] = [
        Fee("Tuition Fee", 50000, "Paid", "2023-07-15"),
        Fee("Library Fee", 2000, "Paid", "2023-07-15"),
        Fee("Examination Fee", 5000, "Paid", "2023-07-15"),
        Fee("Development Fee", 3000, "Due", "2023-12-31"),
        Fee("Hostel Fee", 25000, "Due", "2023-12-31")
    ]

initialize_sample_data()

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/auth/login', methods=['POST'])
def auth_login():
    enrollment = request.form.get('enrollment')
    password = request.form.get('password')
    
    if enrollment in users and check_password_hash(users[enrollment]["password"], password):
        session['user_id'] = enrollment
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    else:
        flash('Invalid enrollment number or password.', 'danger')
        return redirect(url_for('login'))

@app.route('/auth/register', methods=['POST'])
def auth_register():
    fullname = request.form.get('fullname')
    enrollment = request.form.get('enrollment')
    password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')
    
    if enrollment in users:
        flash('Enrollment number already exists.', 'danger')
        return redirect(url_for('login'))
    
    if password != confirm_password:
        flash('Passwords do not match.', 'danger')
        return redirect(url_for('login'))
    
    users[enrollment] = {
        "enrollment": enrollment,
        "password": generate_password_hash(password),
        "name": fullname,
        "email": f"{enrollment}@university.edu",
        "department": "Not Set",
        "year": "1st Year",
        "semester": "1st Semester"
    }
    
    flash('Registration successful! You can now log in.', 'success')
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = users.get(session['user_id'])
    if not user:
        session.pop('user_id', None)
        return redirect(url_for('login'))
    
    return render_template('dashboard.html', user=user)

@app.route('/profile')
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = users.get(session['user_id'])
    if not user:
        session.pop('user_id', None)
        return redirect(url_for('login'))
    
    return render_template('profile.html', user=user)

@app.route('/courses')
def course_list():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = users.get(session['user_id'])
    if not user:
        session.pop('user_id', None)
        return redirect(url_for('login'))
    
    return render_template('courses.html', user=user, courses=courses.values())

@app.route('/grades')
def grade_list():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = users.get(session['user_id'])
    if not user:
        session.pop('user_id', None)
        return redirect(url_for('login'))
    
    user_grades = grades.get(session['user_id'], {})
    
    return render_template('grades.html', user=user, grades=user_grades)

@app.route('/attendance')
def attendance_list():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = users.get(session['user_id'])
    if not user:
        session.pop('user_id', None)
        return redirect(url_for('login'))
    
    user_attendance = attendance_records.get(session['user_id'], {})
    
    return render_template('attendance.html', user=user, attendance=user_attendance)

@app.route('/timetable')
def timetable():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = users.get(session['user_id'])
    if not user:
        session.pop('user_id', None)
        return redirect(url_for('login'))
    
    return render_template('timetable.html', user=user)

@app.route('/fees')
def fee_details():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = users.get(session['user_id'])
    if not user:
        session.pop('user_id', None)
        return redirect(url_for('login'))
    
    user_fees = fees.get(session['user_id'], [])
    
    return render_template('fees.html', user=user, fees=user_fees)

@app.route('/library')
def library():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = users.get(session['user_id'])
    if not user:
        session.pop('user_id', None)
        return redirect(url_for('login'))
    
    return render_template('library.html', user=user)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
