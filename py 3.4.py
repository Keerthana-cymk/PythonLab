# Attendance Tracker

attendance = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("\nEnter student name: ")
    status = input("Enter attendance (Present/Absent): ")

    attendance[name] = status.capitalize()

print("\n--- Attendance Report ---")

present = 0
absent = 0

for name, status in attendance.items():
    print(name, ":", status)

    if status == "Present":
        present += 1
    else:
        absent += 1

print("\nTotal Students:", n)
print("Total Present:", present)
print("Total Absent:", absent)

percentage = (present / n) * 100
print("Attendance Percentage:", percentage, "%")
