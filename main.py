from student import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)


# Main Menu
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