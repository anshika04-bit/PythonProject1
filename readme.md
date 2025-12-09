## PythonProject1

This is a desktop-based Registration Management System developed using Python (Tkinter GUI) and MySQL database.
The application allows users to register, update, delete, search, and view records through an interactive graphical interface.

This project is suitable for college projects, practice, and learning CRUD operations with GUI and database connectivity.
Features

## User Registration Form
Insert New Records
Update Existing Records
Delete Records
Search Record by First Name
View All Records in Table (Treeview)
Date Picker for DOB
Gender Selection (Radio Buttons)
City Selection (Dropdown)
Password Hide/Show Feature
MySQL Database Integration

## Technologies Used

Python

Tkinter (GUI)

MySQL

PyMySQL

tkcalendar

Pillow (PIL)

## Database Structure

Database Name: project2
Table Name: registeration

CREATE TABLE registeration (
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    contact BIGINT,
    age INT,
    dob DATE,
    password VARCHAR(50),
    gender VARCHAR(20),
    city VARCHAR(50)
);

📂 Project Files
📁 Registration-System
│
├── main.py
├── README.md
└── images/
    └── background.jpg


🔹 Note: Update image paths according to your system.

How to Run the Project
1️⃣ Install Required Libraries
pip install pymysql tkcalendar pillow

2️⃣ Setup MySQL

Create database project2

Create table registeration

Update database credentials in code:

host='localhost'
user='root'
password='your_password'

3️⃣ Run the Application
python main.py

Functional Description
🔹 Submit

Adds new user data into the MySQL database.

🔹 Update

Updates an existing record based on First Name.

🔹 Delete

Deletes record from database using First Name.

🔹 Search

Searches user record and displays in Treeview table.

🔹 Show

Displays all saved registration records.

GUI Preview

Purple themed registration form with background image, entry fields, dropdowns, radio buttons, and data table.

Important Notes

Ensure MySQL server is running

First Name is used as primary identifier

Password is stored as plain text (for learning purpose only)


Add Login Authentication
Password Encryption
Input Validation
Email Verification
Separate Dashboard Page

🙌 Author

Anshika Gupta
Python & Data Analysis Learner

