# ==============================================================================
# Case Study 3: Attendance Recovery Computation
# Student Name: NUKALA SASI KIRAN | Roll Number: 26000656 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

# Input current attendance records
total_classes = int(input("Enter total classes held so far: "))
attended_classes = int(input("Enter classes attended so far: "))

# Validation check
if total_classes <= 0:
    print("Error: Total classes must be greater than zero.")
elif attended_classes < 0 or attended_classes > total_classes:
    print("Error: Attended classes cannot be negative or exceed total classes.")
else:
    # Calculate current percentage
    current_pct = (attended_classes / total_classes) * 100.0

    print("\n" + "=" * 50)
    print("          ATTENDANCE RECOVERY REPORT          ")
    print("=" * 50)
    print(f"Total Classes Held      : {total_classes}")
    print(f"Classes Attended        : {attended_classes}")
    print(f"Current Attendance      : {current_pct:.2f}%")
    print("-" * 50)

    # Check 75% threshold
    if current_pct >= 75.0:
        print("Status                  : Attendance is sufficient (>= 75%).")
        print("No additional recovery classes required.")
    else:
        print("Status                  : Shortage of attendance (< 75%).")
        # Iteratively compute consecutive classes required to reach 75%
        extra = 0
        while ((attended_classes + extra) / (total_classes + extra)) * 100.0 < 75.0:
            extra += 1

        new_total = total_classes + extra
        new_attended = attended_classes + extra
        new_pct = (new_attended / new_total) * 100.0

        print(f"Recovery Classes Needed : {extra} consecutive classes")
        print(f"Projected Total Classes : {new_total}")
        print(f"Projected Attended      : {new_attended}")
        print(f"Projected Attendance    : {new_pct:.2f}%")

    print("=" * 50)
