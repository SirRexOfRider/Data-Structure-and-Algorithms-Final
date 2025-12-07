from timer import print_execution_time
# import csv

from book_csv import read_books_from_csv_file, BookCsvFormatError
from library_management_system import LinearSearchLMS, BinarySearchLMS
from book import Book

def main():
	print("Hello World!")
	books = []
	try:
		books = read_books_from_csv_file("books.csv")
	except BookCsvFormatError as e:
		print(f"{e}")

	# llms = LinearSearchLMS(books)
	# print(llms)
	# print()
	# print()
	blms = BinarySearchLMS(books)
	blms.shelve(Book("Structure & Interpretation of Computer Prograsm", "Gerald Sussman"))
	blms.shelve(Book("tSructure & Interpretation of Computer Programs", "Gerald Sussman"))

	blms.shelve(Book("Clash of Civilizations and Remaking of the World O drer", "Samuel Huntington"))
	print(blms)

	print(f"found: {blms.find("Clash of Civilizations and Remaking of the World O drer")}")
	print(f"found: {blms.find("Structure & Interpretation of Computer Prograsm")}")

	# blms.shelve(Book("Empire of the Mughal - The Serpent's Tooth", "Alex Rutherford"))


if __name__ == "__main__":
	main()