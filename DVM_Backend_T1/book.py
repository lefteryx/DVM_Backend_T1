class Book:
    def __init__(self, name, author, ISBN):
        self.name = name
        self.author = author
        self.ISBN = ISBN
        self.borrowed = False
        self.reserved = False

    def borrow_book(self):
        if not self.borrowed and not self.reserved:
            self.borrowed = True
            return "Book borrowed successfully!"
        else:
            return "Book is not available for borrowing at the moment."

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            return "Book returned successfully!"
        else:
            return "Book was not borrowed so it cannot be returned."

    def reserve_book(self):
        if not self.borrowed and not self.reserved:
            self.reserved = True
            return "Book reserved successfully!"
        else:
            return "Book is not available for reservation at the moment."
