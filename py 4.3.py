
import csv

# Payroll Management System

def add_employee():
    name = input("Enter employee name: ")
    emp_id = input("Enter employee ID: ")
    salary = float(input("Enter basic salary: "))

    hra = salary * 0.20
    da = salary * 0.10
    pf = salary * 0.12

    gross = salary + hra + da
    net = gross - pf

    with open("payroll.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, emp_id, salary, hra, da, pf, net])

    print("Employee payroll added successfully!")

def view_payroll():
    print("\n--- Payroll Report ---")

    try:
        with open("payroll.csv", "r") as file:
            reader = csv.reader(file)

            for row in reader:
                print("Name:", row[0])
                print("Employee ID:", row[1])
                print("Basic Salary:", row[2])
                print("HRA:", row[3])
                print("DA:", row[4])
                print("PF:", row[5])
                print("Net Salary:", row[6])
                print("----------------------")

    except FileNotFoundError:
        print("No payroll records found!")

while True:
    print("\n1. Add Employee")
    print("2. View Payroll")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_payroll()

    elif choice == "3":
        print("Exiting Payroll System...")
        break

    else:
        print("Invalid choice!")
