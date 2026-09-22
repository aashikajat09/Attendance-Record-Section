"""
STUDENT ATTENDANCE RECORD SYSTEM
A simple menu-driven console program using only basic Python.
No external libraries, databases, or frameworks are used.
"""

# ---------------------------------------------------------
# GLOBAL DATA
# ---------------------------------------------------------

# List used to store all student records (each student is a dictionary)
students = []

# Counters used only for "Today's Attendance Summary" (session-based)
present_today = 0
absent_today = 0


# ---------------------------------------------------------
# FEATURE 1: ADD STUDENT
# ---------------------------------------------------------
def add_student():
    print("\n" + "=" * 50)
    print("ADD STUDENT")
    print("=" * 50)

    roll_input = input("Enter Roll Number: ").strip()

    # Make sure roll number is a valid number
    if not roll_input.isdigit():
        print("Invalid roll number. Please enter numbers only.")
        return

    roll_no = int(roll_input)

    # Check whether the roll number already exists
    for student in students:
        if student["roll_no"] == roll_no:
            print("Student with this roll number already exists.")
            return

    name = input("Enter Student Name: ").strip()

    if name == "":
        print("Name cannot be empty. Student not added.")
        return

    # Create a new student dictionary and add it to the list
    new_student = {
        "roll_no": roll_no,
        "name": name,
        "present": 0,
        "absent": 0
    }
    students.append(new_student)

    print(f"Student {name} added successfully!")


# ---------------------------------------------------------
# FEATURE 2: VIEW ALL STUDENTS
# ---------------------------------------------------------
def view_students():
    print("\n" + "=" * 50)
    print("ALL STUDENTS")
    print("=" * 50)

    if len(students) == 0:
        print("No students registered yet.")
        return

    print(f"{'Roll No':<10}{'Name':<20}{'Present':<10}{'Absent':<10}")
    print("-" * 50)

    for student in students:
        print(f"{student['roll_no']:<10}{student['name']:<20}"
              f"{student['present']:<10}{student['absent']:<10}")

    print("-" * 50)


