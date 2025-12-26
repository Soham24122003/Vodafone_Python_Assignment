
from typing import Dict, List, Tuple
from datetime import date

TUITION_FEE_PER_TERM = 50000.0

# student_id -> list of payments (amount, date, mode)
_fee_db: Dict[str, List[Tuple[float, date, str]]] = {}

def record_payment(student_id: str, amount: float, paid_on: date, mode: str = 'UPI') -> None:
    if amount <= 0:
        raise ValueError('Payment amount must be positive')
    _fee_db.setdefault(student_id, []).append((float(amount), paid_on, mode))

def outstanding_balance(student_id: str, terms: int = 2) -> float:
    total_fee = TUITION_FEE_PER_TERM * terms
    paid = sum(p[0] for p in _fee_db.get(student_id, []))
    return max(total_fee - paid, 0.0)

def get_statement(student_id: str) -> List[Tuple[float, date, str]]:
    return list(_fee_db.get(student_id, []))

