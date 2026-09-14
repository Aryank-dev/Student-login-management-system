# 🎓 Student Management System

A simple **Student Management System built with Python**.
This project is a console-based application that allows users to register students, log in, view marks and attendance, manage student information, and update or delete student accounts.

## 📌 Features

* 👤 Register a new student
* 🔐 Student login with ID and password
* 📊 View student marks
* 📝 Update student marks
* 📅 View attendance
* 📚 View available subjects
* 👨‍🏫 View teacher information
* 🔎 Search for a student
* 🗑️ Delete a student account
* 🚪 Logout and exit the application
* ⚠️ Prevent duplicate student IDs

## 📚 Subjects

The system currently includes:

* Python
* Maths
* Physics
* Sn&AI

## 👨‍🏫 Teachers

The current teacher list includes:

* Mr. Sharma
* Mrs. Patil
* Mr. Joshi

## 🛠️ Technologies Used

* **Python 3**
* Python lists
* Python dictionaries
* Functions
* Loops
* Conditional statements
* User input

## 📂 Project Structure

```text
Student-Management-System/
│
├── main.py
└── README.md
```

> Replace `main.py` with your actual Python filename if it is different.

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-username/Student-Management-System.git
```

### 2. Open the project folder

```bash
cd Student-Management-System
```

### 3. Run the Python program

```bash
python main.py
```

On some systems, you may need:

```bash
python3 main.py
```

## 🖥️ Main Menu

When the program starts, you will see:

```text
================================
    STUDENT MANAGEMENT SYSTEM
================================

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
```

Choose an option by entering its corresponding number.

## 🔐 Student Registration

When registering, the program asks for:

```text
Enter your name:
Enter your ID:
Enter your password:
```

Each student is stored with:

* Student ID
* Name
* Password
* Attendance
* Marks

Example student data:

```python
{
    "id": "101",
    "name": "Rahul",
    "password": "1234",
    "attendance": 0,
    "marks": {}
}
```

## 🔑 Login

Students can log in using their registered ID and password.

After successful login, the student receives a menu containing:

```text
1. View Marks
2. View Attendance
3. Subject Information
4. Update Marks
5. Logout
```

## 📊 Marks Management

The program allows marks to be viewed and updated.

For example:

```text
Current marks:
{}

What subject's mark do you want to change? : Python
New mark for Python: 85

Marks updated successfully.
{'Python': 85}
```

## 🔎 Search Student

The search functionality allows you to enter a student ID and find the corresponding student.

The program displays the student's name and optionally provides additional information.

## 🗑️ Delete Student

A student can delete their account by entering their ID and password.

The program asks for confirmation before deleting the account.

```text
Are you sure you want to delete 101? (Y/N):
```

## ⚠️ Current Limitations

This project is currently designed as a **basic Python console application**, so there are some limitations:

* Student data is stored only in memory.
* Data is lost when the program exits.
* Passwords are stored as plain text.
* There is no database.
* There are no separate admin and student roles.
* Attendance cannot currently be updated through a dedicated function.
* Input validation is limited.

## 🚀 Future Improvements

Possible improvements include:

* 💾 Store data using **SQLite/MySQL**
* 🔒 Hash passwords instead of storing them directly
* 👨‍💼 Add an administrator/teacher login
* 📅 Add attendance management
* 📈 Add percentage and grade calculation
* 📊 Create a better marks-report system
* 🛡️ Add stronger input validation
* 🖥️ Build a graphical user interface using **Tkinter**
* 🌐 Convert the project into a web application using **Flask** or **Django**

## 🎯 Learning Objectives

This project was created to practice fundamental Python programming concepts, including:

* Variables
* Lists
* Dictionaries
* Functions
* `if/elif/else`
* `for` and `while` loops
* User input
* Data manipulation
* Basic program structure

## 📄 License

This project is available for educational and personal use.

---

⭐ If you found this project useful, consider giving the repository a star!
