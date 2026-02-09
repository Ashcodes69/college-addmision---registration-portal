from datetime import datetime
from db.connection import db
from utils.password_utils import hash_password, verify_password

students_collection = db["students"]
credentials_collection = db["credentials"]


def student_exist(reg_no: str) -> bool:
    return students_collection.find_one({"registration_number": reg_no}) is not None


def set_password(reg_no: str, password: str):
    if not student_exist(reg_no):
        raise ValueError("Invalid registration no")

    if credentials_collection.find_one({"registration_number": reg_no}):
        raise ValueError("Password is already set")

    credentials_collection.insert_one(
        {
            "registration_number": reg_no,
            "password_hash": hash_password(password),
            "password_set": True,
            "last_updated": datetime.now(),
        }
    )


def login_student(reg_no: str, password: str) -> bool:
    if not student_exist(reg_no):
        raise ValueError("Registration number not found")

    creds = credentials_collection.find_one({"registration_number": reg_no})

    if not creds:
        raise ValueError("Password is not set, Please set a password first")

    if not verify_password(password, creds["password_hash"]):
        raise ValueError("Incorrect password")

    return True


def change_password(reg_no: str, old_password: str, new_password: str):
    creds = credentials_collection.find_one({"registration_number": reg_no})

    if not creds:
        raise ValueError("Credentials not found")

    if not verify_password(old_password, creds["password_hash"]):
        raise ValueError("Your old password is incorrect")

    credentials_collection.update_one(
        {"registration_number": reg_no},
        {
            "$set": {
                "password_hash": hash_password(new_password),
                "last_updated": datetime.now,
            }
        },
    )
