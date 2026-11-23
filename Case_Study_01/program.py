# ==============================================================================
# Case Study 1: Employee Payroll and Deduction Analysis
# Student Name: NUKALA SASI KIRAN | Roll Number: 26000656 | Branch: CSE
# College: Dr. RVR NRI Institute of Technology
# ==============================================================================

# Input Section
employee_name = input("Enter employee name: ")
basic_pay = float(input("Enter basic pay (Rs.): "))
overtime_hours = float(input("Enter overtime hours: "))
incentive = float(input("Enter incentive amount (Rs.): "))

# Allowances and Overtime Compensation
hra = basic_pay * 0.20          # House Rent Allowance (20% of basic pay)
da = basic_pay * 0.10           # Dearness Allowance (10% of basic pay)
overtime_comp = overtime_hours * 500.0  # Overtime rate = Rs. 500 per hour

# Gross Salary Calculation
gross_salary = basic_pay + hra + da + overtime_comp + incentive

# Progressive Income Tax Slab Calculation
if gross_salary <= 50000.0:
    income_tax = 0.0
elif gross_salary <= 100000.0:
    income_tax = gross_salary * 0.05
elif gross_salary <= 150000.0:
    income_tax = gross_salary * 0.10
else:
    income_tax = gross_salary * 0.15

# Statutory and Other Deductions
pf = basic_pay * 0.12           # Provident Fund (12% of basic pay)
other_deductions = 2000.0       # Fixed deductions (insurance, professional tax)
total_deductions = income_tax + pf + other_deductions

# Net Salary Calculation
net_salary = gross_salary - total_deductions

# Formatted Output Display
print("\n" + "=" * 55)
print("             EMPLOYEE SALARY STATEMENT             ")
print("=" * 55)
print(f"Employee Name          : {employee_name}")
print(f"Basic Pay              : Rs. {basic_pay:,.2f}")
print(f"HRA (20%)              : Rs. {hra:,.2f}")
print(f"DA (10%)               : Rs. {da:,.2f}")
print(f"Overtime Compensation  : Rs. {overtime_comp:,.2f}")
print(f"Incentive Amount       : Rs. {incentive:,.2f}")
print("-" * 55)
print(f"GROSS SALARY           : Rs. {gross_salary:,.2f}")
print("-" * 55)
print(f"Income Tax Deduction   : Rs. {income_tax:,.2f}")
print(f"Provident Fund (12%)   : Rs. {pf:,.2f}")
print(f"Other Deductions       : Rs. {other_deductions:,.2f}")
print("-" * 55)
print(f"TOTAL DEDUCTIONS       : Rs. {total_deductions:,.2f}")
print("=" * 55)
print(f"NET TAKE-HOME SALARY   : Rs. {net_salary:,.2f}")
print("=" * 55)
