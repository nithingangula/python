# -----------------------------
# Student Management System
# -----------------------------

students = []


def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter age: "))
    marks = float(input("Enter marks: "))

    student = {
        "name": name,
        "age": age,
        "marks": marks
    }

    students.append(student)

    print("Student added successfully!\n")


def display_students():

    if len(students) == 0:
        print("No students found.\n")
        return

    print("\n------ Student List ------")

    for student in students:
        print(f"Name  : {student['name']}")
        print(f"Age   : {student['age']}")
        print(f"Marks : {student['marks']}")
        print("--------------------------")


def search_student():

    search_name = input("Enter student name: ")

    for student in students:

        if student["name"].lower() == search_name.lower():
            print("\nStudent Found")
            print(student)
            return

    print("Student not found.\n")


def calculate_average():

    if len(students) == 0:
        print("No student data available.\n")
        return

    total = 0

    for student in students:
        total += student["marks"]

    average = total / len(students)

    print("Average Marks =", average)


def main():

    while True:

        print("\n===== Student Management =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Search Student")
        print("4. Average Marks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            calculate_average()

        elif choice == "5":
            print("Thank you!")
            break

        else:
            print("Invalid Choice")


main()