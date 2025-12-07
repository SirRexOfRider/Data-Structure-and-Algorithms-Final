import time

from abc import ABC, abstractmethod
import math

class LibraryManagementSystem(ABC):
    def __init__(self, books):
        self._books = books

    def empty(self):
        self.__init__([])

    @abstractmethod
    def shelve(self, book): 
        ...

    def unshelve(self, title): 
        index = self._find_index(title)
        if index is None:
            return None
        book = self._books.pop(index)
        return book

    def find(self, title):
        index = self._find_index(title)
        if index is None:
            return None
        book = self._books[index]
        return book

    @abstractmethod
    def _find_index(self, title):
        ...

    def __str__(self): 
        return "\n".join(map(str, self._books))

class LinearSearchLMS(LibraryManagementSystem):
    def __init__(self, books):
        super().__init__(books)

    def shelve(self, book): 
        self._books.append(book)

    def _find_index(self, title):
        for index, book in enumerate(self._books):
            if book.title().lower() == title.lower():
                return index
        return None

class BinarySearchLMS(LibraryManagementSystem):
    def __init__(self, books):
        super().__init__(books)
        self._books.sort(key=lambda book: self._key(book.title()))

    @staticmethod
    def _key(title):
        return sum(map(ord, title))

    def shelve(self, book): 
        """ 
        Adds the specified book to the library. 

        Works in linear time.
        """
        # if no books are in the library, just add the book as the first
        if len(self._books) == 0:
            self._books.append(book)
            return 

        # otherwise, find the position of the book in the library
        for index in range(len(self._books)):
            if self._key(book.title()) <= self._key(self._books[index].title()):
                self._books.insert(index, book)
                return

        # if the book's key is the highest, add it at the end
        self._books.append(book)

    def __str__(self):
        string = ""
        for book in self._books:
            string += str(book) + " key: " + str(self._key(book.title())) + "\n"
        return string

    def _find_index(self, title):
        target_key = self._key(title)
        left = 0
        right = len(self._books) - 1

        while left <= right:
            middle = left + math.floor((right - left) / 2)
            if self._key(self._books[middle].title()) < target_key:
                left = middle + 1
            elif self._key(self._books[middle].title()) > target_key:
                right = middle - 1
            else:
                if self._books[middle].title() == title:
                    return middle
                for i in range(left, right + 1):
                    if self._books[i].title() == title:
                        return i
                break
        return None

def binary_search(collection, target_key, key):
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