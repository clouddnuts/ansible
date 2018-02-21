class Employee:

# init method will be first called
     def __init__(self,par_name):
         self.name = par_name

     def displayEmployeeName(self):
         print(self.name)


employeeOne = Employee("Mark")
employeeTwo = Employee("John")

employeeOne.displayEmployeeName()
employeeTwo.displayEmployeeName()
         
