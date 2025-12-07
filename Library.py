import time


class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayBooks(self):
        print("The available books in the library are: ")
        for book in self.books:
            print(" *" + book)
        
    #LINEAR TIME
    #Search for the book by ID
    #O(n)
    def Linear_search(self, bookID):
        
        #Running time
        start = time.perf_counter()
        
        #Book currently not found
        found = False
        
        #For as many books in the LMS
        for x in range(len(self.books)):
            
            #If the bookname is the same for the current entry in the database
            #Declare that it was found
            if bookID == self.books[x][-1]:
                print(f"Found the book {self.books[bookID -1][0]} using this ID: {bookID} ")
                #self.books.remove(bookName)
                found = True
    
        if not found:
            print(f"Could not find ID: {bookID} in the LMS")
            
        #Stop time
        end = time.perf_counter()
        
        #Return the amount of time taken for the function call
        return round(end - start, 2)
             
       
    #TODO: NEEDS IMPLEMENTED      
    def Binary_search(self, bookID):   
        pass

            
            

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning it. Hope you enjoy reading it")

    def addBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for donating the book to the library!!")

class student:
    def requestBook(self):
        self.book = input("Enter the name of the book: ")
        return self.book
    
    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        return self.book

    def addBook(self):
        self.book = input("Enter the name of the book you want to add to the library: ")
        return self.book

if __name__ == "__main__":
    centralLibrary = Library(["Algorithms", "Sherlock Holmes", "Django", "HTML Notes", "Python Notes", "C++ Notes", "Java Notes"])
    student = student()
    msg = ''' 
### Welcome to the Central library of the university ###
Please Enter the option:
1. List the names of all available books
2. Request to borrow a book
3. Return a book
4. Add a book to the library
5. Exit the Library
    '''
    print(msg)
    while(True):
        wlcMsg = '''
        Please Enter the option : 
        '''
        print(wlcMsg)
        a = int(input("How can I help you? : "))
        if a == 1:
            centralLibrary.displayBooks()
        elif a == 2:
            centralLibrary.borrowBooks(student.requestBook())
        elif a == 3:
            centralLibrary.returnBook(student.returnBook())
        elif a == 4:
            centralLibrary.addBook(student.addBook())
        elif a == 5:
            print("Thanks for using the Central Library!!")
            exit()
        else:
            print("You entered an invalid choice.....")