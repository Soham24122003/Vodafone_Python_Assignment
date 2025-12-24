from typing import Dict, List, Tuple

students: Dict[str, Dict[str, int]] = {
    "Sutirtha": {"Math": 95, "Science": 88, "English": 92},
    "Abir":   {"Math": 76, "Science": 81, "English": 79},
    "Ratnadip": {"Math": 64, "Science": 72, "English": 68},
    "Arka": {"Math": 58, "Science": 61, "English": 55},
    "Soham": {"Math": 89, "Science": 94, "English": 91},
}

def calculate_average(marks: Dict[str, int]) -> float:
    return sum(marks.values()) / len(marks)


def assign_grade(avg: float) -> str:
    if avg >= 90:
        return "A"
    elif 75 <= avg <= 89:
        return "B"
    elif 60 <= avg <= 74:
        return "C"
    else:
        return "Fail"


results: List[Tuple[str, float, str]] = []
for name, marks in students.items():
    avg = calculate_average(marks)
    grade = assign_grade(avg)
    results.append((name, avg, grade))


results.sort(key=lambda x: x[1], reverse=True)

print("Student Results:\n" + "-" * 40)
for name, avg, grade in results:
    print(f"Name: {name:6s} | Average: {avg:6.2f} | Grade: {grade}")

top_name, top_avg, _ = results[0]
print("\nTop Scorer:\n" + "-" * 40)
print(f"Name: {top_name} | Average: {top_avg:.2f}")
