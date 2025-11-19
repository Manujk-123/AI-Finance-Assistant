from pydantic import BaseModel
from typing import Optional

class SMSIn(BaseModel):
    text: str
    received_at: Optional[str]
