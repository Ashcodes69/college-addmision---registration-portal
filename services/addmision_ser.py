# from datetime import datetime
# from db.connection import db
# from modules.students import Student

# students_collection = db["students"]


# def gen_reg_no(department: str, year: int) -> str:
#     count = students_collection.count_documents(
#         {"department": department, "admission_year": year}
#     )
#     return f"DSPMU{year}{department[:2].upper()}{count + 1:03d}"


# def gen_roll_no(department: str) -> str:
#     last_student = students_collection.find_one(
#         {"department": department}, sort=[("roll_no", -1)]
#     )
#     if last_student:
#         last_roll = int(last_student["roll_no"])
#         return str(last_roll + 1)
#     return "1"


# def create_student(student_data: dict):
#     if students_collection.find_one({"email": student_data["email"]}):
#         raise ValueError("Student already exists")

#     dob_str = student_data.get("DOB", "")
#     try:
#         dob_datetime = datetime.strptime(dob_str, "%d/%m/%Y")
#         student_data["DOB"] = dob_datetime
#     except ValueError:
#         raise ValueError("Invalid date format. Please use DD/MM/YYYY")

#     current_year = datetime.now().year
#     reg_no = gen_reg_no(department=student_data["department"], year=current_year)
#     roll_no = gen_roll_no(student_data["department"])

#     student_data.update(
#         {
#             "registration_number": reg_no,
#             "roll_no": roll_no,
#             "admission_year": current_year,
#             "admission_time": datetime.now(),
#             "current_semester": "1",
#         }
#     )

#     student = Student(**student_data)

#     if students_collection.find_one({"registration_number": reg_no}):
#         raise ValueError("Registration no already exists")

#     students_collection.insert_one(student_data)

#     return reg_no, roll_no
from datetime import datetime
from db.connection import db
from modules.students import Student

students_collection = db["students"]


def gen_reg_no(department: str, year: int) -> str:
    # Count ALL students in this department for this year (including ones just added)
    count = students_collection.count_documents(
        {"department": department, "admission_year": year}
    )
    # The next student gets count + 1
    return f"DSPMU{year}{department[:2].upper()}{count + 1:03d}"


def gen_roll_no(department: str) -> str:
    # Find the highest roll number in this department
    last_student = students_collection.find_one(
        {"department": department}, 
        sort=[("roll_no", -1)]
    )
    
    if last_student and last_student.get("roll_no"):
        try:
            last_roll = int(last_student["roll_no"])
            return str(last_roll + 1)
        except (ValueError, TypeError):
            # If conversion fails, count all students and add 1
            count = students_collection.count_documents({"department": department})
            return str(count + 1)
    else:
        # No students in this department yet, start with 1
        return "1"


def create_student(student_data: dict):
    # Check if email already exists
    if students_collection.find_one({"email": student_data["email"]}):
        raise ValueError("Student already exists with this email")

    # Convert DOB
    dob_str = student_data.get("DOB", "")
    try:
        dob_datetime = datetime.strptime(dob_str, "%d/%m/%Y")
        student_data["DOB"] = dob_datetime
    except ValueError:
        raise ValueError("Invalid date format. Please use DD/MM/YYYY")

    current_year = datetime.now().year
    department = student_data["department"]
    
    # Generate unique registration number and roll number
    reg_no = gen_reg_no(department=department, year=current_year)
    roll_no = gen_roll_no(department=department)

    # Update student data with generated values
    student_data.update(
        {
            "registration_number": reg_no,
            "roll_no": roll_no,
            "admission_year": current_year,
            "admission_time": datetime.now(),
            "current_semester": "1",
        }
    )

    # Validate with Pydantic
    student = Student(**student_data)

    # Double-check registration number uniqueness (safety check)
    if students_collection.find_one({"registration_number": reg_no}):
        raise ValueError("Registration number conflict. Please try again.")

    # Insert the student into database
    students_collection.insert_one(student_data)

    return reg_no, roll_no