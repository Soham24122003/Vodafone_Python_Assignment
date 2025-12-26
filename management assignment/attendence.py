
from typing import Dict
from datetime import date, timedelta

_attendance_db: Dict[str, Dict[date, bool]] = {}

def mark_attendance(student_id: str, day: date, present: bool) -> None:
    _attendance_db.setdefault(student_id, {})[day] = bool(present)

def attendance_percentage(student_id: str, start: date, end: date) -> float:
    if start > end:
        start, end = end, start
    record = _attendance_db.get(student_id, {})
    total_days = 0
    present_days = 0
    d = start
    while d <= end:
        if d.weekday() < 5:  # Mon-Fri considered working days
            total_days += 1
            if record.get(d, False):
                present_days += 1
        d += timedelta(days=1)
    return (present_days / total_days * 100.0) if total_days else 0.0
