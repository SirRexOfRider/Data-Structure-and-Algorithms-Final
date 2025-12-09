class Book:
	""" A class that represents a book. """

	def __init__(self, title, author):
		""" 
		Creates a book with the specified title and author. 
		
		title - the title of the book.
		author - the author of the book. If the book has no author, None can be used. 
		"""
		self._title = title
		self._author = author

	def title(self):
		""" Returns the title of the book. """
		return self._title

	def author(self):
		""" Returns the author of the book, if one is specified. Otherwise, returns None. """
		return self._author

	def __str__(self):
		""" Returns a string representation of the book. """
		if self._author is not None:
			return f"\"{self._title}\" by: \"{self._author}\""
		else:
			return f"\"{self._title}\""