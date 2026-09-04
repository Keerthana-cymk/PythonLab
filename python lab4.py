print("Unit Converter")
print("1. Kilometers to Meters")
print("2. Meters to Kilometers")
print("3. Kilograms to Grams")
print("4. Grams to Kilograms")

choice = int(input("Enter your choice: "))
value = float(input("Enter value: "))

if choice == 1:
    print("Meters =", value * 1000)

elif choice == 2:
    print("Kilometers =", value / 1000)

elif choice == 3:
    print("Grams =", value * 1000)

elif choice == 4:
    print("Kilograms =", value / 1000)

else:
    print("Invalid choice")
