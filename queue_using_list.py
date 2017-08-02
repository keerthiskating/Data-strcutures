from slist import *
class queue():
	 
	def __init__(self):
		
		s=slist()
		self.s = s

	def queue(self,val):
	
	 	self.s.addatfirst(val)

	def dequeue(self):

		self.s.removeatlast()

	def show(self):
	
		self.s.printlist()

	def length(self):
		
		self.s.length()

q=queue()
q.queue(2)
q.show()
q.length()
print "\n"
q.queue(3)
q.show()
q.length()
print "\n"
q.dequeue()
q.show()
q.length()
print "\n"
