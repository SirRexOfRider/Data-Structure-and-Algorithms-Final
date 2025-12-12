from timer import *
from library_management_system import *
from binary_search_lms import *
from linear_search_lms import *
from hash_map_lms import *
from book import Book
import title_keys
import book_csv

import time

@print_benchmark(100)
def test():
	for i in range(1000):
		for j in range(1000):
			i * j

def main():
	test()
	# benchmarker = Benchmarker()
	# benchmarker.add_time(1000000)
	# benchmarker.add_function_call(test)()
	# benchmarker.add_function_call(test)()
	# benchmarker.add_function_call(test)()

	# print(benchmarker)
	# test()
	# print(TimePrefix.AUTO.get_string(1_000_000_000_000))
	# n = prompt_user_for_number_in_range("How many books do you want to add to the libraries?", 1, 1_000_000)

	# books = []
	# try:
	# 	books = book_csv.read_n_books_from_csv_file("data/large_books_file.csv", 10000)
	# except BookCsvFormatError as e:
	# 	print(f"Error while parsing books: {e}")

	# n = prompt_user_for_number_in_range("How many times do you want to initialize the libraries?", 1, 100)

	# llms = print_benchmark(n)(LinearSearchLMS)(books)
	# blms = print_benchmark(n)(BinarySearchLMS)(books)
	# hlms = print_benchmark(n)(HashMapLMS)(books)

	# llms = LinearSearchLMS(books)
	# blms = BinarySearchLMS(books)
	# hlms = HashMapLMS(books)

	# print_execution_time_ns(llms.find)(llms.random_book().title())

	# n = prompt_user_for_number_in_range("How many times do you want to run the search function?", 1, 1_000_000)

	# print("Linear search library results: ")
	# print_benchmark(n)(test_find)(llms)
	# print("Binary search library results: ")
	# print_benchmark(n)(test_find)(blms)
	# print("Hash map library results: ")
	# print_benchmark(n)(test_find)(hlms)

if __name__ == "__main__":
	main()