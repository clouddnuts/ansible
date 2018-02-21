# Class => Library
# Layer of abstraction => display available book, to lend book, to add book

# Class => Customer
# Layer of Abstraction => request for a book, return a book

class Library:
   def __init__(self,listOfBook):
      self.availableBooks = listOfBook
       
   
   def displayAvailableBook(self):
       print ("Available Books")
       for book in self.availableBooks:
           print(book)

   def lendBook(self,requestedBook):
       if requestedBook in self.availableBooks:
          print("Now you have browed the book")
          self.availableBooks.remove(requestedBook)
       
       else:
          print("Sorry the book is now available")  

   def addBook(self,returnBook):
       print("Adding the retured book to library")
       self.availablebook.append(returnBook)
       print("You have returned the book. Thank you!!")

class Customer:

   def requestBook(self):
       print ("Enter the name of the book you want to lend:")
       self.book = input()
       return self.book

   def returnBook(self):
       print ("Enter the name of the book which you are returning")
       self.book = input()
       return self.book

library = Library(['ABC','XYX','MNO'])
customer = Customer()

while True:
   print("Enter 1 to Display th avilable book")
   print("Enter 2 to Request a book")
   print("Enter 3 to Return a book")
   print("Enter 4 to exit")

   userChoice = int(input())

   if userChoice is 1:
      library.displayAvailableBook()

   elif userChoice is 2:
      requestedBook = customer.requestBook()
      library.lendBook(requestedBook)

   elif userChoice is 3:
      returnBook = customer.returnBook()
      library.addBook(returnBook)
   
   elif userChoice is 4:
      quit()






