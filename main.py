
students =[]
subject =["Python", "Maths", "Physics","Sn&AI"]
teacher =["Mr. Sharma", "Mrs. Patil", "Mr. Joshi"]

def register_student():

    for student in students:
        name = input("Enter your name: ")
        student_id = input("Enter your ID: ")
        password = input("Enter your password: ")

        if student_id in students:
            print("ID already exist")

    student = {
        "id" : student_id,
        "name" : name,
        "password" : password,
        "attendance" : 0,
        "marks": {}
        }

    students.append(student)

    print(student)

def login():

    st_id = input("Enter your ID: ")
    password = input("Enter your password: ")

    for student in students:

        if st_id == student["id"] and password == student["password"]:
            print("Login successful")
            
            print("================================")
            print("         STUDENT MENU           ")
            print("================================")
            print(student)
            print("\n1. View Marks\n2. View Attendance\n3. Subject Information\n4. Update Marks\n5. Exit")

            choice = int(input("Enter your choice: "))
            
            if choice == '1':
                view_marks()
            elif choice == '2':
                view_attendance()
            elif choice == '3':
                subject_information()
            elif choice == '4':
                update_marks()
            elif choice == '5':
                print("Program ended.")
                break
            else: print("Please enter choise in number")

            return

    print("Wrong ID or password")

def view_marks():
    st_id = input("Enter your ID: ")

    for student in students:

        if st_id == student["id"]:
            print(student["marks"])
            return

    print(f"Student{st_id} doesn't exist")

def view_attendance():
    st_id = input("Enter your ID: ")

    for student in students:

        if st_id == student["id"]:
            print(student["attendance"])
            return
        
    print("ID is wrong.")

def subject_information():
    print(subject)

def teacher_information():
    print(teacher)

def search_student():

    search_st = input("Enter your ID: ")

    for student in students:

        if search_st == student["id"]:
            print(student["name"])
            yn = input("Do you want detail regarding the student: (Y or N)")
            if yn == "Y":
                print(student)
            return
            
            
    print(f"Student {search_st} doesn't exist")

def update_marks():
    st_id = input("Enter your ID: ")
    
    for student in students:
    
        if st_id == student["id"]:

            print(student["marks"])

            nu_subject = input("What subject's mark do you want to change? : ")

            if nu_subject in subject:
                n_mark = int(input(f"New mark for {nu_subject} : "))

                student["marks"][nu_subject] = n_mark

                print(student)

                return
            else:
                print("Subject doesn't exist.")

                return
    print(f"Student {st_id} doesn't exist")

def delete_student():
    identify_id = input("Enter your ID: ")
    identify_password = input("Enter your password: ")
    for student in students:
        if identify_id == student["id"] and identify_password == student["password"]:
            yn = input(f"Are you sure you want to delete {identify_id} (Y or N): ")
            if yn == "Y":
                students.remove(student)
                print("Student login is deleted")
                return
            else:
                print("Deletion cancelled.")
                return
    print("ID or password is wrong.")

def main():

    while True:

        print("================================")
        print("  STUDENT MANAGEMENT SYSTEM")
        print("================================")
        print("\n1. Register Student\n2. Login\n3. View Marks\n4. View Attendance\n5. Subject Information\n6. Teacher Information\n7. Search Student\n8. Update Marks\n9. Delete Student\n10. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register_student()
        elif choice == '2':
            login()
        elif choice == '3':
            view_marks()
        elif choice == '4':
            view_attendance()
        elif choice == '5':
            subject_information()
        elif choice == '6':
            teacher_information()
        elif choice == '7':
            search_student()
        elif choice == '8':
            update_marks()
        elif choice == '9':
            delete_student()
        elif choice == '10':
            print("Program ended.")
            break
        else: print("Please enter choise in number")

main()