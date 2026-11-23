# ==============================================================================
# Case Study 8: Nested Loop Calendar Generator
# Student Name: NUKALA SASI KIRAN | Roll Number: 26000656 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

# Month and Year input
month = int(input("Enter month (1-12): "))
year = int(input("Enter year (e.g., 2026): "))

# List of month names (1-indexed using empty string at index 0)
month_names = [
    "", "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Standard days in each month
days_in_months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Check leap year condition
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Adjust February days for leap year
if month == 2 and is_leap:
    total_days = 29
else:
    total_days = days_in_months[month]

# Determine day of week for the 1st of the given month using Sakamoto's formula
# Weekday: 0 = Monday, 1 = Tuesday, ..., 6 = Sunday
t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
y = year
if month < 3:
    y = y - 1

# Formula gives: 0 = Sunday, 1 = Monday, ..., 6 = Saturday
day_code = (y + y // 4 - y // 100 + y // 400 + t[month - 1] + 1) % 7
# Convert to: 0 = Monday, 1 = Tuesday, ..., 6 = Sunday
start_day = (day_code + 6) % 7

# Print Calendar Header
print("\n" + "=" * 35)
print(f"         {month_names[month]} {year}         ")
print("=" * 35)
print(" Mon  Tue  Wed  Thu  Fri  Sat  Sun")
print("-" * 35)

# Render Calendar Grid using Nested Loops
# Outer loop runs for up to 6 possible weeks in a month
# Inner loop runs for 7 days (columns) of each week
day_counter = 1
for week in range(6):
    for col in range(7):
        cell_index = week * 7 + col
        
        # Check if cell is before the start day or beyond total days in month
        if cell_index < start_day or day_counter > total_days:
            print("     ", end="")
        else:
            print(f"{day_counter:>4} ", end="")
            day_counter += 1
            
    print()  # Newline at end of each week
    if day_counter > total_days:
        break

print("=" * 35)
