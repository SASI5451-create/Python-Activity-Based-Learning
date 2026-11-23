# ==============================================================================
# Case Study 9: Student Marks Matrix Analysis
# Student Name: NUKALA SASI KIRAN | Roll Number: 26000656 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

# Student names and Subject names
students = ["Arun", "Bala", "Divya", "Esha"]
subjects = ["Maths", "Science", "English", "Python"]

# 2D Nested List: rows represent students, columns represent subjects
marks = [
    [88, 76, 65, 92],  # Arun
    [55, 60, 72, 48],  # Bala
    [91, 85, 88, 95],  # Divya
    [70, 55, 60, 75]   # Esha
]

print("=" * 65)
print("                  MARKS MATRIX ANALYSIS REPORT                   ")
print("=" * 65)

# Print Matrix Table Header
print(f"{'Student':<12}", end="")
for sub in subjects:
    print(f"{sub:>10}", end="")
print(f"{'Total':>10}{'Avg':>9}")
print("-" * 65)

# Calculate Row Totals and Row Averages
row_totals = []
row_averages = []

for i in range(len(students)):
    r_total = 0
    for j in range(len(subjects)):
        r_total += marks[i][j]
        
    r_avg = r_total / len(subjects)
    row_totals.append(r_total)
    row_averages.append(r_avg)
    
    # Print student row
    print(f"{students[i]:<12}", end="")
    for j in range(len(subjects)):
        print(f"{marks[i][j]:>10}", end="")
    print(f"{r_total:>10}{r_avg:>9.1f}")

print("-" * 65)

# Calculate Column Averages (Subject-wise performance)
print(f"{'Col Avg':<12}", end="")
col_averages = []

for j in range(len(subjects)):
    c_total = 0
    for i in range(len(students)):
        c_total += marks[i][j]
        
    c_avg = c_total / len(students)
    col_averages.append(c_avg)
    print(f"{c_avg:>10.1f}", end="")

print()
print("=" * 65)

# Find Overall Highest and Lowest Marks using nested loops
highest_mark = marks[0][0]
lowest_mark = marks[0][0]

for i in range(len(students)):
    for j in range(len(subjects)):
        val = marks[i][j]
        if val > highest_mark:
            highest_mark = val
        if val < lowest_mark:
            lowest_mark = val

# Determine Top Student
top_student_index = 0
max_student_total = row_totals[0]
for i in range(1, len(students)):
    if row_totals[i] > max_student_total:
        max_student_total = row_totals[i]
        top_student_index = i

# Determine Best Subject
best_subject_index = 0
max_subject_avg = col_averages[0]
for j in range(1, len(subjects)):
    if col_averages[j] > max_subject_avg:
        max_subject_avg = col_averages[j]
        best_subject_index = j

# Display Summary Metrics
print("PERFORMANCE HIGHLIGHTS:")
print(f"  Highest Mark in Class   : {highest_mark}")
print(f"  Lowest Mark in Class    : {lowest_mark}")
print(f"  Top Performing Student  : {students[top_student_index]} (Total: {max_student_total}, Avg: {row_averages[top_student_index]:.1f})")
print(f"  Best Performing Subject : {subjects[best_subject_index]} (Class Avg: {max_subject_avg:.1f})")
print("=" * 65)
