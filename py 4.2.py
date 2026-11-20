
# Student Data Manager Using Files

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")

    with open("students.txt", "a") as file:
        file.write(name + "," + roll + "," + marks + "\n")

    print("Student details added successfully!")

def view_students():
    print("\n--- Student Records ---")

    try:
        with open("students.txt", "r") as file:
            for line in file:
                name, roll, marks = line.strip().split(",")
                print("Name:", name)
                print("Roll Number:", roll)
                print("Marks:", marks)
                print("-------------------")

    except FileNotFoundError:
        print("No student records found!")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        print("Exiting Student Data Manager...")
        break

    else:
        print("Invalid choice!")
