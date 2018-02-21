class Apple:

     manufacturer = "Apple INC."
     contact = "www.apple.com"
   
     def contactDetails(self):
         print("To contact please visit Website on :",self.contact)
      

class MacBook(Apple):

     def __init__(self):
         self.yearOfManufacture = "2000"

     def manufactureDetails(self):
        # print("Manufactur:",self.manufacturer)
        # print("Contact:",self.contact)
         print "This MacBook was manufactured in {} by {}".format(self.yearOfManufacture,self.manufacturer)

macbook = MacBook()
macbook.contactDetails()
macbook.manufactureDetails()


