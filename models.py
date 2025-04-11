class User:
    def __init__(self, enrollment, name, password, email, department="", year="", semester=""):
        self.enrollment = enrollment
        self.name = name
        self.password = password
        self.email = email
        self.department = department
        self.year = year
        self.semester = semester

class Course:
    def __init__(self, code, name, instructor, credits):
        self.code = code
        self.name = name
        self.instructor = instructor
        self.credits = credits

class Attendance:
    def __init__(self, course_code, percentage):
        self.course_code = course_code
        self.percentage = percentage

class Grade:
    def __init__(self, course_code, grade, marks):
        self.course_code = course_code
        self.grade = grade
        self.marks = marks

class Fee:
    def __init__(self, name, amount, status, due_date):
        self.name = name
        self.amount = amount
        self.status = status
        self.due_date = due_date
