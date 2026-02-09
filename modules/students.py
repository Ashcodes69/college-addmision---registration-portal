from pydantic import BaseModel, EmailStr
from datetime import datetime

class Student(BaseModel):
    # students personal details
    name: str
    DOB: datetime
    mobile_no: str
    email: EmailStr
    religion: str
    category: str  # ST SC OBC

    # address
    address: str
    pinCode: str
    ps: str
    district: str
    state: str
    Nationality: str

    # father/ mother details
    father_name: str
    father_occupation: str
    mother_name: str
    mother_occupation: str

    # previous college and marks percentage
    previous_institution: str
    prev_marks_per: str

    # Department to take admission & time of admission
    department: str

    # info we provide
    admission_time :datetime
    current_semester: str
    registration_number: str
    roll_no: str
