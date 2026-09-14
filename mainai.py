students = []
subject = ["Python", "Maths", "Physics", "Sn&AI"]
teacher = ["Mr. Sharma", "Mrs. Patil", "Mr. Joshi"]


def register_student():

    name = input("Enter your name: ")
    student_id = input("Enter your ID: ")
    password = input("Enter your password: ")

    # Check if ID already exists
    for student in students:
        if student_id == student["id"]:
            print("ID already exists.")
            return

    student = {
        "id": student_id,
        "name": name,
        "password": password,
        "attendance": 0,
        "marks": {}
    }

    students.append(student)

    print("Student registered successfully.")
    print(student)

def login():

    st_id = input("Enter your ID: ")
    password = input("Enter your password: ")

    for student in students:

        if st_id == student["id"] and password == student["password"]:

            print("Login successful.")

            # Student menu
            while True:

                print("================================")
                print("         STUDENT MENU")
                print("================================")
                print("1. View Marks")
                print("2. View Attendance")
                print("3. Subject Information")
                print("4. Update Marks")
                print("5. Logout")

                choice = input("Enter your choice: ")

                if choice == "1":
                    view_marks(student)

                elif choice == "2":
                    view_attendance(student)

                elif choice == "3":
                    subject_information()

                elif choice == "4":
                    update_marks(student)

                elif choice == "5":
                    print("Logged out.")
                    break

                else:
                    print("Please enter a valid number.")

            return

    print("Wrong ID or password.")

def view_marks(student):

    print("Marks:")
    print(student["marks"])

def view_attendance(student):

    print("Attendance:")
    print(student["attendance"])

def subject_information():

    print("Subjects:")
    print(subject)

def teacher_information():

    print("Teachers:")
    print(teacher)

def search_student():

    search_st = input("Enter student ID: ")

    for student in students:

        if search_st == student["id"]:

            print("Student Name:", student["name"])

            yn = input("Do you want details regarding the student? (Y/N): ")

            if yn.upper() == "Y":
                print(student)

            return

    print(f"Student {search_st} doesn't exist.")

def update_marks(student):

    print("Current marks:")
    print(student["marks"])

    nu_subject = input("What subject's mark do you want to change? : ")

    if nu_subject in subject:

        n_mark = int(input(f"New mark for {nu_subject}: "))

        student["marks"][nu_subject] = n_mark

        print("Marks updated successfully.")
        print(student["marks"])

    else:

        print("Subject doesn't exist.")

def delete_student():

    identify_id = input("Enter your ID: ")
    identify_password = input("Enter your password: ")

    for student in students:

        if identify_id == student["id"] and identify_password == student["password"]:

            yn = input(
                f"Are you sure you want to delete {identify_id}? (Y/N): "
            )

            if yn.upper() == "Y":

                students.remove(student)

                print("Student account deleted.")

            else:

                print("Deletion cancelled.")

            return

    print("ID or password is wrong.")

def main():

    while True:

        print("================================")
        print("    STUDENT MANAGEMENT SYSTEM")
        print("================================")

        print("""
1. Register Student
2. Login
3. View Marks
4. View Attendance
5. Subject Information
6. Teacher Information
7. Search Student
8. Update Marks
9. Delete Student
10. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_student()

        elif choice == "2":
            login()

        elif choice == "3":
            # Temporary: asks for ID because this is outside login
            view_marks_by_id()

        elif choice == "4":
            view_attendance_by_id()

        elif choice == "5":
            subject_information()

        elif choice == "6":
            teacher_information()

        elif choice == "7":
            search_student()

        elif choice == "8":
            update_marks_by_id()

        elif choice == "9":
            delete_student()

        elif choice == "10":
            print("Program ended.")
            break

        else:
            print("Please enter a valid number.")

def view_marks_by_id():

    st_id = input("Enter student ID: ")

    for student in students:

        if st_id == student["id"]:
            print(student["marks"])
            return

    print(f"Student {st_id} doesn't exist.")

def view_attendance_by_id():

    st_id = input("Enter student ID: ")

    for student in students:

        if st_id == student["id"]:
            print(student["attendance"])
            return

    print(f"Student {st_id} doesn't exist.")

def update_marks_by_id():

    st_id = input("Enter student ID: ")

    for student in students:

        if st_id == student["id"]:
            update_marks(student)
            return

    print(f"Student {st_id} doesn't exist.")

main()