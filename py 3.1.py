
# Contact Book using Lists and Dictionaries

contacts = []

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }

        contacts.append(contact)
        print("Contact added successfully!")

    elif choice == 2:
        print("\nContact List:")
        for c in contacts:
            print("Name:", c["name"])
            print("Phone:", c["phone"])
            print("Email:", c["email"])
            print("----------------")

    elif choice == 3:
        search = input("Enter name to search: ")
        found = False

        for c in contacts:
            if c["name"].lower() == search.lower():
                print("Contact Found!")
                print("Name:", c["name"])
                print("Phone:", c["phone"])
                print("Email:", c["email"])
                found = True
                break

        if not found:
            print("Contact not found!")

    elif choice == 4:
        print("Exiting Contact Book...")
        break

    else:
        print("Invalid choice!")

