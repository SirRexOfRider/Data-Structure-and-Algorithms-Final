import time
import math
from enum import Enum

##################################################
############# TIMING UTILITY CLASSES #############
##################################################

class SecondsFormatter(Enum):
	""" 
	An enum used to convert seconds between metric prefixes on seconds. 
	SecondsPrefix.SECONDS represents seconds,
	SecondsPrefix.MILLISECONDS represents milliseconds,
	SecondsPrefix.MICROSECONDS represents microseconds, 
	SecondsPrefix.NANOSECONDS represents nanoseconds, and 
	SecondsPrefix.AUTO automatically selects the best conversion and should be used as the default. 
	"""
	SECONDS = 9
	MILLISECONDS = 6
	MICROSECONDS = 3
	NANOSECONDS = 0 	
	AUTO = None

	def convert(self, nanoseconds):
		converted_form = self
		if self is SecondsFormatter.AUTO:
			power = math.floor(math.log(nanoseconds, 10))
			if power <= 2:
				converted_form = SecondsFormatter.NANOSECONDS
			elif 3 <= power <= 5:
				converted_form = SecondsFormatter.MICROSECONDS
			elif 6 <= power <= 8:
				converted_form = SecondsFormatter.MILLISECONDS
			elif 9 <= power:
				converted_form = SecondsFormatter.SECONDS
		converted_time = nanoseconds / 10**converted_form.value
		converted_time_name = converted_form.name.lower()
		return (converted_time, converted_time_name)

class Benchmarker:
	""" Used to generate execution time statistics from function calls. """

	def __init__(self, total_formatter=SecondsFormatter.AUTO, stats_formatter=SecondsFormatter.AUTO):
		""" Creates a new benchmarker. """
		self._count = 0
		self._total_ns = 0
		self._min_ns = math.inf
		self._max_ns = 0
		self._total_formatter = total_formatter
		self._stats_formatter = stats_formatter

	def add_time(self, nanoseconds):
		""" 
		Add the execution time to the benchmarker. 
		Added time must be in nanoseconds. 
		"""
		self._count += 1
		self._total_ns += nanoseconds
		self._min_ns = min(self._min_ns, nanoseconds)
		self._max_ns = max(self._max_ns, nanoseconds)

	def count(self):
		""" Returns the total amount of executions measured. """
		return self._count

	def total(self):
		""" Returns the total amount of execution time measured in nanoseconds. """
		return self._total_ns

	def minimum(self):
		""" Returns the minimum amount of execution time measured in nanoseconds. """
		return self._min_ns

	def maximum(self):
		""" Returns the maximum amount of execution time measured in nanoseconds. """
		return self._max_ns

	def average(self):
		""" Returns the average amount of execution time measured in nanoseconds. """
		return self._total_ns / self._count

	def set_total_formatter(self, total_formatter):
		""" Sets the total formatter to the specified seconds formatter. """
		self._total_formatter = total_formatter

	def set_stats_formatter(self, stats_formatter):
		""" Sets the statistics formatter to the specified seconds formatter. """
		self._stats_formatter = stats_formatter

	def __str__(self):
		""" Returns a report of all of the stats generated from benchmarking. """

		if self._count <= 0:
			raise AttributeError("Must add times to benchmarker before printing results.")

		converted_total, converted_total_name = self._total_formatter.convert(self.total())
		converted_minimum, converted_minimum_name = self._stats_formatter.convert(self.minimum())
		converted_average, converted_average_name = self._stats_formatter.convert(self.average())
		converted_maximum, converted_maximum_name = self._stats_formatter.convert(self.maximum())

		report = f"""{self._count} executions:
total ... {converted_total:.3f} {converted_total_name} 
min ..... {converted_minimum:.3f} {converted_minimum_name}
avg ..... {converted_average:.3f} {converted_average_name}
max ..... {converted_maximum:.3f} {converted_maximum_name}"""

		return report

#################################################
############### TIMING DECORATORS ###############
#################################################

