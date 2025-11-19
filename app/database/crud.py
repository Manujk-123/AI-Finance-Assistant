# Dummy in-memory DB
DB = []

def save_transaction(txn: dict) -> int:
    txn_id = len(DB) + 1
    txn["id"] = txn_id
    DB.append(txn)
    return txn_id

def list_transactions():
    return DB

def get_transaction(txn_id: int):
    for txn in DB:
        if txn["id"] == txn_id:
            return txn
    return None
