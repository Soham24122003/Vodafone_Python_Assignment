
from typing import Dict, Tuple
import math

_marks_db: Dict[str, Dict[str, float]] = {}

def add_mark(student_id: str, subject: str, score: float) -> None:
    if not (0.0 <= score <= 100.0):
        raise ValueError("Score must be between 0 and 100")
    _marks_db.setdefault(student_id, {})[subject] = float(score)

def get_transcript(student_id: str) -> Dict[str, float]:
    return dict(_marks_db.get(student_id, {}))

def compute_total_and_percentage(student_id: str) -> Tuple[float, float]:
    subjects = _marks_db.get(student_id, {})
    total = sum(subjects.values())
    max_total = len(subjects) * 100.0 if subjects else 0.0
    percentage = (total / max_total * 100.0) if max_total else 0.0
    return total, percentage

def compute_grade(percentage: float) -> str:

    rounded = math.floor(percentage)
    if rounded >= 90:
        return 'A+'
    if rounded >= 80:
        return 'A'
    if rounded >= 70:
        return 'B+'
    if rounded >= 60:
        return 'B'
    if rounded >= 50:
        return 'C'
    return 'D'