def print_execution_time(formatter=SecondsFormatter.AUTO):
	""" 
	A decorator used to print the execution time of the given function with the specified formatting. 

	formatter (optional) - the format to print the time with (e.g. SecondsFormatter.SECONDS will print the time in seconds).

	USAGE:

	#################### METHOD 1 ####################
	Will always print execution time whenever the function is called.
	
	@print_execution_time()
	def time_this(arg_1, arg_2):
		# doing something here
	
	def main():
		result = time_this(arg_1_value, arg_2_value)

	--- OUTPUT ---
	"time_this executed in 2.305 seconds."

	#################### METHOD 2 ####################
	Can be used to selectively print execution time. 

	def time_this(arg_1, arg_2):
		# doing something here

	def main():
		result = print_execution_time()(time_this)(arg_1_value, arg_2_value)

	--- OUTPUT ---
	"time_this executed in 2.074 seconds."

	#################### FORMATTING ####################
	Formatting can be specified with formatters. 

	SecondsFormatter.SECONDS will force the execution time to be displayed in seconds. 
	SecondsFormatter.MILLISECONDS will force the execution time to be displayed in milliseconds.
	SecondsFormatter.MICROSECONDS will force the execution time to be displayed in microseconds.
	SecondsFormatter.NANOSECONDS will force the execution time to be displayed in nanoseconds.
	SecondsFormatter.AUTO (the default) will choose the most human-readable execution time conversion. 
	
	@print_execution_time(SecondsFormatter.MICROSECONDS)
	def time_this(arg_1, arg_2)
		# doing something here

	--- OR ---

	print_execution_time(SecondsFormatter.MICROSECONDS)(time_this)(arg_1_value)(arg_2_value)

	In both examples, the output will be displayed in microseconds.

	"""
	def print_execution_time_decorator(function):
		def timing_wrap(*args, **kwargs):
			start = time.perf_counter_ns()
			result = function(*args, **kwargs)
			end = time.perf_counter_ns()
			execution_time_in_ns = end - start
			converted_execution_time, converted_execution_time_name = formatter.convert(execution_time_in_ns)
			print(f"{function.__name__} executed in {converted_execution_time:.3f} {converted_execution_time_name}.")
			return result
		return timing_wrap
	return print_execution_time_decorator

def time_execution(function):
	""" 
	A decorator used to wrap the return value with the execution time (in nanoseconds) of the specified function. 
	All functions decorated with this will have their return type changed from <result> to <(result, execution_time_in_ns)>

	USAGE:

	#################### METHOD 1 ####################
	Will always return the wrapped execution time whenever the function is called.
	
	@time_execution
	def time_this(arg_1, arg_2):
		# doing something here
	
	def main():
		result, execution_time_in_ns = time_this(arg_1_value, arg_2_value)

	#################### METHOD 2 ####################
	Can be used to selectively return execution time. 
	Note the functional syntax.

	def time_this(arg_1, arg_2):
		# doing something here

	def main():
		result, execution_time_in_ns = time_execution(time_this)(arg_1_value, arg_2_value)

	"""
	def timing_wrap(*args, **kwargs):
		start = time.perf_counter_ns()
		result = function(*args, **kwargs)
		end = time.perf_counter_ns()
		execution_time_in_ns = end - start
		return (result, execution_time_in_ns)
	return timing_wrap

def print_benchmark(count, total_formatter=SecondsFormatter.AUTO, stats_formatter=SecondsFormatter.AUTO):
	""" 
	A decorator used to print the execution time statistics of the given function over count calls with the specified formatting. 

	count - the amount of times to execute the function to gather data.
		If the count specified is not at least 1, then a ValueError will be raised.
	total_formatter (optional) - the format to print the total execution time with (e.g. SecondsFormatter.SECONDS will print the time in seconds).
	stats_formatter (optional) - the format to print the execution time statistics with (such as minimum, maximum, average, etc.).

	If the function returns a value, only the last one is kept and returned. 

	USAGE:

	#################### METHOD 1 ####################
	Will always print benchmarking results and run the function count times whenever it is called.
	NOTE -- it may be best to only use method 2 for benchmarking. 
	
	@print_benchmark(10)
	def time_this(arg_1, arg_2):
		# doing something here
	
	def main():
		result = time_this(arg_1_value, arg_2_value)

	--- OUTPUT ---
	"--- time_this benchmark results ---
	10 executions:
	total ... 1.182 seconds
	min ..... 84.836 milliseconds
	avg ..... 118.225 milliseconds
	max ..... 147.665 milliseconds"

	#################### METHOD 2 ####################
	Can be used to selectively print benchmarking results. 

	def time_this(arg_1, arg_2):
		# doing something here

	def main():
		result = print_benchmark(10)(time_this)(arg_1_value, arg_2_value)

	--- OUTPUT ---
	"--- time_this benchmark results ---
	10 executions:
	total ... 1.182 seconds
	min ..... 84.836 milliseconds
	avg ..... 118.225 milliseconds
	max ..... 147.665 milliseconds"

	#################### FORMATTING ####################
	Formatting can be specified with formatters. 
	Formatting is separate for the total time and the stats times. 

	SecondsFormatter.SECONDS will force the total/stats times to be displayed in seconds. 
	SecondsFormatter.MILLISECONDS will force the total/stats times to be displayed in milliseconds.
	SecondsFormatter.MICROSECONDS will force the total/stats times to be displayed in microseconds.
	SecondsFormatter.NANOSECONDS will force the total/stats times to be displayed in nanoseconds.
	SecondsFormatter.AUTO (the default) will choose the most human-readable total/stats times conversion. 

	@print_benchmark(10, total_formatter=SecondsFormatter.MICROSECONDS, stats_formatter=SecondsFormatter.MIRCOSECONDS) # using key-words
	def time_this(arg_1, arg_2)
		# doing something here

	--- OR ---

	print_benchmark(10, SecondsFormatter.MICROSECONDS, SecondsFormatter.MICROSECONDS)(time_this)(arg_1_value)(arg_2_value) # without key-words

	In both examples, the benchmarking results (total and stats) will be displayed in microseconds.

	"""
	if count <= 0: 
		raise ValueError("count must be greater or equal to 1 to benchmark")

	def benchmark_decorator(function):
		def benchmark_wrap(*args, **kwargs):
			benchmarker = Benchmarker(total_formatter, stats_formatter)
			for i in range(count):
				start = time.perf_counter_ns()
				result = function(*args, **kwargs)
				end = time.perf_counter_ns()
				execution_time = end - start
				benchmarker.add_time(execution_time)
			print(f"--- {function.__name__} benchmark results ---")
			print(benchmarker)
			return (result, benchmarker)
		return benchmark_wrap
	return benchmark_decorator

