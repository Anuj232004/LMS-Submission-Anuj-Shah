class Library:
    def __init__(self, books):
        self.books = books

    def display_books(self):
        if not self.books:
            print("No books available.")
        else:
            print("Available books:")
            for book in self.books:
                print("-", book)

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"You borrowed '{book_name}'")
        else:
            print(f"'{book_name}' is not available.")

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"'{book_name}' has been returned.")


def library_menu():
    lib = Library(["Python Basics", "Data Science", "Algorithms", "Machine Learning"])
    while True:
        print("\n--- Library Menu ---")
        print("1. Display books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            lib.display_books()
        elif choice == '2':
            book = input("Enter book name to borrow: ")
            lib.borrow_book(book)
        elif choice == '3':
            book = input("Enter book name to return: ")
            lib.return_book(book)
        elif choice == '4':
            print("Exiting the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    library_menu()