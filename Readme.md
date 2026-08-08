# Student Record Validator & Analyzer

## 📌 Project Overview

**Student Record Validator & Analyzer** is a Python-based console application that manages student records, validates user input, analyzes student performance, and generates a detailed report.

The project demonstrates important Python programming concepts such as **collections, regular expressions, exception handling, functions, scoping, loops, conditions, string operations, and standard modules**.

---

## 🎯 Objectives

The main objectives of this project are:

* Store and manage student records efficiently.
* Validate email addresses and phone numbers using Regular Expressions.
* Handle invalid inputs using custom exceptions.
* Calculate student averages and assign grades.
* Track unique subjects using a set.
* Generate performance reports.
* Calculate the median of student averages.
* Demonstrate Python functions, loops, conditions, and variable scoping.

---

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **Modules:**

  * `re` – Regular Expression validation
  * `statistics` – Median calculation
  * `datetime` – Report timestamping

No external libraries are required.

---

## 📂 Project Structure

```text
Student-Record-Validator-Analyzer/
│
├── student_record_validator.py
└── README.md
```

---

## ✨ Features

### 1. Student Data Storage

Each student is stored as a dictionary:

```python
{
    "name": "Rahul Sharma",
    "email": "rahul@gmail.com",
    "phone": "9876543210",
    "marks": [85, 92, 78]
}
```

All student dictionaries are stored in a list:

```python
students = []
```

A set is used to maintain unique subjects:

```python
unique_subjects = set()
```

---

### 2. Input Validation

The program validates:

#### Email

Email addresses must follow the format:

```text
name@domain.com
```

Regular expressions are used for validation.

Example:

```text
rahul@gmail.com       → Valid
rahul@gmail           → Invalid
rahul@gmail.org       → Invalid
```

#### Phone Number

The phone number must contain exactly **10 digits**.

Example:

```text
9876543210             → Valid
987654321              → Invalid
98765432101            → Invalid
```

The `{10}` regex quantifier is used to enforce the requirement.

---

### 3. Custom Exceptions

Two custom exceptions are implemented:

```python
class InvalidEmailError(Exception):
    pass

class InvalidPhoneError(Exception):
    pass
```

These exceptions are raised when invalid email addresses or phone numbers are entered.

---

### 4. Grade Calculation

The program uses immutable grade boundaries:

```python
GRADE_BOUNDARIES = (
    ("A", 90),
    ("B", 75),
    ("C", 60),
    ("D", 40)
)
```

Grades are assigned based on the student's average:

|  Average | Grade |
| -------: | :---: |
|   90–100 |   A   |
|    75–89 |   B   |
|    60–74 |   C   |
|    40–59 |   D   |
| Below 40 |   F   |

---

### 5. Performance Analysis

For every student with marks, the program calculates:

* Average marks
* Grade
* Student performance

The program also calculates the **median of all student averages** using Python's `statistics` module.

---

### 6. Email Privacy

Student emails are masked in the report for privacy.

Example:

```text
rahul@gmail.com
```

is displayed as:

```text
ra***@gmail.com
```

This is implemented using string slicing.

---

### 7. Report Timestamp

The `datetime` module is used to record when the report was generated.

Example:

```text
Report generated on: 08-08-2026 22:30:15
```

---

## 🖥️ Menu

When the program starts, the following menu is displayed:

```text
===================================
 Student Record Validator & Analyzer
===================================
1. Add Student
2. View Report
3. Exit
===================================
Enter your choice:
```

### Option 1 – Add Student

Allows the user to:

* Enter student name
* Enter and validate email
* Enter and validate phone number
* Enter subjects
* Enter marks
* Store the student record

### Option 2 – View Report

Displays:

* Total students
* Unique subjects
* Student details
* Masked email
* Marks
* Average
* Grade
* Median student average
* Report generation timestamp

### Option 3 – Exit

Terminates the application.

---

## ▶️ How to Run

### Step 1: Install Python

Make sure Python 3 is installed.

Check the installation using:

```bash
python --version
```

or:

```bash
python3 --version
```

### Step 2: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 3: Open the Project Folder

```bash
cd Student-Record-Validator-Analyzer
```

### Step 4: Run the Program

```bash
python student_record_validator.py
```

---

## 📊 Example Output

```text
===================================
 Student Record Validator & Analyzer
===================================
1. Add Student
2. View Report
3. Exit
===================================

Enter your choice: 1

--- Add Student ---

Enter student name: rahul sharma
Enter email: rahul@gmail.com
Enter phone number: 9876543210

Enter marks for subjects.
Enter 'done' when finished.

Enter subject name: Mathematics
Enter marks for Mathematics: 85

Enter subject name: Python
Enter marks for Python: 92

Enter subject name: DBMS
Enter marks for DBMS: 78

Enter subject name: done

Student added successfully!
```

### Report

```text
============================================================
              STUDENT PERFORMANCE REPORT
============================================================

Report generated on: 08-08-2026 22:30:15
Total students: 1
Unique subjects: {'Mathematics', 'Python', 'DBMS'}

Student Details
------------------------------------------------------------

Name    : Rahul Sharma
Email   : ra***@gmail.com
Phone   : 9876543210
Marks   : [85.0, 92.0, 78.0]
Average : 85.0
Grade   : B

------------------------------------------------------------

Overall Analysis
------------------------------------------------------------
Median of student averages: 85.0
Total students with marks: 1
============================================================
```

---

## 🧠 Python Concepts Demonstrated

This project covers the following concepts:

* Lists
* Dictionaries
* Sets
* Tuples
* Functions
* Local and global scope
* `global` keyword
* `if-elif-else`
* `while` loops
* `for` loops
* `break`
* `continue`
* Regular Expressions
* Custom Exceptions
* `try-except`
* String methods
* String slicing
* `statistics` module
* `datetime` module

---

## 🔐 Input Validation Rules

| Input   | Requirement                              |
| ------- | ---------------------------------------- |
| Name    | Automatically converted using `.title()` |
| Email   | Must follow `name@domain.com`            |
| Phone   | Exactly 10 digits                        |
| Marks   | Must be between 0 and 100                |
| Subject | Cannot be empty                          |

---

## 📈 Future Improvements

The project can be extended by adding:

* Student ID generation
* Search student functionality
* Update/delete student records
* Save records to a JSON or CSV file
* Database integration using SQLite
* Subject-wise performance analysis
* Highest and lowest scorer
* Graphical user interface
* Login/authentication system

---

## 👩‍💻 Author

**Harsh Srivastava**

B.Tech Computer Science & Engineering

---

## 📄 License

This project is created for **educational and academic purposes**.
