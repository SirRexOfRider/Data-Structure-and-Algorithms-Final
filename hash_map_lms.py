from library_management_system import LibraryManagementSystem

class HashMapLMS(LibraryManagementSystem):
	""" 
    A library that uses a hash map to find books. 

    Insertion and searching is O(1).
    Memory usage is much higher than other variations.  
    """

	def __init__(self, books):
		"""
		Creates a new library with the specified books.

	    books - the books to initialize the library with.  
		"""
		super().__init__(books)
		self._hashmap = dict()
		for index, book in enumerate(self._books):
			self._hashmap[book.title()] = index

	def shelve(self, book):
		""" Adds the specified book to the library. """
		self._books.append(book)
		index = len(self._books) - 1
		self._hashmap[book.title()] = index

	def unshelve(self, title):
		""" 
		Removes the book with the specified title from the library. 
		The unshelve method is overriden to update both the books and hashmap.
		"""
		super().unshelve(title)
		del self._hashmap[title]

	def _find_index(self, title):
		"""
		Returns the index of the book with title. 
		If the title is not in the library, None is returned. 
		"""
		return self._hashmap.get(title)