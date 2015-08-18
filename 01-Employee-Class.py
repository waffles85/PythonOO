__author__ = 'waffles85'


class Employee:
    'Common class for all employees'

    'Class variable inherited by all instances of "Employee" '
    empCount = 0

    def __init__(self, EmplName, BaseSalary, Bonus, CareerLevel):
        self.EmplName = EmplName
        self.BaseSalary = BaseSalary
        self.Bonus = Bonus
        self.CareerLevel = CareerLevel

    def displayCount(self):
        print 'The number of employees is %d' % Employee.empCount

    def displayEmployeeDetails(self):
        print 'Employee Name :' + self.EmplName
