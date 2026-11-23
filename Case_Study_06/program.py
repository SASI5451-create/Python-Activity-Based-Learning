# ==============================================================================
# Case Study 6: Student Timetable Conflict Detection
# Student Name: NUKALA SASI KIRAN | Roll Number: 26000656 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

# Timetable represented as a list of tuples: (course_name, start_hour, end_hour)
# 24-hour integer clock format
timetable = [
    ("Mathematics", 9, 10),
    ("Physics", 10, 11),
    ("Chemistry", 9, 11),
    ("Python Lab", 14, 16),
    ("English", 15, 16),
    ("Engineering Graphics", 11, 13)
]

print("=" * 65)
print("             STUDENT TIMETABLE CONFLICT REPORT            ")
print("=" * 65)
print("Enrolled Courses:")
for i in range(len(timetable)):
    name, start, end = timetable[i]
    print(f"  {i+1}. {name:<22} : {start:02d}:00 to {end:02d}:00")

print("-" * 65)
print("Conflict Analysis:")

conflicts_found = False
conflict_count = 0

# Triangular nested loop comparison
for i in range(len(timetable)):
    name_a, start_a, end_a = timetable[i]
    for j in range(i + 1, len(timetable)):
        name_b, start_b, end_b = timetable[j]
        
        # Standard interval overlap condition: start_a < end_b and start_b < end_a
        if start_a < end_b and start_b < end_a:
            conflicts_found = True
            conflict_count += 1
            # Determine overlapping interval
            if start_a > start_b:
                overlap_start = start_a
            else:
                overlap_start = start_b
                
            if end_a < end_b:
                overlap_end = end_a
            else:
                overlap_end = end_b
                
            print(f"  [CONFLICT {conflict_count}] '{name_a}' and '{name_b}' overlap!")
            print(f"             -> '{name_a}' ({start_a:02d}:00-{end_a:02d}:00) vs '{name_b}' ({start_b:02d}:00-{end_b:02d}:00)")
            print(f"             -> Overlapping Window: {overlap_start:02d}:00 to {overlap_end:02d}:00")

if not conflicts_found:
    print("  No schedule conflicts detected. All courses are compatible.")

print("=" * 65)
print(f"Total Conflicts Detected: {conflict_count}")
print("=" * 65)
