from fastapi import APIRouter
from ..database.crud import list_transactions, get_transaction

router = APIRouter(prefix="/transactions", tags=["transactions"])

@router.get("/")
def get_all_transactions():
    return {"transactions": list_transactions()}

@router.get("/{txn_id}")
def get_txn(txn_id: int):
    txn = get_transaction(txn_id)
    if not txn:
        return {"error": "Transaction not found"}
    return txn
