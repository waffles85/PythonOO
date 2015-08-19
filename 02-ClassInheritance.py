__author__ = 'waffles85'

class Parent:   #define parent class
	def __init__(self):
		print "Calling parent constructor"

	def parentMethod(self, attr):
		print "Calling parent method"

	def setAttr(self, attr):
		Parent.parentAttr = attr

	def getAttr(self):
		print "Parent attribute : " + Parent.parentAttr

class Child(Parent):
	'''
	Child class

	'''

	def __init__(self):
		print "Calling child class"

	def childMethod(self):
		print "Calling Child method"


child1 = Child
print child1
