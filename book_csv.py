import csv
from book import Book

class BookCsvFormatError(Exception):
	""" Exception raised when encountering a formatting error in book csv files. """

# def clean_data(path):
# 	data = []
# 	with open(path, "r", encoding="utf-8") as file:
# 		file_reader = csv.reader(file)
# 		for row in file_reader:
# 			if len(row) == 3:
# 				data.append([row[0], row[2] + " " + row[1]])
# 			elif len(row) == 2:
# 				data.append([row[0], row[1]])
# 			else:
# 				data.append([row[0]])

# 	with open(path + "_cleaned", "w", newline="", encoding="utf-8") as file:
# 		file_writer = csv.writer(file)
# 		file_writer.writerows(data)

def read_books_from_csv_file(path):
	""" Reads book objects from a csv file with headers Title, Author. """
	books = []
	with open(path, 'r', encoding='utf-8') as file:
		file_reader = csv.reader(file)
		next(file_reader) # skip the header
		for row in file_reader:
			if len(row) == 1: # book name only
				book = Book(row[0], None)
			elif len(row) == 2: # book name and author name
				book = Book(row[0], row[1])
			else:
				raise BookCsvFormatError(f"Invalid row format: {row} found. Format should be Title, Author or equivalent.")
			books.append(book)
	return books

def read_n_books_from_csv_file(path, amount_of_books_to_read):
	""" Reads a specific amount of book objects from a csv file with headers Title, Author. """
	books = []
	with open(path, 'r', encoding='utf-8') as file:
		file_reader = csv.reader(file)
		next(file_reader) # skip the header
		for amount_read, row in enumerate(file_reader):
			if amount_read >= amount_of_books_to_read:
				return books

			if len(row) == 1: # book name only
				book = Book(row[0], None)
			elif len(row) == 2: # book name and author name
				book = Book(row[0], row[1])
			else:
				raise BookCsvFormatError(f"Invalid row format: {row} found. Format should be Title, Author or equivalent.")
			books.append(book)
	return books