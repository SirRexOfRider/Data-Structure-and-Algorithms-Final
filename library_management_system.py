import time

from abc import ABC, abstractmethod
import math

class LibraryManagementSystem(ABC):
    """ 
    A library management system framework. 

    Different frameworks (linear, binary, etc.) must implement insertion (shelve) and index resolution (_find_index)
    """

    def __init__(self, books):
        """ Creates a new library management system. """
        self._books = books

    def empty(self):
        """ Creates an empty library with no books. """
        self.__init__([])

    def __len__(self):
        return len(self._books)

    @abstractmethod
    def shelve(self, book): 
        """ A method that should add a book to the library. """
        # might be able to make this work with _find_index, might be too complex 
        ...

    def unshelve(self, title): 
        """ 
        Removes and returns the book in the library with title. 
        If the book is not in the library, None is returned and the library is not changed.
        """
        index = self._find_index(title)
        if index is None:
            return None
        book = self._books.pop(index)
        return book

    def find(self, title):
        """ 
        Finds and returns the book in the library with title. 
        If the book is not in the library, None is returned.
        """
        index = self._find_index(title)
        if index is None:
            return None
        book = self._books[index]
        return book

    @abstractmethod
    def _find_index(self, title):
        """ A method that should find the position of the book with the given title. """
        ...

    def __str__(self): 
        """ Returns a basic string representation of the library. """
        return "\n".join(map(str, self._books))

class LinearSearchLMS(LibraryManagementSystem):
    """ 
    A library that uses linear search to find books. 
    Inserting is O(1).
    Searching is O(n).
    """

    # not required because of inheiritance rules
    # def __init__(self, books):
    #     """ Returns a library with the specified books. """
    #     super().__init__(books)

    def shelve(self, book): 
        """ Shelves the book at the end of the library. """
        self._books.append(book)

    def _find_index(self, title):
        """ Searches linearly for the position of the book with title. """
        for index, book in enumerate(self._books):
            if book.title().lower() == title.lower():
                return index
        return None

class BinarySearchLMS(LibraryManagementSystem):
    """ 
    A library that uses binary search to find books. 
    Inserting is O(n). -- todo, use binary insertion
    Searching is O(log n). -- todo, make binary search use bounds to handle duplicate key values
    """
    def __init__(self, books):
        """ Creates a new library with the specified books; sorts books for binary search. """
        super().__init__(books)
        self._books.sort(key=lambda book: self._key(book.title()))

    @staticmethod
    def _key(title):
        """ 
        Generates the values used to sort the books.
        This implementation is simple and does not create very unique keys. 
        """
        return sum(map(ord, title))

    def shelve(self, book): 
        """ 
        Adds the specified book to the library. 
        Works in linear time.
        TODO -- adapt a binary search to insert -> O(log n)
        """
        # if no books are in the library, just add the book as the first
        if len(self) == 0:
            self._books.append(book)
            return 
        # otherwise, find the position of the book in the library
        for index in range(len(self)):
            if self._key(book.title()) <= self._key(self._books[index].title()):
                self._books.insert(index, book)
                return
        # if the book's key is the highest, add it at the end
        self._books.append(book)

    def _find_index(self, title):
        """ 
        Finds and returns the index of the book in the library with title. 
        Uses binary search to find the books with the same keys then linearly searches for the book with the correct title. 
        Average case -- O(log n) -- Reasonable key function and different books.
        Worst case -- O(n) -- Would only occur if the key function was extremely bad or the same book had n occurences in the library. 
        """
        first_occurence_index = lower_bound_binary_search(self._books, title, lambda book: self._key(book.title()))
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

    # Used for inspecting key values and collisions
    def __str__(self):
        string = ""
        for book in self._books:
            string += str(book) + " key: " + str(self._key(book.title())) + "\n"
        return string

# class HashMapLMS(LMS):
#     def __init__(self, books): 
#         super().__init__(books)
#         self._hashmap = dict()



def binary_search(collection, target, key):
    """ 
    A basic binary search in a sorted collection. 

    collection - the collection to search through
    target_key - the key of the desired object
    key - the function that generates keys from objects in the collection
    """
    target_key = key(target)
    left = 0
    right = len(collection) - 1

    while left <= right:
        middle = left + math.floor((right - left) / 2)
        if key(collection[middle]) < target_key:
            left = middle + 1
        elif key(collection[middle]) > target_key:
            right = middle - 1
        else:
            return middle
    return None

def lower_bound_binary_search(collection, target, key):
    """ 
    Finds the first occurence of target_key in collection.  
    Note -- in the case of duplicate keys, this function finds the first occurence.
    
    collection - the collection to search through
    target_key - the key of the desired object
    key - the function that generates keys from objects in the collection
    """
    target_key = key(target)
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

# class Library:
#     def __init__(self, listOfBooks):
#         self.books = listOfBooks

#     def displayBooks(self):
#         print("The available books in the library are: ")
#         for book in self.books:
#             print(" *" + book)
        
#     #LINEAR TIME
#     #Search for the book by ID
#     #O(n)
#     def Linear_search(self, bookID):
        
#         #Running time
#         start = time.perf_counter()
        
#         #Book currently not found
#         found = False
        
#         #For as many books in the LMS
#         for x in range(len(self.books)):
            
#             #If the bookname is the same for the current entry in the database
#             #Declare that it was found
#             if bookID == self.books[x][-1]:
#                 print(f"Found the book {self.books[bookID -1][0]} using this ID: {bookID} ")
#                 #self.books.remove(bookName)
#                 found = True
    
#         if not found:
#             print(f"Could not find ID: {bookID} in the LMS")
            
#         #Stop time
#         end = time.perf_counter()
        
#         #Return the amount of time taken for the function call
#         return round(end - start, 2)
             
       
#     #TODO: NEEDS IMPLEMENTED      
#     def Binary_search(self, bookID):   
#         pass

            
            

#     def returnBook(self, bookName):
#         self.books.append(bookName)
#         print("Thanks for returning it. Hope you enjoy reading it")

#     def addBook(self, bookName):
#         self.books.append(bookName)
#         print("Thanks for donating the book to the library!!")

# class student:
#     def requestBook(self):
#         self.book = input("Enter the name of the book: ")
#         return self.book
    
#     def returnBook(self):
#         self.book = input("Enter the name of the book you want to return: ")
#         return self.book

#     def addBook(self):
#         self.book = input("Enter the name of the book you want to add to the library: ")
#         return self.book

# if __name__ == "__main__":
#     centralLibrary = Library(["Algorithms", "Sherlock Holmes", "Django", "HTML Notes", "Python Notes", "C++ Notes", "Java Notes"])
#     student = student()
#     msg = ''' 
# ### Welcome to the Central library of the university ###
# Please Enter the option:
# 1. List the names of all available books
# 2. Request to borrow a book
# 3. Return a book
# 4. Add a book to the library
# 5. Exit the Library
#     '''
#     print(msg)
#     while(True):
#         wlcMsg = '''
#         Please Enter the option : 
#         '''
#         print(wlcMsg)
#         a = int(input("How can I help you? : "))
#         if a == 1:
#             centralLibrary.displayBooks()
#         elif a == 2:
#             centralLibrary.borrowBooks(student.requestBook())
#         elif a == 3:
#             centralLibrary.returnBook(student.returnBook())
#         elif a == 4:
#             centralLibrary.addBook(student.addBook())
#         elif a == 5:
#             print("Thanks for using the Central Library!!")
#             exit()
#         else:
#             print("You entered an invalid choice.....")