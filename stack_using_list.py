from slist import *
class stack():

	def __init__(self):
	
		s = slist()
		self.s = s

	def push(self,val):
	 
		self.s.addatfirst(val)

	def pop(self):

		self.s.removeatfirst()

	def show(self):
	
		self.s.printlist()

	def slength(self):
	
		self.s.length()

	def top(self):
	
		self.s.rettop()

a=stack()
a.push(2)
a.show()
a.slength()
a.top()
print "\n"
a.push(3)
a.show()
a.slength()
a.top()
print "\n"
a.push(4)
a.show()
a.slength()
a.top()
print "\n"
a.pop()
a.show()
a.slength()
a.top()
print "\n"
a.pop()
a.show()
a.slength()
a.top()
print "\n"
