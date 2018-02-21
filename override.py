class Employee:
    def setNumberOfWorkingHours(self):
	self.numberofWorkingHours = 40
		
    def displayNumberOfWorkingHours(self):
	print(self.numberofWorkingHours)


class Tainee(Employee):
    def setNumberOfWorkingHours(self):
	self.numberofWorkingHours = 45
	
    def resetNumberOfWorkingHours(self):
	super.setNumberOfWorkingHours()
		
employee = Employee()
employee.setNumberOfWorkingHours()
print("Number of working hours of employee:")
employee.displayNumberOfWorkingHours()

trainee = Tainee()
trainee.setNumberOfWorkingHours()
print("Number of working hours of employee:")
trainee.displayNumberOfWorkingHours()

trainee.resetNumberOfWorkingHours()
print("Reset Number of working hours of employee:")
trainee.displayNumberOfWorkingHours()

