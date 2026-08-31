import sqlite3

# Connect to database
connection = sqlite3.connect("students.db")
cursor = connection.cursor()

# Create students table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    course TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

connection.commit()


# ---------------- ADD STUDENT ----------------
def add_student():
    print("\n===== ADD STUDENT =====")

    try:
        student_id = int(input("Enter Student ID: "))
        name = input("Enter Student Name: ")
        course = input("Enter Course: ")
        email = input("Enter Email: ")

        cursor.execute("""
            INSERT INTO students (id, name, course, email)
            VALUES (?, ?, ?, ?)
        """, (student_id, name, course, email))

        connection.commit()

        print("\nStudent added successfully!")

    except sqlite3.IntegrityError:
        print("\nStudent ID already exists. Please use another ID.")

    except ValueError:
        print("\nStudent ID must be a number.")


# ---------------- VIEW STUDENTS ----------------
def view_students():
    print("\n===== ALL STUDENTS =====")

    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
        return

    print("\nID\tName\t\tCourse\t\tEmail")
    print("-" * 70)

    for student in students:
        print(
            f"{student[0]}\t"
            f"{student[1]}\t\t"
            f"{student[2]}\t\t"
            f"{student[3]}"
        )


# ---------------- SEARCH STUDENT ----------------
def search_student():
    print("\n===== SEARCH STUDENT =====")

    try:
        student_id = int(input("Enter Student ID: "))

        cursor.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        if student:
            print("\nStudent Found!")
            print("ID:", student[0])
            print("Name:", student[1])
            print("Course:", student[2])
            print("Email:", student[3])
        else:
            print("\nStudent not found.")

    except ValueError:
        print("\nPlease enter a valid Student ID.")


# ---------------- UPDATE STUDENT ----------------
def update_student():
    print("\n===== UPDATE STUDENT =====")

    try:
        student_id = int(input("Enter Student ID to update: "))

        cursor.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        if not student:
            print("\nStudent not found.")
            return

        print("\nCurrent Details:")
        print("Name:", student[1])
        print("Course:", student[2])
        print("Email:", student[3])

        name = input("\nEnter New Name: ")
        course = input("Enter New Course: ")
        email = input("Enter New Email: ")

        cursor.execute("""
            UPDATE students
            SET name = ?, course = ?, email = ?
            WHERE id = ?
        """, (name, course, email, student_id))

        connection.commit()

        print("\nStudent updated successfully!")

    except ValueError:
        print("\nPlease enter a valid Student ID.")


# ---------------- DELETE STUDENT ----------------
def delete_student():
    print("\n===== DELETE STUDENT =====")

    try:
        student_id = int(input("Enter Student ID to delete: "))

        cursor.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        student = cursor.fetchone()

        if not student:
            print("\nStudent not found.")
            return

        print("\nStudent Details:")
        print("ID:", student[0])
        print("Name:", student[1])
        print("Course:", student[2])
        print("Email:", student[3])

        confirmation = input(
            "\nAre you sure you want to delete this student? (yes/no): "
        )

        if confirmation.lower() == "yes":

            cursor.execute(
                "DELETE FROM students WHERE id = ?",
                (student_id,)
            )

            connection.commit()

            print("\nStudent deleted successfully!")

        else:
            print("\nDeletion cancelled.")

    except ValueError:
        print("\nPlease enter a valid Student ID.")


# ================= MAIN MENU =================

while True:

    print("\n======================================")
    print("       STUDENT MANAGEMENT SYSTEM")
    print("======================================")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("======================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("\nThank you for using Student Management System!")
        break

    else:
        print("\nInvalid choice. Please enter a number from 1 to 6.")


# Close database
connection.close()