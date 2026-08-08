import re
import statistics
from datetime import datetime

# ============================================================
# Student Record Validator & Analyzer
# ============================================================

# Data Storage
students = []

# Set to store unique subjects
unique_subjects = set()

# Immutable grade boundaries
GRADE_BOUNDARIES = (
    ("A", 90),
    ("B", 75),
    ("C", 60),
    ("D", 40)
)

# Global counter
total_students = 0


# ============================================================
# Custom Exceptions
# ============================================================

class InvalidEmailError(Exception):
    """Raised when an email address is invalid."""
    pass


class InvalidPhoneError(Exception):
    """Raised when a phone number is invalid."""
    pass


# ============================================================
# Validation Functions
# ============================================================

def validate_email(email):
    """
    Validates email using regex.
    Required format: name@domain.com
    """
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com$'

    if not re.match(pattern, email):
        raise InvalidEmailError(
            "Invalid email! Email must follow the format name@domain.com."
        )


def validate_phone(phone):
    """
    Validates phone number using regex.
    Required format: exactly 10 digits.
    """
    pattern = r'^\d{10}$'

    if not re.match(pattern, phone):
        raise InvalidPhoneError(
            "Invalid phone number! Phone must contain exactly 10 digits."
        )


# ============================================================
# Calculate Average
# ============================================================

def calculate_average(marks):
    """Returns the average of the given marks."""
    if not marks:
        return 0

    return sum(marks) / len(marks)


# ============================================================
# Assign Grade
# ============================================================

def assign_grade(average):
    """Assigns a grade based on the average marks."""

    if average >= GRADE_BOUNDARIES[0][1]:
        return GRADE_BOUNDARIES[0][0]

    elif average >= GRADE_BOUNDARIES[1][1]:
        return GRADE_BOUNDARIES[1][0]

    elif average >= GRADE_BOUNDARIES[2][1]:
        return GRADE_BOUNDARIES[2][0]

    elif average >= GRADE_BOUNDARIES[3][1]:
        return GRADE_BOUNDARIES[3][0]

    else:
        return "F"


# ============================================================
# Add Student
# ============================================================

def add_student():
    """
    Adds a new student after validating email and phone.
    Uses local variables and updates the global counter.
    """

    global total_students

    print("\n--- Add Student ---")

    name = input("Enter student name: ").strip().title()

    # -------------------------
    # Email Validation
    # -------------------------
    while True:
        email = input("Enter email: ").strip()

        try:
            validate_email(email)
            break

        except InvalidEmailError as e:
            print("Error:", e)
            print("Please enter a valid email.")

    # -------------------------
    # Phone Validation
    # -------------------------
    while True:
        phone = input("Enter phone number: ").strip()

        try:
            validate_phone(phone)
            break

        except InvalidPhoneError as e:
            print("Error:", e)
            print("Please enter a valid phone number.")

    # -------------------------
    # Marks Input
    # -------------------------
    marks = []
    subjects = []

    print("\nEnter marks for subjects.")
    print("Enter 'done' when finished.")

    while True:
        subject = input("Enter subject name: ").strip()

        if subject.lower() == "done":
            break

        if subject == "":
            print("Subject name cannot be empty.")
            continue

        while True:
            try:
                mark = float(input(f"Enter marks for {subject}: "))

                if mark < 0 or mark > 100:
                    print("Marks must be between 0 and 100.")
                    continue

                break

            except ValueError:
                print("Please enter a valid number.")

        subjects.append(subject)
        marks.append(mark)

    # Store student as dictionary
    student = {
        "name": name,
        "email": email,
        "phone": phone,
        "marks": marks
    }

    # Add student to list
    students.append(student)

    # Add subjects to the set
    unique_subjects.update(subjects)

    total_students += 1

    print("\nStudent added successfully!")


# ============================================================
# Mask Email
# ============================================================

def mask_email(email):
    """
    Masks the username portion of an email.
    Example:
    student@gmail.com -> st***@gmail.com
    """

    username, domain = email.split("@")

    if len(username) <= 2:
        masked_username = username[0] + "***"
    else:
        masked_username = username[:2] + "***"

    return masked_username + "@" + domain


# ============================================================
# View Report
# ============================================================

def view_report():
    """Displays student analysis and report."""

    print("\n" + "=" * 60)
    print("              STUDENT PERFORMANCE REPORT")
    print("=" * 60)

    timestamp = datetime.now()

    print("Report generated on:", timestamp.strftime("%d-%m-%Y %H:%M:%S"))
    print("Total students:", total_students)
    print("Unique subjects:", unique_subjects)

    if not students:
        print("\nNo student records available.")
        return

    averages = []

    print("\nStudent Details")
    print("-" * 60)

    # For loop to iterate through students
    for student in students:

        # Skip student if they have no marks
        if not student["marks"]:
            print(f"{student['name']}: No marks available.")
            continue

        average = calculate_average(student["marks"])
        grade = assign_grade(average)

        averages.append(average)

        print("Name    :", student["name"])
        print("Email   :", mask_email(student["email"]))
        print("Phone   :", student["phone"])
        print("Marks   :", student["marks"])
        print("Average :", round(average, 2))
        print("Grade   :", grade)
        print("-" * 60)

    # Calculate median
    if averages:
        median_average = statistics.median(averages)

        print("\nOverall Analysis")
        print("-" * 60)
        print("Median of student averages:", round(median_average, 2))
        print("Total students with marks:", len(averages))
    else:
        print("\nNo marks available for calculating median.")

    print("=" * 60)


# ============================================================
# Main Menu
# ============================================================

def main():
    """Main menu-driven program."""

    while True:

        print("\n===================================")
        print(" Student Record Validator & Analyzer")
        print("===================================")
        print("1. Add Student")
        print("2. View Report")
        print("3. Exit")
        print("===================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_report()

        elif choice == "3":
            print("\nThank you for using Student Record Validator & Analyzer!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")
            continue


# ============================================================
# Program Execution
# ============================================================

if __name__ == "__main__":
    main()
