import time

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
		""" The wrapping function used to decorate the given function. """
		start = time.perf_counter()
		result = function(*args, **kwargs)
		end = time.perf_counter()
		execution_time = end - start
		print(f"{function.__name__} executed in {execution_time:.6f} seconds.")
		return result
	return timing_wrap
