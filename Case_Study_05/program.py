# ==============================================================================
# Case Study 5: Student Performance Trend Analysis
# Student Name: NUKALA SASI KIRAN | Roll Number: 26000656 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

# Data structures: list of student names, subject list, 2D list of marks
students = ["Ananya", "Bharath", "Chitra", "Deepak"]
subjects = ["Maths", "Physics", "Chemistry", "Python"]

marks = [
    [85, 72, 68, 91],  # Ananya
    [55, 48, 62, 70],  # Bharath
    [38, 45, 50, 42],  # Chitra
    [92, 88, 94, 96]   # Deepak
]

print("=" * 65)
print("             STUDENT ACADEMIC PERFORMANCE REPORT             ")
print("=" * 65)

# Header Row
print(f"{'Student':<12}", end="")
for sub in subjects:
    print(f"{sub:>10}", end="")
print(f"{'Total':>8}{'Avg %':>8}  {'Grade':<10}")
print("-" * 65)

# Process student-wise marks (Row-wise analysis)
student_totals = []
student_averages = []

for i in range(len(students)):
    row_sum = 0
    for j in range(len(subjects)):
        row_sum += marks[i][j]
    
    avg = row_sum / len(subjects)
    student_totals.append(row_sum)
    student_averages.append(avg)
    
    # Grade classification
    if avg >= 80.0:
        grade = "Excellent"
    elif avg >= 60.0:
        grade = "Good"
    elif avg >= 40.0:
        grade = "Average"
    else:
        grade = "Poor"
        
    # Print row
    print(f"{students[i]:<12}", end="")
    for j in range(len(subjects)):
        print(f"{marks[i][j]:>10}", end="")
    print(f"{row_sum:>8}{avg:>8.1f}  {grade:<10}")

print("-" * 65)

# Subject-wise average (Column-wise analysis)
print(f"{'Sub Average':<12}", end="")
for j in range(len(subjects)):
    col_sum = 0
    for i in range(len(students)):
        col_sum += marks[i][j]
    col_avg = col_sum / len(students)
    print(f"{col_avg:>10.1f}", end="")
print()
print("=" * 65)