def benchmark(count):
	""" 
	A decorator used to wrap the return value with the execution time statistics of the given function over count calls. 
	All functions decorated with this will have their return type changed from <result> to <(result, benchmark)>, 
		where benchmark is a Benchmark object (defined above). 

	count - the amount of times to execute the function to gather data.
		If the count specified is not at least 1, then a ValueError will be raised.

	If the function returns a value, only the last one is kept and returned. 

	USAGE:

	#################### METHOD 1 ####################
	Will always return benchmarking results and run the function count times whenever it is called.
	NOTE -- it may be best to only use method 2 for benchmarking. 
	
	@print_benchmark(10)
	def time_this(arg_1, arg_2):
		# doing something here
	
	def main():
		result, benchmark = time_this(arg_1_value, arg_2_value)

	#################### METHOD 2 ####################
	Can be used to selectively return benchmarking results. 

	def time_this(arg_1, arg_2):
		# doing something here

	def main():
		result, benchmark = benchmark(10)(time_this)(arg_1_value, arg_2_value)

	#################### FORMATTING ####################
	Formatting can be specified with formatters. 
	Formatting is separate for the total time and the stats times. 

	SecondsFormatter.SECONDS will force the total/stats times to be displayed in seconds. 
	SecondsFormatter.MILLISECONDS will force the total/stats times to be displayed in milliseconds.
	SecondsFormatter.MICROSECONDS will force the total/stats times to be displayed in microseconds.
	SecondsFormatter.NANOSECONDS will force the total/stats times to be displayed in nanoseconds.
	SecondsFormatter.AUTO (the default) will choose the most human-readable total/stats times conversion. 

	@benchmark(10, total_formatter=SecondsFormatter.MICROSECONDS, stats_formatter=SecondsFormatter.MIRCOSECONDS) # using key-words
	def time_this(arg_1, arg_2)
		# doing something here

	--- OR ---

	result, benchmark = benchmark(10, SecondsFormatter.MICROSECONDS, SecondsFormatter.MICROSECONDS)(time_this)(arg_1_value)(arg_2_value) # without keywords

	In both examples, the benchmarking results (total and stats) will be displayed in microseconds.

	"""
	if count <= 0: 
		raise ValueError("count must be greater or equal to 1 to benchmark")

	def benchmark_decorator(function):
		def benchmark_wrap(*args, **kwargs):
			benchmarker = Benchmarker()
			for _ in range(count):
				start = time.perf_counter_ns()
				result = function(*args, **kwargs)
				end = time.perf_counter_ns()
				execution_time = end - start
				benchmarker.add_time(execution_time)
			return (result, benchmarker)
		return benchmark_wrap
	return benchmark_decorator


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

# def print_execution_time(function):
	# """ 
	# A decorator used to print the execution time of the given function. 

	# Usage:
	# ### METHOD 1 ###
	# Note -- will always print whenever the function is called.
	
	# @print_execution_time
	# def time_this(arg_1, arg_2):
	# 	# a function that takes a while
	
	# def main():
	# 	time_this(arg_1_value, arg_2_value)

	# --- OUTPUT ---
	# "time_this executed in 2.305397 seconds."

	# ### METHOD 2 ###

	# def time_this(arg_1, arg_2):
	# 	# a function that takes a while

	# def main():
	# 	print_execution_time(time_this)(arg_1_value, arg_2_value)

	# --- OUTPUT ---
	# "time_this executed in 2.074378 seconds."

	# """
