class Employee:
      NumberOfWorkingHours = 8

employeeOne = Employee()
employeeTwo = Employee()

print (employeeOne.NumberOfWorkingHours)
print (employeeTwo.NumberOfWorkingHours)

# class attribute(1)
Employee.NumberOfWorkingHours = 10

print (employeeOne.NumberOfWorkingHours)
print (employeeTwo.NumberOfWorkingHours)

employeeOne.name = 'John'
employeeTwo.name = 'Marry'

print (employeeOne.name)
print (employeeTwo.name)

# instance attribute(2) [first it checks instance attribute then class attribut]
employeeOne.NumberOfWorkingHours = 12

print (employeeOne.NumberOfWorkingHours)
print (employeeTwo.NumberOfWorkingHours)
