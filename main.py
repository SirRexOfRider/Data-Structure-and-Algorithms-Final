from timer import *
from library_management_system import *
from binary_search_lms import *
from book import Book
import title_keys
import book_csv

def main():
	print("Hello World!")
	print("Done")
	# books = []
	# try:
	# 	books = book_csv.read_n_books_from_csv_file("books.csv", 20)
	# except BookCsvFormatError as e:
	# 	print(f"{e}")

	# llms = LinearSearchLMS(books)
	# print(llms)
	# print()
	# print()
	# blms = BinarySearchLMS(books, title_keys.positional_ord)
	# blms.shelve(Book("tSructure & Interpretation of Computer Programs", "Gerald Sussman"))
	# blms.shelve(Book("Structure & Interpretation of Computer Prograsm", "Gerald Sussman"))
	# blms.shelve(Book("Clash of Civilizations and Remaking of the World Odrer", "Samuel Huntington"))

	# print(blms)
	# title = "ClashofCaivilizations"
	# print(f"{blms._key(title)}")
	# book = print_benchmark(10)(func)(blms, "The Drunkard's Walk")
	# # print(f"time: {time} s")
	# print(f"found: {blms.find(title)}")
	# print(f"found: {blms.find("The Drunkard's Walk")}")

	# blms.shelve(Book("Empire of the Mughal - The Serpent's Tooth", "Alex Rutherford"))


if __name__ == "__main__":
	main()