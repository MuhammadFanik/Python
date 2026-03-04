# Step 1 — Set up the constructor
# In __init__, initialize two attributes: self.books as an empty list, and self.members as an empty dictionary. Then call self.menu() at the end.
# Step 2 — Build the menu
# Create a menu() method that shows these options and calls the appropriate method based on user input:
#
# Add a book
# View all books
# Register a member
# Issue a book to a member
# Exit
#
# Step 3 — Add a book
# Create an add_book() method that takes a book name as input and appends it to self.books. Print a confirmation message, then call self.menu().
# Step 4 — View all books
# Create a view_books() method that prints all books in self.books. If the list is empty, print "No books available". Then call self.menu().
# Step 5 — Register a member
# Create a register_member() method that takes a member name as input and adds them to self.members dictionary with an empty list as their value (this list will hold their issued books). Then call self.menu().
# Step 6 — Issue a book
# Create an issue_book() method that asks for a member name and a book name. If both exist (member in self.members and book in self.books), remove the book from self.books and add it to that member's list in self.members. Otherwise print an appropriate error message. Then call self.menu().
# Step 7 — Create the object
# At the bottom, write library = Library() to kick everything off.

# Library Management System
class Library:
    # Constructor method
    def __init__(self):
        self.books = []
        self.members = {}
        self.menu()

    # Menu method
    def menu(self):
        menu_input = int(input("""
        1. Press 1 to add a book
        2. Press 2 to view all the books
        3. Press 3 to register a member
        4. Press 4 to issue a book to a member
        5. Press anything else to exit the library managment system
        """))
        if menu_input == 1:
            self.add_book()
        elif menu_input == 2:
            self.all_books()
        elif menu_input == 3:
            self.register_member()
        elif menu_input == 4:
            self.issue_book()
        else:
            pass

    # Add book
    def add_book(self):
        book_name = input("Enter the book you want to add: ")
        self.books.append(book_name)
        print(f"{book_name} added to the library")
        # Call the menu again
        self.menu()

    # View all the books
    def all_books(self):
        if len(self.books) == 0:
            print("No books available")
        else:
            for book in self.books:
                print(f"{book}")

        # Print the menu
        self.menu()

    # Register a member
    def register_member(self):
        member_name = input("Enter your name: ")
        self.members[member_name] = []
        # Print the menu
        self.menu()

    # Issue a book
    def issue_book(self):
        user_name = input("Enter your name: ")
        book_to_issue = input("Enter the book you want to issue: ")
        if book_to_issue in self.books and user_name in self.members:
            self.books.remove(book_to_issue)
            self.members[user_name].append(book_to_issue)
            print(f"{book_to_issue} has been issued to {user_name}")
        elif book_to_issue not in self.books:
            print("Book not found")
        elif user_name not in self.members:
            print("Member not found")

        self.menu()

stu1 = Library()