from pydantic import BaseModel
from datetime import datetime

class Credentials(BaseModel):
        registration_number: str
        password_hash: str
        password_set: bool
        last_updated: datetime