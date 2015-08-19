__author__ = 'waffles85'


class Employee:
    '''
    Common class for all employees
    '''

    #Class variable inherited by all instances of "Employee"

    empCount = 0

    def __init__(self, EmplName, BaseSalary, Bonus, CareerLevel):
        self.EmplName = EmplName
        self.BaseSalary = BaseSalary
        self.Bonus = Bonus
        self.CareerLevel = CareerLevel
        Employee.empCount += 1

    def displayCount(self):
        print 'The number of employees is %d' % Employee.empCount

    def displayEmployeeDetails(self):
        print 'Employee Name :' + self.EmplName
        print 'Salary: %d' %self.BaseSalary

#Instantiates e1, sets details
e1 = Employee('Jim',CareerLevel = 4, BaseSalary = 19000, Bonus = 0.15)
e1.displayEmployeeDetails()
e1.displayCount()

#getattr can get attributes of an object
#print getattr(e1,'Bonus')

#hassttr checks if object has attribute
print hasattr(e1,'Bonus')
#print hasattr(e1,'NoBonus')

#setattr sets attribute value
#setattr(e1,'Bonus', 0.23)
#print getattr(e1,'Bonus')

#delattr deletes attribute
#delattr(e1,'Bonus')
#print getattr(e1,'Bonus')


'''
There are a number of built-in method in any class
__dict__ is the name space of the class
'''
print "e1.__dict__ : " + str(e1.__dict__)

#__doc__ os the doc string
print "e1.__doc__ : " + str(e1.__doc__)

#__name__ is the class name
print "e1.__name__ : " + str(Employee.__name__)

# __bases__ is a tuple containing base classes, in order of their occurance
print 'e1.__class__.__bases__ : ' + str(e1.__class__.__bases__)

# __module__ module name in which the class is defined
print 'e1.__module__ : %' + e1.__module__

print Employee


