import time
import math

def print_execution_time(function):
	""" 
	A decorator used to print the execution time of the given function. 

	Usage:
	### METHOD 1 ###
	Note -- will always print whenever the function is called.
	
	@print_execution_time
	def time_this(arg_1, arg_2):
		# a function that takes a while
	
	def main():
		time_this(arg_1_value, arg_2_value)

	--- OUTPUT ---
	"time_this executed in 2.305397 seconds."

	### METHOD 2 ###

	def time_this(arg_1, arg_2):
		# a function that takes a while

	def main():
		print_execution_time(time_this)(arg_1_value, arg_2_value)

	--- OUTPUT ---
	"time_this executed in 2.074378 seconds."

	"""
	def timing_wrap(*args, **kwargs):
		start = time.perf_counter()
		result = function(*args, **kwargs)
		end = time.perf_counter()
		execution_time = end - start
		print(f"{function.__name__} executed in {execution_time:.6f} seconds.")
		return result
	return timing_wrap

def time_execution(function):
	""" 
	A decorator used to return the execution time of the given function.
	Wraps the original return value with the execution time in a tuple like: 
	(result, execution_time) 

	Usage:
	### METHOD 1 ###
	Note -- will always return (result, time) whenever the function is called.
	
	@time_execution
	def time_this(arg_1, arg_2):
		# a function that takes a while
	
	def main():
		(result, time) = time_this(arg_1_value, arg_2_value)

	### METHOD 2 ###

	def time_this(arg_1, arg_2):
		# a function that takes a while

	def main():
		(result, time) = time_execution(time_this)(arg_1_value, arg_2_value)
	
	"""
	def timing_wrap(*args, **kwargs):
		start = time.perf_counter()
		result = function(*args, **kwargs)
		end = time.perf_counter()
		execution_time = end - start
		return (result, execution_time)
	return timing_wrap

def print_benchmark(count):
	""" 
	A decorator that prints the minimum, average, and maximum execution time of a function over count calls.  
	Executes the specified function count times and returns the last result.

	Usage:
	### METHOD 1 ###
	Always prints whenever the function is called.
	
	@print_benchmark(10)
	def time_this(arg_1, arg_2):
		# a function that takes a while
	
	def main():
		time_this(arg_1_value, arg_2_value)

	--- OUTPUT ---
	"time_this executed 10 times:
	min: 0.098723 seconds
	avg: 0.153283 seconds
	max: 0.293488 seconds"

	### METHOD 2 ###
	Used to selectively benchmark.

	def time_this(arg_1, arg_2):
		# a function that takes a while

	def main():
		print_benchmark(10)(time_this)(arg_1_value, arg_2_value)

	--- OUTPUT ---
	"time_this executed 10 times:
	min: 0.098723 seconds
	avg: 0.153283 seconds
	max: 0.293488 seconds"

	"""
	if count >= 0: 
		raise ValueError("count must be greater or equal to 1 to benchmark")

	def print_benchmark_decorator(function):
		def benchmark_wrap(*args, **kwargs):
			minimum_execution_time = math.inf
			maximum_execution_time = 0
			total_execution_time = 0
			for i in range(count):
				start = time.perf_counter()
				result = function(*args, **kwargs)
				end = time.perf_counter()
				execution_time = end - start
				minimum_execution_time = min(execution_time, minimum_execution_time)
				maximum_execution_time = max(execution_time, maximum_execution_time)
				total_execution_time += execution_time
			average_execution_time = total_execution_time / count
			print(f"""{function.__name__} executed {count} times: 
min: {minimum_execution_time:.6f} seconds
avg: {average_execution_time:.6f} seconds
max: {maximum_execution_time:.6f} seconds""")
			return result
		return benchmark_wrap
	return print_benchmark_decorator


def benchmark(count):
	""" 
	A decorator used to return the benchmark values of the given function over count executions.
	Executes the specified function count times and returns the last result.
	Wraps the original return value with the execution times in a tuple like: 
	(result, minimum_execution_time, average_execution_time, maximum_execution_time) 


	Usage:
	### METHOD 1 ###
	Note -- will always return (result, min_time, avg_time, max_time) whenever the function is called.

	
	@benchmark(10)
	def time_this(arg_1, arg_2):
		# a function that takes a while
	
	def main():
		(result, min_time, avg_time, max_time) = time_this(arg_1_value, arg_2_value)

	### METHOD 2 ###

	def time_this(arg_1, arg_2):
		# a function that takes a while

	def main():
		(result, min_time, avg_time, max_time) = benchmark(10)(time_this)(arg_1_value, arg_2_value)
	
	"""
	if count >= 0: 
		raise ValueError("count must be greater or equal to 1 to benchmark")

	def benchmark_decorator(function):
		def benchmark_wrap(*args, **kwargs):
			minimum_execution_time = math.inf
			maximum_execution_time = 0
			total_execution_time = 0
			for i in range(count):
				start = time.perf_counter()
				result = function(*args, **kwargs)
				end = time.perf_counter()
				execution_time = end - start
				minimum_execution_time = min(execution_time, minimum_execution_time)
				maximum_execution_time = max(execution_time, maximum_execution_time)
				total_execution_time += execution_time
			average_execution_time = total_execution_time / count
			return (result, minimum_execution_time, average_execution_time, maximum_execution_time)
		return benchmark_wrap
	return benchmark_decorator