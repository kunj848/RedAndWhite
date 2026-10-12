
from datetime import datetime

students = {}

def add_student():
    print("\n--- Add Student ---")

    student_id = input("Student ID: ").strip()

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Name: ").strip()

    try:
        age = int(input("Age: "))
        if age <= 0:
            print("Age must be greater than 0.")
            return
    except ValueError:
        print("Please enter a valid age.")
        return

    grade = input("Grade: ").strip()

    dob = input("Date of Birth (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        print("Invalid date! Use YYYY-MM-DD.")
        return

    subjects = [
        subject.strip()
        for subject in input("Subjects (comma-separated): ").split(",")
        if subject.strip()
    ]

    students[student_id] = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade,
        "dob": dob,
        "subjects": subjects
    }

    print("Student added successfully!")


def display_students():
    print("\n--- All Students ---")

    if not students:
        print("No students found.")
        return

    for student in students.values():
        print("-" * 40)
        print(f"Student ID : {student['id']}")
        print(f"Name       : {student['name']}")
        print(f"Age        : {student['age']}")
        print(f"Grade      : {student['grade']}")
        print(f"Date of Birth: {student['dob']}")
        print(f"Subjects   : {', '.join(student['subjects'])}")


def update_student():
    student_id = input("\nEnter Student ID to update: ").strip()

    if student_id not in students:
        print("Student not found!")
        return

    student = students[student_id]
    print("Press Enter to keep the existing value.")

    name = input(f"Name [{student['name']}]: ").strip()
    if name:
        student["name"] = name

    age = input(f"Age [{student['age']}]: ").strip()
    if age:
        try:
            new_age = int(age)
            if new_age <= 0:
                print("Age must be greater than 0.")
                return
            student["age"] = new_age
        except ValueError:
            print("Invalid age!")
            return

    grade = input(f"Grade [{student['grade']}]: ").strip()
    if grade:
        student["grade"] = grade

    dob = input(f"DOB [{student['dob']}]: ").strip()
    if dob:
        try:
            datetime.strptime(dob, "%Y-%m-%d")
            student["dob"] = dob
        except ValueError:
            print("Invalid date!")
            return

    subjects = input(
        f"Subjects [{', '.join(student['subjects'])}]: "
    ).strip()

    if subjects:
        student["subjects"] = [
            s.strip() for s in subjects.split(",") if s.strip()
        ]

    print("Student information updated successfully!")


def delete_student():
    student_id = input("\nEnter Student ID to delete: ").strip()

    if student_id in students:
        confirm = input(
            f"Delete {students[student_id]['name']}? (yes/no): "
        ).strip().lower()

        if confirm == "yes":
            del students[student_id]
            print("Student deleted successfully!")
        else:
            print("Deletion cancelled.")
    else:
        print("Student not found!")


def display_subjects():
    print("\n--- Subjects Offered ---")

    subjects = sorted({
        subject
        for student in students.values()
        for subject in student["subjects"]
    })

    if subjects:
        for number, subject in enumerate(subjects, start=1):
            print(f"{number}. {subject}")
    else:
        print("No subjects available.")


def main():
    while True:
        print("\n" + "=" * 40)
        print(" Welcome to Student Data Organizer ")
        print("=" * 40)
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student Information")
        print("4. Delete Student")
        print("5. Display Subjects Offered")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            display_subjects()
        elif choice == "6":
            print("Thank you for using Student Data Organizer!")
            break
        else:
            print("Invalid choice! Please select 1 to 6.")


if __name__ == "__main__":
    main()
