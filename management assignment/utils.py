
from datetime import datetime, date
import random

def today() -> date:
    return date.today()

def parse_date(s: str, fmt: str = '%Y-%m-%d') -> date:
    return datetime.strptime(s, fmt).date()

def format_date(d: date, fmt: str = '%d-%b-%Y') -> str:
    return d.strftime(fmt)

def random_bool(p_true: float = 0.7) -> bool:

    return random.random() < p_true

def compute_age(dob: date) -> int:
    today = date.today()
    years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return years

if __name__ == '__main__':
    print('Module properties (utils.py):')
    print('__name__:', __name__)
    print('__file__:', __file__)
    print('__dict__ keys (sample):', list(globals().keys())[:10])
