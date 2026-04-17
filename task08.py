students = [
    {"name": "Aziz", "grade": 89},
    {"name": "Kamola", "grade": 95},
    {"name": "Javlon", "grade": 76},
    {"name": "Ali", "grade": 45},
    {"name": "Vali", "grade": 99},
    {"name": "Sami", "grade": 80},
]

ordered_students = list(sorted(students, key=lambda student: student["grade"]))


result = ordered_students[-3:]
print(result)
