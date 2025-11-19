from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services.sms_parser import parse_sms
from ..services.categorizer_services import categorize_transaction
from ..database.crud import save_transaction

router = APIRouter(prefix="/sms", tags=["sms"])

class SMSIn(BaseModel):
    text: str
    received_at: str | None = None

@router.post("/process")
def process_sms(payload: SMSIn):
    try:
        # Parse SMS
        parsed = parse_sms(payload.text)

        if parsed.get("amount") is None:
            parsed["amount"] = 0.0  

        # Categorize transaction safely
        parsed["category"] = categorize_transaction(parsed["text"])

        if payload.received_at:
            parsed["received_at"] = payload.received_at

        # Save to database
        txn_id = save_transaction(parsed)

        return {
            "status": "success",
            "transaction_id": txn_id,
            "parsed": parsed
        }

    except Exception as e:
        # Catch any unexpected error and return a JSON response
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")
