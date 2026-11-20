
# Library Management System Using OOP

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append({"title": book, "available": True})
        print("Book added successfully!")

    def view_books(self):
        print("\n--- Library Books ---")
        for book in self.books:
            status = "Available" if book["available"] else "Borrowed"
            print("Book:", book["title"], "| Status:", status)

    def search_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                print("Book Found:", book["title"])
                print("Status:", "Available" if book["available"] else "Borrowed")
                return
        print("Book not found!")

    def borrow_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                if book["available"]:
                    book["available"] = False
                    print("Book borrowed successfully!")
                else:
                    print("Book is already borrowed!")
                return
        print("Book not found!")

    def return_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                if not book["available"]:
                    book["available"] = True
                    print("Book returned successfully!")
                else:
                    print("Book was not borrowed!")
                return
        print("Book not found!")


library = Library()

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        title = input("Enter book title: ")
        library.add_book(title)

    elif choice == 2:
        library.view_books()

    elif choice == 3:
        title = input("Enter book title: ")
        library.search_book(title)

    elif choice == 4:
        title = input("Enter book title: ")
        library.borrow_book(title)

    elif choice == 5:
        title = input("Enter book title: ")
        library.return_book(title)

    elif choice == 6:
        print("Exiting Library Management System...")
        break

    else:
        print("Invalid choice!")
