from timer import print_execution_time
# import csv

from book_csv import read_n_books_from_csv_file, BookCsvFormatError
from library_management_system import LinearSearchLMS, BinarySearchLMS, lower_bound_binary_search
from book import Book

def main():
	print("Hello World!")
	books = []
	try:
		books = read_n_books_from_csv_file("books.csv", 10)
	except BookCsvFormatError as e:
		print(f"{e}")

	# llms = LinearSearchLMS(books)
	# print(llms)
	# print()
	# print()
	blms = BinarySearchLMS(books)
	# blms.shelve(Book("tSructure & Interpretation of Computer Programs", "Gerald Sussman"))

	# blms.shelve(Book("Structure & Interpretation of Computer Prograsm", "Gerald Sussman"))

	# blms.shelve(Book("Clash of Civilizations and Remaking of the World Odrer", "Samuel Huntington"))
	print(blms)
	title = "ClashofCaivilizations"
	print(f"{blms._key(title)}")
	print(f"found: {blms.find(title)}")
	print(f"found: {blms.find("The Drunkard's Walk")}")

	# blms.shelve(Book("Empire of the Mughal - The Serpent's Tooth", "Alex Rutherford"))


if __name__ == "__main__":
	main()