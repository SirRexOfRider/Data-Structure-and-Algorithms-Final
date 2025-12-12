from library_management_system import LibraryManagementSystem

class LinearSearchLMS(LibraryManagementSystem):
    """ 
    A library that uses linear search to find books. 
    Inserting is O(1).
    Searching is O(n).
    """

    def shelve(self, book): 
        """ Shelves the book at the end of the library. """
        self._books.append(book)

    def _find_index(self, title):
        """ 
        Searches linearly for the position of the book with title -- runs in O(n).
        NOTE -- CASE-SENSITIVE
        """
        for index, book in enumerate(self._books):
            if book.title() == title:
                return index
        return None
