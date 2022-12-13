class Shelf:
    def __init__(self, genre):
        self.genre = genre
        self.books = []

    def show_books(self):
        if len(self.books) == 0:
            return "No books on the shelf."
        else:
            book_names = []
            for book in self.books:
                book_names.append(book.name)
            return ", ".join(book_names)

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def get_books_count(self):
        return len(self.books)

    def populate_books(self, import_function):
        imported_books = import_function()
        for book in imported_books:
            self.add_book(book)
