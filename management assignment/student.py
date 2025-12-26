
from datetime import date
from typing import Dict, List, Optional
import random
import string

_students: Dict[str, Dict] = {}

def _generate_student_id(prefix: str = 'STU') -> str:
    rand = ''.join(random.choices(string.digits, k=5))
    return f"{prefix}{rand}"

def create_student(name: str, class_name: str, dob: date) -> str:

    sid = _generate_student_id()
    _students[sid] = {
        'id': sid,
        'name': name,
        'class': class_name,
        'dob': dob,
        'created_on': date.today(),
    }
    return sid

def get_student(student_id: str) -> Optional[Dict]:
    return _students.get(student_id)

def list_students() -> List[Dict]:
    return list(_students.values())

def update_student(student_id: str, **updates) -> bool:
    if student_id not in _students:
        return False
    _students[student_id].update(updates)
    return True

def delete_student(student_id: str) -> bool:
    return _students.pop(student_id, None) is not None

if __name__ == '__main__':

    print("Module properties (student.py):")
    print("__name__:", __name__)
    print("__file__:", __file__)
    print("__dict__ keys (sample):", list(globals().keys())[:10])
