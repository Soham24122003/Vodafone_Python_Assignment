
from .student import create_student, get_student, list_students, update_student, delete_student
from .marks import add_mark, get_transcript, compute_total_and_percentage, compute_grade
from .attendance import mark_attendance, attendance_percentage
from .fees import record_payment, outstanding_balance, get_statement
from .report import ReportGenerator
