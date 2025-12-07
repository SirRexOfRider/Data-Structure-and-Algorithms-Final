import csv
from book import Book

class BookCsvFormatError(Exception):
	""" Exception raised when encountering a formatting error in book csv files. """

def read_books_from_csv_file(path):
	""" Reads book objects from a csv file with headers Title, AuthorLastName, AuthorFirstName. """
	books = []
	with open(path) as file:
		file_reader = csv.reader(file)
		next(file_reader) # skip the header
		for row in file_reader:
			if len(row) == 1: # book name only
				book = Book(row[0], None)
			elif len(row) == 2: # book name and author last
				book = Book(row[0], row[1])
			elif len(row) == 3: # book name, author last, author first
				book = Book(row[0], row[2] + " " + row[1])
			else:
				raise BookCsvFormatError(f"Invalid row format: {row} found. Format should be Title, AuthorLastName, AuthorFirstName or equivalent.")
			books.append(book)
	return books