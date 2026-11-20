
# Bank Account System Using OOP

class BankAccount:

    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited successfully!")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        else:
            print("Insufficient balance!")

    def display(self):
        print("\n--- Account Details ---")
        print("Account Holder:", self.name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


name = input("Enter account holder name: ")
account_number = input("Enter account number: ")
balance = float(input("Enter initial balance: "))

account = BankAccount(name, account_number, balance)

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Display Account")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)

    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)

    elif choice == 3:
        account.display()

    elif choice == 4:
        print("Thank you for using our bank!")
        break

    else:
        print("Invalid choice!")
