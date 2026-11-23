# Python Activity-Based Learning (ABL)

[![Python 3.x](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Assignment-Completed-success.svg)]()
[![Institution](https://img.shields.io/badge/College-Dr.%20RVR%20NRI%20Institute%20of%20Technology-navy.svg)]()

---

## Student Information

- **Student Name:** NUKALA SASI KIRAN
- **Roll Number:** 26000656
- **Branch:** Computer Science and Engineering (CSE)
- **Section:** *[To be filled by student / Enter Section here]*
- **College:** Dr. RVR NRI Institute of Technology
- **Course:** Python Programming – Activity-Based Learning (ABL)
- **Submission Type:** Individual Academic Submission

---

## About the Project

This repository contains **10 comprehensive, challenging Python case studies** developed for the first-year **Python Programming Activity-Based Learning (ABL)** assignment at Dr. RVR NRI Institute of Technology.

Each case study applies fundamental computational thinking and programming concepts to solve authentic, real-world problems in business, operations management, academic administration, and banking. Every program has been developed from first principles, strictly adheres to the prescribed first-year engineering syllabus, has been rigorously executed and verified with multiple test cases, and is structured for independent academic defense and oral viva voce examination.

---

## Python Concepts Used

In strict adherence to the first-year engineering syllabus, all 10 case studies utilize only sanctioned foundational Python constructs. No external packages, object-oriented programming (OOP), lambda functions, complex exception handlers, or advanced comprehensions are used.

- **Variables & Data Foundations:** `int`, `float`, `str`, `bool`
- **User Input & Type Casting:** `input()`, `int()`, `float()`
- **Operators:** Arithmetic (`+`, `-`, `*`, `/`, `//`, `%`), Relational (`==`, `!=`, `<`, `>`, `<=`, `>=`), Logical (`and`, `or`, `not`)
- **Conditional Branching:** `if`, `if-else`, `if-elif-else` decision ladders
- **Iterative Control Flow:** `for` loops, `while` loops, `range()` function, `break` statements
- **String Handling & Formatting:** String indexing, string slicing, `.strip()`, `.lower()`, f-strings with precision formatting (`:,.2f`, `:>10`)
- **Sequences & Collections:**
  - **Lists:** Mutable sequences, list indexing, `append()`, `len()`
  - **Tuples:** Immutable sequences, tuple packing, tuple unpacking
  - **Nested 2D Lists:** Matrix representation, row-wise and column-wise nested loop traversal
- **Algorithmic Patterns:** Convergence loops, triangular pair scans ($O(n^2)$), 2D grid generation, extrema tracking

---

## Case Studies Overview

| # | Case Study Title | Primary Concepts | Real-World Application |
| :-: | :--- | :--- | :--- |
| **01** | **Employee Payroll and Deduction Analysis** | `if-elif-else`, `float`, f-strings | Computes employee net pay with allowances, overtime, progressive tax slabs, and statutory PF deductions. |
| **02** | **Retail Billing with Multiple Discount Rules** | Lists, `for` loops, discount cap | Itemized retail billing applying category-specific taxes, tiered volume discounts, and discount ceiling enforcement. |
| **03** | **Attendance Recovery Computation** | `while` loop, mathematical convergence | Iteratively simulates the exact consecutive classes needed to recover attendance to the mandatory 75% threshold. |
| **04** | **Warehouse Inventory Reconciliation** | Parallel lists, `abs()`, multi-flagging | Audits physical stock counts against ERP database records to flag stock discrepancies and safety reorder alerts. |
| **05** | **Student Performance Trend Analysis** | 2D lists, nested loops, grading ladders | Analyzes multi-subject exam marks matrix, computes individual averages, grades students, and tracks subject averages. |
| **06** | **Student Timetable Conflict Detection** | Tuples, tuple unpacking, interval overlap | Detects overlapping lecture and lab hours across student schedules using interval intersection logic. |
| **07** | **Repeated Transaction Detection** | Tuples, triangular nested loop scan | Scans banking payment records to detect and flag suspicious duplicate debits sharing identical amounts and merchants. |
| **08** | **Nested Loop Calendar Generator** | Nested loops, integer arithmetic, date logic | Formats and prints a 7-column monthly calendar grid (Mon–Sun) using integer date formulas without external modules. |
| **09** | **Student Marks Matrix Analysis** | 2D lists, nested loops, extrema tracking | Evaluates a 4x4 academic marks matrix, identifies class highest/lowest marks, top student, and top subject without comprehensions. |
| **10** | **Smart Canteen Order and Stock Management** | List of lists, inventory deduction, loops | Interactive cafeteria ordering system that validates live stock, applies bulk order discounts, and audits low inventory. |

---

## Repository Structure

```text
Python-Activity-Based-Learning/
│
├── README.md                          # Master project documentation, student info, and run guide
├── Assignment_Report.pdf              # Comprehensive consolidated college assignment report
│
├── Case_Study_01/
│   ├── program.py                     # Executable Python source code
│   ├── documentation.md               # Complete 12-section technical case study documentation
│   ├── flowchart.png                  # High-resolution flowchart diagram
│   └── output.txt                     # Verified console execution log
│
├── Case_Study_02/
│   ├── program.py
│   ├── documentation.md
│   ├── flowchart.png
│   └── output.txt
│
├── Case_Study_03/
│   ├── program.py
│   ├── documentation.md
│   ├── flowchart.png
│   └── output.txt
│
├── Case_Study_04/
│   ├── program.py
│   ├── documentation.md
│   ├── flowchart.png
│   └── output.txt
│
├── Case_Study_05/
│   ├── program.py
│   ├── documentation.md
│   ├── flowchart.png
│   └── output.txt
│
├── Case_Study_06/
│   ├── program.py
│   ├── documentation.md
│   ├── flowchart.png
│   └── output.txt
│
├── Case_Study_07/
│   ├── program.py
│   ├── documentation.md
│   ├── flowchart.png
│   └── output.txt
│
├── Case_Study_08/
│   ├── program.py
│   ├── documentation.md
│   ├── flowchart.png
│   └── output.txt
│
├── Case_Study_09/
│   ├── program.py
│   ├── documentation.md
│   ├── flowchart.png
│   └── output.txt
│
└── Case_Study_10/
    ├── program.py
    ├── documentation.md
    ├── flowchart.png
    └── output.txt
```

---

## How to Run the Programs

Follow these beginner-friendly steps to execute any case study program on your computer:

### Step 1: Verify Python Installation
Open your terminal (Command Prompt, PowerShell, or macOS/Linux Terminal) and verify that Python 3 is installed:
```bash
python --version
```
*(If Python is not recognized, download and install Python 3.10+ from [python.org](https://www.python.org/), ensuring you check the box **"Add Python to PATH"** during installation).*

### Step 2: Navigate to a Case Study Folder
Change directory into the desired case study folder:
```bash
cd Case_Study_01
```
*(Or `Case_Study_02`, `Case_Study_03`, etc.)*

### Step 3: Run the Program
Execute the Python script using standard Python:
```bash
python program.py
```

### Step 4: Follow Interactive Prompts
Enter the requested test inputs when prompted in the terminal. The program will execute and display the formatted output statement directly in your console.

---

## Assignment Requirements and Compliance

Every case study in this repository adheres strictly to all departmental evaluation criteria:
1. **Problem Statement:** Real-world background and problem description.
2. **Objectives:** Explicit, measurable computational goals.
3. **Assumptions:** Mathematical formulas, tax/discount slabs, thresholds, and boundary conditions.
4. **Input and Output:** Precise data types and expected visual displays.
5. **Algorithm:** Numbered step-by-step procedural logic in simple English.
6. **Flowchart:** Standard flowchart diagrams (Ovals, Parallelograms, Rectangles, Diamonds, Arrows).
7. **Pseudocode:** Clean, beginner-friendly pseudocode mirroring the program flow.
8. **Python Source Code:** Clean, properly indented, commented code using first-year syllabus constructs only.
9. **Test Cases:** Rigorous test tables including normal, boundary, and edge cases.
10. **Program Execution and Output:** Verifiable captured console output.
11. **Conclusion:** Learning outcomes and computational insights.
12. **Viva Preparation:** Tailored oral viva questions and concise answers for viva defense.
