class Book:
    def __init__(self, title, author, quantity):
        self.title = title
        self.author = author
        self.quantity = quantity

    def issue_book(self):
        if self.quantity > 0:
            self.quantity -= 1
            print(f"You have successfully issued '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is currently unavailable.")

    def return_book(self):
        self.quantity += 1
        print(f"'{self.title}' has been successfully returned.")

    def get_info(self):
        return f"{self.title} by {self.author}"

    def get_quantity(self):
        return self.quantity


class Member:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.books_issued = []

    def verify_login(self, entered_username, entered_password):
        return self.username == entered_username and self.password == entered_password

    def issue_book(self, book):
        if book.quantity > 0:
            self.books_issued.append(book)
            book.issue_book()
        else:
            print(f"Sorry, '{book.title}' is unavailable.")

    def return_book(self, book):
        if book in self.books_issued:
            self.books_issued.remove(book)
            book.return_book()
        else:
            print("You didn't issue this book.")

    def show_issued_books(self):
        if self.books_issued:
            print("Books issued by you:")
            for book in self.books_issued:
                print(book.get_info())
        else:
            print("No books issued.")


class Library:
    def __init__(self):
        # Predefined books and members (in place of JSON files)
        self.books = [
            Book("The Great Gatsby", "F. Scott Fitzgerald", 5),
            Book("1984", "George Orwell", 3),
            Book("To Kill a Mockingbird", "Harper Lee", 4),
        ]
        self.members = [
            Member("john_doe", "password123"),
            Member("jane_doe", "password456"),
        ]

    def get_books_info(self):
        print("\nLibrary Books Information:")
        for book in self.books:
            print(f"{book.get_info()} - {book.get_quantity()} available")

    def add_book(self, title, author, quantity):
        new_book = Book(title, author, quantity)
        self.books.append(new_book)
        print(f"New book '{title}' added to the library.")

    def register_member(self, username, password):
        new_member = Member(username, password)
        self.members.append(new_member)
        print(f"New member '{username}' registered.")


def user_login(library):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    # Verify the member
    for member in library.members:
        if member.verify_login(username, password):
            print(f"Welcome, {username}!")
            return member
    print("Invalid login credentials. Please try again.")
    return None


def main():
    library = Library()

    # Option for new member registration
    register_choice = input("Do you want to register as a new user? (y/n): ").strip().lower()
    if register_choice == "y":
        new_username = input("Enter your new username: ")
        new_password = input("Enter your new password: ")
        library.register_member(new_username, new_password)

    # Ask the user to log in
    current_member = None
    while current_member is None:
        current_member = user_login(library)

    # Main menu for performing operations
    while True:
        print("\n--- Library System ---")
        print("1. View books")
        print("2. Issue a book")
        print("3. Return a book")
        print("4. Show issued books")
        print("5. Add new book (admin only)")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            library.get_books_info()
        elif choice == "2":
            book_title = input("Enter the title of the book you want to issue: ")
            book = None
            for b in library.books:
                if b.title.lower() == book_title.lower():
                    book = b
                    break
            if book:
                current_member.issue_book(book)
            else:
                print("Book not found.")
        elif choice == "3":
            book_title = input("Enter the title of the book you want to return: ")
            book = None
            for b in current_member.books_issued:
                if b.title.lower() == book_title.lower():
                    book = b
                    break
            if book:
                current_member.return_book(book)
            else:
                print("You didn't issue this book.")
        elif choice == "4":
            current_member.show_issued_books()
        elif choice == "5":
            # For simplicity, we'll treat this as an "admin only" option
            # In a real system, we should have an admin login
            print("Admin access: Add new books")
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            quantity = int(input("Enter book quantity: "))
            library.add_book(title, author, quantity)
        elif choice == "6":
            print("Thank you for using the Library System!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
