class Book:
	def __init__(self, title, author):
		self._title = title
		self._author = author

	def title(self):
		return self._title

	def author(self):
		return self._author

	def __str__(self):
		if self._author is not None:
			return f"\"{self._title}\" by: \"{self._author}\""
		else:
			return f"\"{self._title}\""