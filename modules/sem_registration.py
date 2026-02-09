from pydantic import BaseModel
from datetime import datetime

class registration_info(BaseModel):
    registration_number: str
    student_name: str
    semester: str
    Major_paper_1: str
    Major_paper_2: str
    Minor_paper: str
    Language_paper: str
    MDC_paper: str
    registered_at: datetime
