import csv

# Fictional student dataset for CUL-CYB 371
students = [
    ["CUL001", "Computer Science", "200 Level", 92, 84],
    ["CUL002", "Cyber Security", "200 Level", 88, 79],
    ["CUL003", "Information Technology", "300 Level", 76, 71],
    ["CUL004", "Computer Science", "100 Level", 95, 90],
    ["CUL005", "Software Engineering", "200 Level", 81, 86],
    ["CUL006", "Cyber Security", "300 Level", 69, 74],
    ["CUL007", "Information Technology", "100 Level", 90, 82],
    ["CUL008", "Computer Science", "300 Level", 73, 68],
    ["CUL009", "Software Engineering", "100 Level", 85, 88],
    ["CUL010", "Cyber Security", "200 Level", 94, 91],
    ["CUL011", "Computer Science", "400 Level", 78, 76],
    ["CUL012", "Information Technology", "200 Level", 87, 80],
    ["CUL013", "Software Engineering", "300 Level", 66, 72],
    ["CUL014", "Cyber Security", "100 Level", 91, 85],
    ["CUL015", "Computer Science", "200 Level", 83, 89],
]

columns = [
    "Student ID",
    "Department",
    "Level",
    "Attendance Percentage",
    "Average Examination Score",
]

# Create a CSV file that can be opened in Excel or other spreadsheet programs.
with open("student_dataset.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(columns)
    writer.writerows(students)

print("Student dataset created successfully: student_dataset.csv")
