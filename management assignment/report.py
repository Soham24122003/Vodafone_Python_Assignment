
from dataclasses import dataclass
from datetime import date
from typing import List

import student as student_mod
import marks as marks_mod
import attendence as attendance_mod
import fees as fees_mod
import utils as utils

@dataclass
class Section:
    title: str
    lines: List[str]

class ReportGenerator:
    def __init__(self):
        pass

    def _student_header(self, sid: str) -> Section:
        s = student_mod.get_student(sid)
        if not s:
            return Section('Student', ['UNKNOWN STUDENT'])
        header = [
            f"ID       : {s['id']}",
            f"Name     : {s['name']}",
            f"Class    : {s['class']}",
            f"DOB      : {utils.format_date(s['dob'])} (Age {utils.compute_age(s['dob'])})",
            f"Created  : {utils.format_date(s['created_on'])}",
        ]
        return Section('Student', header)

    def _academic_section(self, sid: str) -> Section:
        transcript = marks_mod.get_transcript(sid)
        total, pct = marks_mod.compute_total_and_percentage(sid)
        grade = marks_mod.compute_grade(pct)
        lines = [f"{sub}: {score}" for sub, score in transcript.items()]
        lines += [f"Total: {total:.1f}", f"Percentage: {pct:.2f}%", f"Grade: {grade}"]
        return Section('Academics', lines)

    def _attendance_section(self, sid: str, start: date, end: date) -> Section:
        pct = attendance_mod.attendance_percentage(sid, start, end)
        lines = [f"Attendance between {utils.format_date(start)} and {utils.format_date(end)}: {pct:.2f}%"]
        return Section('Attendance', lines)

    def _finance_section(self, sid: str, terms: int) -> Section:
        balance = fees_mod.outstanding_balance(sid, terms=terms)
        payments = fees_mod.get_statement(sid)
        lines = [f"Outstanding Balance (for {terms} terms): ₹{balance:,.2f}"]
        for amt, dt, mode in payments:
            lines.append(f"Paid ₹{amt:,.2f} on {utils.format_date(dt)} via {mode}")
        return Section('Finance', lines)

    def generate_student_report(self, sid: str, start: date, end: date, terms: int = 2) -> str:
        sections = [
            self._student_header(sid),
            self._academic_section(sid),
            self._attendance_section(sid, start, end),
            self._finance_section(sid, terms),
        ]
        report_lines = []
        report_lines.append('=' * 60)
        report_lines.append('STUDENT REPORT')
        report_lines.append('=' * 60)
        for sec in sections:
            report_lines.append('')  # blank line
            report_lines.append(f"[{sec.title}]")
            report_lines.extend(sec.lines)
        report_lines.append('')
        report_lines.append('=' * 60)
        return '\\n'.join(report_lines)  # literal '\n' written so module code stays valid

    def save_report(self, content: str, filepath: str) -> None:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
