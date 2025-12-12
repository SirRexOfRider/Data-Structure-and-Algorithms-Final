import math

from library_management_system import LibraryManagementSystem
from title_keys import basic_key

class BinarySearchLMS(LibraryManagementSystem):
    """ 
    A library that uses binary search to find books. 

    Insertion and searching is O(log n). 
    """

    def __init__(self, books, key=basic_key):
        """ 
        Creates a new library with the specified books. 
        Makes a deep copy of the books. 
        Sorts books for binary search. 

        books - the books to initialize the library with. 
        key (optional) - the key function used to sort and search through the library. 

        """
        super().__init__(books)
        self._books.sort(key=lambda book: key(book.title()))
        self._key = key

    def shelve(self, book): 
        """ Adds the specified book to the library. """
        insert_at_index = lower_bound_binary_search(self._books, self._key(book.title()), lambda book: self._key(book.title()))
        if insert_at_index is None:
            self._books.append(book)
        else:
            self._books.insert(insert_at_index, book)

    def _find_index(self, title):
        """ 
        Finds and returns the index of the book in the library with title. 
        Uses binary search to find the books with the same keys then linearly searches for the book with the correct title. 
        
        Average case -- O(log n) -- Reasonable key function and different books.
        Worst case -- O(n) -- Would only occur if the key function was extremely bad or the same book had n occurences in the library. 
        
        NOTE -- CASE-SENSITIVE (even if key is not case-sensitive)
        """
        first_occurence_index = lower_bound_binary_search(self._books, self._key(title), lambda book: self._key(book.title()))
        if first_occurence_index is None:
            return None
        first_occurence_key = self._key(self._books[first_occurence_index].title())
        index = first_occurence_index
        for index in range(first_occurence_index, len(self)): 
            book = self._books[index]   
            book_key = self._key(book.title())
            # if the key no longer matches, then the book does not exist in the library
            if book_key != first_occurence_key: 
                return None
            # if the book title matches, the book was found in the library
            if book.title() == title:
                return index
        return None

def lower_bound_binary_search(collection, target_key, key=lambda x: x):
    """ 
    Finds the first occurence of or where to insert target_key in collection.  
    Note -- in the case of duplicate keys, this function finds the first occurence.
    
    collection - the collection to search through.
    target_key - the key of the desired object.
    key (optional) - the function that generates keys from objects in the collection. 
        If the keys are the objects themselves, there is no need to specify the key. 
    """
    left = 0
    right = len(collection) - 1
    lower_bound = None;

    while left <= right:
        middle = left + math.floor((right - left) / 2)
        if key(collection[middle]) < target_key:
            left = middle + 1
        else:
            lower_bound = middle
            right = middle - 1

    return lower_bound