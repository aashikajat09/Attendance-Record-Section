# Attendance-Record-Section
# Student Attendance Record System

## Project Overview

The **Student Attendance Record System** is a menu-driven Python console application that helps manage student attendance records. It allows users to add students, mark attendance, calculate attendance percentage, search student records, and identify students with low attendance.

This project is developed using **basic Python concepts** without using external libraries, databases, or frameworks.

---

## Objective

The objective of this project is to demonstrate the use of:

* Functions
* Lists
* Dictionaries
* Loops
* Conditional statements
* File handling
* User input validation
* Menu-driven programming

---

## Features

1. **Add Student**

   * Register a new student with Roll Number and Name.
   * Prevent duplicate roll numbers.

2. **View All Students**

   * Display all registered students with attendance details.

3. **Mark Attendance**

   * Mark a student as Present or Absent.

4. **View Attendance Records**

   * Display Present, Absent, and Attendance Percentage.

5. **Search Student**

   * Search a student using Roll Number.

6. **Calculate Attendance Percentage**

   * Calculate attendance percentage of an individual student.

7. **Low Attendance Report**

   * Display students whose attendance is below a chosen threshold.

8. **Today's Attendance Summary**

   * Show today's Present, Absent, and attendance percentage.

9. **Save Records**

   * Save student records into `students.txt` before exiting.

---

## Technologies Used

* Python 3
* Console/Terminal
* Text File (`students.txt`)

No external libraries are required.

---

## Data Structure Used

Each student is stored as a dictionary inside a list.

Example:

```python
{
    "roll_no": 101,
    "name": "Rahul",
    "present": 5,
    "absent": 2
}
```

---

## How to Run

1. Install Python 3.
2. Save the program as `attendance.py`.
3. Open Command Prompt or Terminal.
4. Navigate to the project folder.
5. Run:

```bash
python attendance.py
```

---

## Menu

```text
1. Add Student
2. View All Students
3. Mark Attendance
4. View Attendance Records
5. Search Student
6. Calculate Attendance Percentage
7. Show Low Attendance Students
8. Today's Attendance Summary
9. Exit
```

---

## Sample Output

```text
==================================================
STUDENT ATTENDANCE RECORD SYSTEM
==================================================

MAIN MENU

1. Add Student
2. View All Students
3. Mark Attendance
...
Enter your choice: 1

ADD STUDENT

Enter Roll Number: 101
Enter Student Name: Aashika

Student Aashika added successfully!
```

---

## Attendance Percentage Formula

Attendance percentage is calculated using:

<math value="\\frac{Present}{Present+Absent}\\times100" block/>

If no attendance has been recorded, the program displays **N/A**.

---

## File Handling

When the user exits the program:

* Student records are saved into `students.txt`.
* The file stores Roll Number, Name, Present count, and Absent count.

Example:

```text
Roll No: 101
Name: Aashika
Present: 5
Absent: 1
```

---

## Input Validation

The program checks:

* Roll number must contain only digits.
* Student name cannot be empty.
* Duplicate roll numbers are not allowed.
* Attendance accepts only **P** or **A**.
* Threshold accepts numeric values.

---

## Future Improvements

* Automatic loading of saved records at startup.
* Date-wise attendance history.
* Edit student details.
* Delete student records.
* Export attendance to CSV.
* Simple GUI using Tkinter.

---

## Learning Outcomes

This project demonstrates practical implementation of:

* Functions
* Lists and Dictionaries
* Loops
* Conditional Statements
* File Handling
* User Input Validation
* Modular Programming

---

## Author

**Student Name:** Aashika Jat

**Course:** Python Programming

**Project:** Student Attendance Record System
