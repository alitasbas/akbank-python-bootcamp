import operator as op


class Library:
    def __init__(self):
        self.list = open("books.txt", "a+")

    def __del__(self):
        self.list.close()

    def __str__(self):
        return self.list.read()

    def list_books(self):
        self.list.seek(0)
        content = self.list.read()
        books = content.splitlines()
        if books:
            for book in books:
                name, author = book.split(",")[0:2]
                print("Title:", name.title() + ", Author:", author.title())
        else:
            print("There are no books. Enter 2 to add some!")

    def add_book(self):
        book_name = input("Book Name: ")
        author_name = input("Author Name: ")
        release_date = input("Release Date: ")
        page_count = input("Page Count: ")
        self.list.write(f"{book_name},{author_name},{release_date},{page_count}\n")# \n to prepare for next addition by skipping a line

    def delete_book(self):
        found = False
        book_to_delete = input("Book to Delete: ")
        self.list.seek(0)
        content = self.list.read()
        books = content.splitlines()
        for index, book in enumerate(books):
            # if book_to_delete in book:
            if op.contains(book.split(",")[0].lower(), book_to_delete.lower()):
                found = True
                del books[index]
                self.list.seek(0)
                self.list.truncate()
                self.list.writelines(books)
        if not found:
            print(f"No book named {book_to_delete} found")

        if found:
            print(f"{book_to_delete} deleted successfully")
            found = False


lib = Library()

while True:
    print("*** MENU***\n1) List Books\n2) Add Book\n3) Remove Book\nq) Exit")
    command = input("What would you like to do? ")
    if command == "1":
        lib.list_books()
    elif command == "2":
        lib.add_book()
    elif command == "3":
        lib.delete_book()
    elif command.lower() == "q":
        break
    else:
        print("Please choose one of the following.")