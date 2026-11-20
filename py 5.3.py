
import random

# Dice Simulator Using Random Module

while True:
    print("\n--- Dice Simulator ---")
    print("1. Roll Dice")
    print("2. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        dice = random.randint(1, 6)
        print("You rolled:", dice)

        if dice == 6:
            print("Congratulations! You got the highest number!")

    elif choice == 2:
        print("Thank you for playing!")
        break

    else:
        print("Invalid choice! Try again.")
