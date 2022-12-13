import openpyxl

def import_books_from_excel(filepath):
    # Load the workbook from the given filepath
    # Reminder to add the filepath at the end
    workbook = openpyxl.load_workbook(filepath)
    # Get the first sheet from the workbook
    sheet = workbook.worksheets[0]

    books = []
    # Iterate over all rows in the sheet
    for row in sheet.rows:
        # Get the values of the first three cells in the row (assuming the first three columns contain the book name, ISBN and author respectively)
        name, ISBN, author = row[0].value, row[1].value, row[2].value
        # Create a Book object using the values and append it to the books list
        books.append(Book(name, author, ISBN))

    # Return the list of books
    return books

# Import the import_books_from_excel function
from book_import_functions import import_books_from_excel

# Create a shelf object
shelf = Shelf("Fiction")
# Populate the shelf with books from the Excel file
shelf.populate_books(import_books_from_excel)
