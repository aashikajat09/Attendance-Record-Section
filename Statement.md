# Project Requirement Statement
## Student Attendance Record System

---

## 1. Problem Statement

Educational institutions and individual instructors often rely on manual methods — paper registers or scattered spreadsheets — to record and track student attendance. These methods are time-consuming, error-prone, and make it difficult to quickly answer simple questions such as "Which students have low attendance?" or "What is a student's overall attendance percentage?"

There is a need for a lightweight, easy-to-use console application that allows a teacher or administrator to register students, mark their daily attendance, and instantly retrieve attendance statistics — without depending on external software, databases, or an internet connection.

The **Student Attendance Record System** addresses this by providing a simple, menu-driven Python program that manages student records and attendance data entirely in memory during a session, with the option to export the final records to a text file.

---

## 2. Scope of the Project

### In Scope
- Adding new students with a unique roll number and name.
- Viewing a list of all registered students along with their cumulative present/absent counts.
- Marking a student as Present (P) or Absent (A) for a given session.
- Viewing detailed attendance records, including attendance percentage per student.
- Searching for an individual student's attendance details by roll number.
- Calculating the attendance percentage for a specific student.
- Identifying students whose attendance falls below a user-defined threshold.
- Displaying a same-day ("today's") attendance summary based on the current session.
- Saving all student records to a local text file (`students.txt`) upon exit.
- Basic input validation (e.g., numeric roll numbers, duplicate roll number checks, non-empty names).

### Out of Scope (Current Version)
- Persistent storage across multiple sessions (data is not automatically reloaded from `students.txt` on startup).
- Date-wise or historical attendance tracking (the system tracks cumulative totals, not attendance by specific calendar date).
- Multi-user access, login/authentication, or role-based permissions.
- Graphical User Interface (GUI) or web-based interface.
- Integration with external databases or cloud services.
- Editing or deleting existing student records.
- Class/section-wise or subject-wise attendance segregation.

---

## 3. Target Users

- **Teachers / Instructors** — who need a quick way to take daily attendance for a class or group of students.
- **Small Institutes / Coaching Centers** — that do not require complex, large-scale attendance software and prefer a simple offline tool.
- **Students of Programming (Learning Context)** — as a reference/demo project for practicing Python fundamentals such as functions, dictionaries, lists, and file handling.
- **Administrative Staff** — who may use the exported text file for basic record-keeping or reporting.

---

## 4. High-Level Features

| # | Feature | Description |
|---|----------|-------------|
| 1 | **Add Student** | Register a new student with a unique roll number and name. |
| 2 | **View All Students** | Display a tabular list of all students with present/absent counts. |
| 3 | **Mark Attendance** | Mark a specific student as Present or Absent for the current session. |
| 4 | **View Attendance Records** | Display each student's present/absent counts along with computed attendance percentage. |
| 5 | **Search Student** | Look up a single student's full attendance details using their roll number. |
| 6 | **Calculate Attendance Percentage** | Compute and display the attendance percentage for a specific student. |
| 7 | **Low Attendance Report** | List students whose attendance percentage falls below a threshold entered by the user. |
| 8 | **Today's Attendance Summary** | Show a session-level summary of how many students were marked present/absent. |
| 9 | **Save & Exit** | Export all student records to `students.txt` and safely close the program. |

### Supporting Design Elements
- **Menu-driven console interface** for straightforward navigation.
- **In-memory data storage** using Python lists and dictionaries (no external database required).
- **Basic input validation** to prevent invalid roll numbers, duplicate entries, and empty names.
- **File export** (`students.txt`) as a simple, human-readable backup of attendance data.

---

## 5. Technology Stack

- **Language:** Python 3 (standard library only)
- **Interface:** Command-line / console
- **Data Storage:** In-memory (Python list of dictionaries) with text-file export
- **Dependencies:** None (no external libraries or frameworks)
