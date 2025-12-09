from timer import *
from book_csv import read_n_books_from_csv_file, BookCsvFormatError
from library_management_system import *
from book import Book

def func(blms, title):
	return blms.find(title)

def main():
	print("Hello World!")
	books = []
	try:
		books = read_n_books_from_csv_file("books.csv", 1000)
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

	collection = [1, 2, 4, 5, 7, 8, 10, 11]
	target = 6
	position = binary_search(collection, target, lambda x: x)
	print(f"{position=}")

	print(blms)
	title = "ClashofCaivilizations"
	print(f"{blms._key(title)}")
	book = print_benchmark(10)(func)(blms, "The Drunkard's Walk")
	# print(f"time: {time} s")
	print(f"found: {blms.find(title)}")
	print(f"found: {blms.find("The Drunkard's Walk")}")

	# blms.shelve(Book("Empire of the Mughal - The Serpent's Tooth", "Alex Rutherford"))


if __name__ == "__main__":
	main()