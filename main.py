from timer import *
from library_management_system import *
from binary_search_lms import *
from linear_search_lms import *
from hash_map_lms import *
from book import Book
import title_keys
import book_csv

def main():
	books = []
	try:
		books = book_csv.read_n_books_from_csv_file("data/large_books_file.csv", 100)
	except BookCsvFormatError as e:
		print(f"{e}")

	llms = print_benchmark(1)(LinearSearchLMS)(books)
	blms = print_benchmark(1)(BinarySearchLMS)(books, key=title_keys.positional_ord)
	hlms = print_benchmark(1)(HashMapLMS)(books)

	title = "Thinking through the skin" #"Every Day in the Year"
	print()
	print(print_benchmark(1)(llms.find)(title))
	print(print_benchmark(1)(blms.find)(title))
	print(print_benchmark(1)(hlms.find)(title))

if __name__ == "__main__":
	main()