# 	def timing_wrap(*args, **kwargs):
# 		start = time.perf_counter()
# 		result = function(*args, **kwargs)
# 		end = time.perf_counter()
# 		execution_time = end - start
# 		print(f"{function.__name__} executed in {execution_time:.6f} seconds.")
# 		return result
# 	return timing_wrap


# def print_benchmark(count):
# 	""" 
# 	A decorator that prints the minimum, average, and maximum execution time of a function over count calls.  
# 	NOTE -- Executes the specified function count times and returns the last result.

# 	Usage:
# 	### METHOD 1 ###
# 	Always prints whenever the function is called.
	
# 	@print_benchmark(10)
# 	def time_this(arg_1, arg_2):
# 		# a function that takes a while
	
# 	def main():
# 		time_this(arg_1_value, arg_2_value)

# 	--- OUTPUT ---
# 	"time_this executed 10 times:
# 	min: 0.098723 seconds
# 	avg: 0.153283 seconds
# 	max: 0.293488 seconds"

# 	### METHOD 2 ###
# 	Used to selectively benchmark.

# 	def time_this(arg_1, arg_2):
# 		# a function that takes a while

# 	def main():
# 		print_benchmark(10)(time_this)(arg_1_value, arg_2_value)

# 	--- OUTPUT ---
# 	"time_this executed 10 times:
# 	min: 0.098723 seconds
# 	avg: 0.153283 seconds
# 	max: 0.293488 seconds"

# 	"""
# 	if count <= 0: 
# 		raise ValueError("count must be greater or equal to 1 to benchmark")

# 	def print_benchmark_decorator(function):
# 		def benchmark_wrap(*args, **kwargs):
# 			minimum_execution_time = math.inf
# 			maximum_execution_time = 0
# 			total_execution_time = 0
# 			for i in range(count):
# 				start = time.perf_counter()
# 				result = function(*args, **kwargs)
# 				end = time.perf_counter()
# 				execution_time = end - start
# 				minimum_execution_time = min(execution_time, minimum_execution_time)
# 				maximum_execution_time = max(execution_time, maximum_execution_time)
# 				total_execution_time += execution_time
# 			average_execution_time = total_execution_time / count
# 			print(f"""{function.__name__} executed {count} times: 
# min: {minimum_execution_time:.6f} seconds
# avg: {average_execution_time:.6f} seconds
# max: {maximum_execution_time:.6f} seconds""")
# 			return result
# 		return benchmark_wrap
# 	return print_benchmark_decorator

# def benchmark(count):
# 	""" 
# 	A decorator used to return the benchmark values of the given function over count executions.
# 	NOTE -- Executes the specified function count times and returns the last result.
	
# 	Wraps the original return value with the execution times in a tuple like: 
# 	(result, minimum_execution_time, average_execution_time, maximum_execution_time) 

# 	Usage:
# 	### METHOD 1 ###
# 	Note -- will always return (result, min_time, avg_time, max_time) whenever the function is called.

	
# 	@benchmark(10)
# 	def time_this(arg_1, arg_2):
# 		# a function that takes a while
	
# 	def main():
# 		(result, min_time, avg_time, max_time) = time_this(arg_1_value, arg_2_value)

# 	### METHOD 2 ###

# 	def time_this(arg_1, arg_2):
# 		# a function that takes a while

# 	def main():
# 		(result, min_time, avg_time, max_time) = benchmark(10)(time_this)(arg_1_value, arg_2_value)
	
# 	"""
# 	if count <= 0: 
# 		raise ValueError("count must be greater or equal to 1 to benchmark")

# 	def benchmark_decorator(function):
# 		def benchmark_wrap(*args, **kwargs):
# 			minimum_execution_time = math.inf
# 			maximum_execution_time = 0
# 			total_execution_time = 0
# 			for i in range(count):
# 				start = time.perf_counter()
# 				result = function(*args, **kwargs)
# 				end = time.perf_counter()
# 				execution_time = end - start
# 				minimum_execution_time = min(execution_time, minimum_execution_time)
# 				maximum_execution_time = max(execution_time, maximum_execution_time)
# 				total_execution_time += execution_time
# 			average_execution_time = total_execution_time / count
# 			return (result, minimum_execution_time, average_execution_time, maximum_execution_time)
# 		return benchmark_wrap
# 	return benchmark_decorator

