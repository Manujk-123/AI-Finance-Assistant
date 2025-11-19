from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TransactionOut(BaseModel):
    id: int
    text: Optional[str]
    amount: float
    txn_type: Optional[str]
    method: Optional[str]
    category: Optional[str]
    received_at: datetime
