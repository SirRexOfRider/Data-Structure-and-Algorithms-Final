from timing import *

def prompt_user_for_number_in_range(prompt, lower, upper):
	""" Prompts the user for a value between lower and upper using prompt. """
	print(prompt)
	n = None
	while n is None:
		user_input = int(input())
		if user_input < lower or user_input > upper:
			print(f"Please choose a value between {lower} and {upper}.")
		else:
			n = user_input
	return n

@print_benchmark(1000)
def test_find(lms):
	""" Tests the searching of the given lms. """
	random_book = lms.random_book()
	lms.find(random_book.title())

@print_benchmark(1000)
def test_unshelve(lms):
	""" Tests the deletion of the given lms. """
	random_book = lms.random_book()
	lms.remove(random_book.title())

def test_shelve(lms, books):
	""" Tests the insertion of books the given lms. """
	benchmark = Benchmark()
	for book in books:
		(_, execution_time_in_ns) = time_execution(lms.shelve)(book)
		benchmark.add_time(execution_time_in_ns)
	print(f"--- Time stats for adding {len(books)} books to lms ---")
	print(benchmark)