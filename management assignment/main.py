
import attendence as attendance              # alias import
from marks import add_mark, get_transcript, compute_grade  # from ... import
import report as rpt                         # alias import of module with classes
from student import create_student, list_students          # from ... import
import fees as fees                          # regular import (with alias)
import utils


from datetime import timedelta
import datetime as dt
import random


# def seed_demo_data():
#     for sid in (sid1, sid2):
#         add_mark(sid, 'Science', random.randint(55, 95))
#         add_mark(sid, 'English', random.randint(50, 100))
#
#     # Mark attendance for last 10 working days
#     start = utils.today() - timedelta(days=12)
#     for i in range(13):
#         day = start + timedelta(days=i)
#         if day.weekday() < 5:  # Mon-Fri
#             attendance.mark_attendance(sid1, day, utils.random_bool(0.9))
#             attendance.mark_attendance(sid2, day, utils.random_bool(0.8))
#
#     # Record some fee payments
#     fees.record_payment(sid1, 30000, utils.today(), mode='UPI')
#     fees.record_payment(sid1, 20000, utils.today(), mode='Card')
#     fees.record_payment(sid2, 25000, utils.today(), mode='UPI')
#
#     return sid1, sid2


def seed_demo_data():
    # Create students
    sid1 = create_student('Aarav Sharma', '10-A', utils.parse_date('2010-02-15'))
    sid2 = create_student('Ananya Gupta', '10-A', utils.parse_date('2010-08-21'))

    # Add marks for both students
    for sid in (sid1, sid2):
        add_mark(sid, 'Math',    random.randint(60, 100))
        add_mark(sid, 'Science', random.randint(55, 95))
        add_mark(sid, 'English', random.randint(50, 100))

    # Mark attendance for last 10 working days
    start = utils.today() - timedelta(days=12)
    for i in range(13):
        day = start + timedelta(days=i)
        if day.weekday() < 5:  # Mon-Fri
            attendance.mark_attendance(sid1, day, utils.random_bool(0.9))
            attendance.mark_attendance(sid2, day, utils.random_bool(0.8))

    # Record some fee payments
    fees.record_payment(sid1, 30000, utils.today(), mode='UPI')
    fees.record_payment(sid1, 20000, utils.today(), mode='Card')
    fees.record_payment(sid2, 25000, utils.today(), mode='UPI')

    return sid1, sid2


def print_module_properties():
    import student as student_mod
    print()
    print('Module Properties Demonstration:')
    print('student.__name__ =', student_mod.__name__)
    print('student.__file__ =', student_mod.__file__)
    print('student.__dict__ has', len(student_mod.__dict__), 'keys (showing few):', list(student_mod.__dict__.keys())[:10])

def main():
    sid1, sid2 = seed_demo_data()
    print('All students:', [s['name'] for s in list_students()])

    tr1 = get_transcript(sid1)
    pct1 = sum(tr1.values()) / (len(tr1) * 100) * 100 if tr1 else 0
    print()
    print(f"{sid1} Transcript:", tr1)
    print('Grade:', compute_grade(pct1))

    rg = rpt.ReportGenerator()
    start = utils.today() - dt.timedelta(days=10)
    end = utils.today()
    report1 = rg.generate_student_report(sid1, start, end, terms=2)
    report2 = rg.generate_student_report(sid2, start, end, terms=2)

    rg.save_report(report1, 'report_' + sid1 + '.txt')
    rg.save_report(report2, 'report_' + sid2 + '.txt')
    print()
    print('Generated report files:', 'report_' + sid1 + '.txt', 'report_' + sid2 + '.txt')

    print_module_properties()

    print()
    print('Standard library modules used: math (grading), datetime (dates), random (demo seeding).')

if __name__ == '__main__':
    main()
import random

def seed_demo_data():
    # Create students
    sid1 = create_student('Aarav Sharma', '10-A', utils.parse_date('2010-02-15'))
    sid2 = create_student('Ananya Gupta', '10-A', utils.parse_date('2010-08-21'))

    # Add marks
    for sid in (sid1, sid2):
        add_mark(sid, 'Math', random.randint(60, 100))
