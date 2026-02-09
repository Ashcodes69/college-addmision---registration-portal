from datetime import datetime
from db.connection import db
from modules.sem_registration import registration_info


students_col = db["students"]
credentials_col = db["credentials"]
registrations_col = db["semester_registrations"]


def register_student(data: dict):
    reg_no = data.get("registration_number")

    student = students_col.find_one({"registration_number": reg_no})
    if not student:
        raise ValueError("Student not found")

    creds = credentials_col.find_one({"registration_number": reg_no})
    if not creds or not creds.get("password_set"):
        raise ValueError("Password not set yet")

    current_semester = data.get("semester") 

    already_registered = registrations_col.find_one(
        {"registration_number": reg_no, "semester": current_semester}
    )
    if already_registered:
        raise ValueError(f"Already registered for semester {current_semester}")

    data.update(
        {
            "student_name": student["name"],
            "semester": current_semester,
            "registered_at": datetime.now(),
        }
    )

    registration = registration_info(**data)
    registrations_col.insert_one(registration.dict())


    students_col.update_one(
        {"registration_number": reg_no}, 
        {"$set":{"current_semester": current_semester}}
    )

    return f"Semester {current_semester} registration successful"