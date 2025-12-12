@print_benchmark(1000)
def test_find(lms):
	random_book = lms.random_book()
	lms.find(random_book.title())

@print_benchmark(1000)
def test_unshelve(lms):
	random_book = lms.random_book()
	lms.remove(random_book.title())

def test_shelve(lms, books):
	total_time = 0
	min_time = 0
	max_time = 0

	for book in books:
		(_, execution_time) = time_execution(lms.shelve)(book)
		total_time += execution_time
		min_time = min(min_time, execution_time)
		max_time = max(max_time, execution_time)
	print(f"""test_shelve executed {len(books)} times: 
min: {min_time:.6f} seconds
avg: {average_execution_time:.6f} seconds
max: {maximum_execution_time:.6f} seconds""")