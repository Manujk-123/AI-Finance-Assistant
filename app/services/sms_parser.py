import re
from app.utils.text_cleaner import clean
from app.utils.regex_patterns import AMOUNT_RE, DATE_RE, UPI_RE, DEBIT_RE, CREDIT_RE

def parse_sms(text: str):
    """
    Parse a bank SMS and extract transaction info: amount, type, method, and date.
    """
    text_clean = clean(text)

    # Extract amount
    amount = None
    m = re.search(AMOUNT_RE, text_clean)
    if m:
        amount = float(re.sub(r"[^0-9.]", "", m.group(0)))

    # Determine transaction type
    txn_type = "unknown"
    if re.search(DEBIT_RE, text_clean):
        txn_type = "debit"
    elif re.search(CREDIT_RE, text_clean):
        txn_type = "credit"

    # Determine payment method
    method = "other"
    if re.search(UPI_RE, text_clean):
        method = "upi"

    # Extract date
    date_str = None
    d = re.search(DATE_RE, text)
    if d:
        date_str = d.group(0)

    return {
        "text": text_clean,
        "amount": amount,
        "txn_type": txn_type,
        "method": method,
        "raw_date": date_str
    }
