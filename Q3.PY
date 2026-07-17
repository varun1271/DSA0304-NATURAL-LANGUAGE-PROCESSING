import re

reg = input("Enter Register Number: ")
email = input("Enter College Email: ")
course = input("Enter Course Code: ")
semester = input("Enter Semester: ")
mobile = input("Enter Mobile Number: ")

status = True

# Register Number
if re.fullmatch(r"\d{2}[A-Z]{3}\d{4}", reg):
    print("Register Number Valid")
else:
    print("Invalid Register Number")
    status = False

# Institutional Email
if re.fullmatch(r"[a-zA-Z0-9._%+-]+@saveetha\.com", email):
    print("Email Valid")
else:
    print("Invalid Email")
    status = False

# Course Code
if re.fullmatch(r"[A-Z]{3}\d{2}", course):
    print("Course Code Valid")
else:
    print("Invalid Course Code")
    status = False

# Semester
if re.fullmatch(r"[1-8]", semester):
    print("Semester Valid")
else:
    print("Invalid Semester")
    status = False

# Mobile Number
if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Mobile Number Valid")
else:
    print("Invalid Mobile Number")
    status = False

# Final Report
print("\nRegistration Status")
if status:
    print("Registration Successful")
else:
    print("Registration Failed")