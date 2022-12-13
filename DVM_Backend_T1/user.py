class BasicUser:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def borrow_book(self, book):
        if self.role == "basic":
            return book.borrow_book()
        else:
            return "Librarian user cannot borrow books."

    def return_book(self, book):
        if self.role == "basic":
            return book.return_book()
        else:
            return "Librarian user cannot return books."

    def reserve_book(self, book):
        if self.role == "basic":
            return book.reserve_book()
        else:
            return "Librarian user cannot reserve books."

    def add_book(self, shelf, book):
        if self.role == "librarian":
            shelf.add_book(book)
            return "Book added to shelf successfully!"
        else:
            return "Basic user cannot add books to shelf."

    def remove_book(self, shelf, book):
        if self.role == "librarian":
            shelf.remove_book(book)
            return "Book removed from shelf successfully!"
        else:
            return "Basic user cannot remove books from shelf."

    def edit_book(self, book, name=None, author=None, ISBN=None):
        if self.role == "librarian":
            if name:
                book.name = name
            if author:
                book.author = author
            if ISBN:
                book.ISBN = ISBN
            return "Book details edited successfully!"
        else:
            return "Basic user cannot edit book details."