# ---------------------------------------------------------
# HELPER FUNCTION: FIND STUDENT BY ROLL NUMBER
# ---------------------------------------------------------
def find_student(roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None


# ---------------------------------------------------------
# HELPER FUNCTION: CALCULATE ATTENDANCE PERCENTAGE
# ---------------------------------------------------------
def get_percentage(student):
    total = student["present"] + student["absent"]

    # Avoid division by zero
    if total == 0:
        return None

    percentage = (student["present"] / total) * 100
    return percentage


# ---------------------------------------------------------
# FEATURE 3: MARK ATTENDANCE
# ---------------------------------------------------------
def mark_attendance():
    global present_today, absent_today

    print("\n" + "=" * 50)
    print("MARK ATTENDANCE")
    print("=" * 50)

    if len(students) == 0:
        print("No students registered yet.")
        return

    roll_input = input("Enter Roll Number: ").strip()

    if not roll_input.isdigit():
        print("Invalid roll number.")
        return

    roll_no = int(roll_input)
    student = find_student(roll_no)

    if student is None:
        print("Student not found.")
        return

    print("Student Found:")
    print(f"Name: {student['name']}")

    choice = input("Enter P for Present, A for Absent: ").strip().lower()

    if choice == "p":
        student["present"] += 1
        present_today += 1
        print(f"{student['name']} marked Present.")
    elif choice == "a":
        student["absent"] += 1
        absent_today += 1
        print(f"{student['name']} marked Absent.")
    else:
        print("Invalid input. Please enter P or A.")


# ---------------------------------------------------------
# FEATURE 4: VIEW ATTENDANCE RECORDS
# ---------------------------------------------------------
def view_attendance():
    print("\n" + "=" * 50)
    print("ATTENDANCE RECORD")
    print("=" * 50)

    if len(students) == 0:
        print("No students registered yet.")
        return

    print(f"{'Roll No':<10}{'Name':<20}{'P':<7}{'A':<7}{'%':<8}")
    print("-" * 50)

    for student in students:
        percentage = get_percentage(student)

        if percentage is None:
            percent_display = "N/A"
        else:
            percent_display = f"{percentage:.2f}%"

        print(f"{student['roll_no']:<10}{student['name']:<20}"
              f"{student['present']:<7}{student['absent']:<7}{percent_display:<8}")

    print("-" * 50)


# ---------------------------------------------------------
# FEATURE 5: SEARCH STUDENT
# ---------------------------------------------------------
def search_student():
    print("\n" + "=" * 50)
    print("SEARCH STUDENT")
    print("=" * 50)

    roll_input = input("Enter Roll Number: ").strip()

    if not roll_input.isdigit():
        print("Invalid roll number.")
        return

    roll_no = int(roll_input)
    student = find_student(roll_no)

    if student is None:
        print("Student not found.")
        return

    percentage = get_percentage(student)
    percent_display = "N/A" if percentage is None else f"{percentage:.2f}%"

    print("\n" + "=" * 50)
    print("STUDENT DETAILS")
    print("=" * 50)
    print(f"Roll Number: {student['roll_no']}")
    print(f"Name: {student['name']}")
    print(f"Present: {student['present']}")
    print(f"Absent: {student['absent']}")
    print(f"Attendance: {percent_display}")


# ---------------------------------------------------------
# FEATURE 6: CALCULATE ATTENDANCE PERCENTAGE
# ---------------------------------------------------------
def calculate_percentage():
    print("\n" + "=" * 50)
    print("CALCULATE ATTENDANCE PERCENTAGE")
    print("=" * 50)

    roll_input = input("Enter Roll Number: ").strip()

    if not roll_input.isdigit():
        print("Invalid roll number.")
        return

    roll_no = int(roll_input)
    student = find_student(roll_no)

    if student is None:
        print("Student not found.")
        return

    percentage = get_percentage(student)

    print(f"Student: {student['name']}")

    if percentage is None:
        print("Attendance Percentage: N/A (no attendance marked yet)")
    else:
        print(f"Attendance Percentage: {percentage:.2f}%")


# ---------------------------------------------------------
# FEATURE 7: LOW ATTENDANCE STUDENTS
# ---------------------------------------------------------
def low_attendance():
    print("\n" + "=" * 50)
    print("LOW ATTENDANCE STUDENTS")
    print("=" * 50)

    if len(students) == 0:
        print("No students registered yet.")
        return

    threshold_input = input("Enter attendance threshold: ").strip()

    try:
        threshold = float(threshold_input)
    except ValueError:
        print("Invalid threshold. Please enter a number.")
        return

    print(f"\nStudents below {threshold}%:")
    print(f"{'Roll No':<10}{'Name':<20}{'Attendance':<10}")
    print("-" * 50)

    found_any = False

    for student in students:
        percentage = get_percentage(student)

        # Skip students with no attendance recorded
        if percentage is None:
            continue

        if percentage < threshold:
            found_any = True
            print(f"{student['roll_no']:<10}{student['name']:<20}{percentage:.2f}%")

    if not found_any:
        print("No students are below the given attendance threshold.")

    print("-" * 50)


# ---------------------------------------------------------
# FEATURE 8: TODAY'S ATTENDANCE SUMMARY
# ---------------------------------------------------------
def today_summary():
    print("\n" + "=" * 50)
    print("TODAY'S SUMMARY")
    print("=" * 50)

    total_students = len(students)

    if total_students == 0:
        print("No students registered yet.")
        return

    # Avoid division by zero
    today_percentage = (present_today / total_students) * 100

    print(f"Total Students     : {total_students}")
    print(f"Present Today      : {present_today}")
    print(f"Absent Today       : {absent_today}")
    print(f"Attendance         : {today_percentage:.2f}%")
    print("=" * 50)


# ---------------------------------------------------------
# FILE HANDLING: SAVE STUDENT RECORDS TO A TEXT FILE
# ---------------------------------------------------------
def save_to_file():
    try:
        file = open("students.txt", "w")

        for student in students:
            file.write(f"Roll No: {student['roll_no']}\n")
            file.write(f"Name: {student['name']}\n")
            file.write(f"Present: {student['present']}\n")
            file.write(f"Absent: {student['absent']}\n")
            file.write("\n")

        file.close()
        print("Student records saved to students.txt")

    except Exception as error:
        print("Could not save file:", error)


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------
def main():
    print("=" * 50)
    print("STUDENT ATTENDANCE RECORD SYSTEM")
    print("=" * 50)

    while True:
        print("\n" + "=" * 50)
        print("MAIN MENU")
        print("=" * 50)
        print("1. Add Student")
        print("2. View All Students")
        print("3. Mark Attendance")
        print("4. View Attendance Records")
        print("5. Search Student")
        print("6. Calculate Attendance Percentage")
        print("7. Show Low Attendance Students")
        print("8. Today's Attendance Summary")
        print("9. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            mark_attendance()
        elif choice == "4":
            view_attendance()
        elif choice == "5":
            search_student()
        elif choice == "6":
            calculate_percentage()
        elif choice == "7":
            low_attendance()
        elif choice == "8":
            today_summary()
        elif choice == "9":
            save_to_file()
            print("Thank you for using Student Attendance Record System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


# ---------------------------------------------------------
# PROGRAM ENTRY POINT
# ---------------------------------------------------------
if __name__ == "__main__":
    main()
