from dnode import *
class dlist():
		
	def __init__(self):
	
		self.size = 0
		self.head = dnode()
		self.tail = dnode()
		self.curnode = dnode()

	def isempty(self):

		if (self.size==0):
		  return True
		else:
		  return False

	def add(self,val):
	
		if(self.isempty() == True):
		 self.head = self.tail = dnode(val)
		 self.size += 1
		else:
		 self.curnode = self.head
		 while self.curnode.next != None:
		  self.curnode = self.curnode.next
		 self.curnode.next = dnode(val)
		 self.curnode.next.prev = self.curnode
		 self.size += 1	

	def addatfirst(self,val):

		if(self.isempty() == True):
		 self.head = dnode(val)
		 self.size += 1
		else:
		 temp = self.head
		 temp1 = dnode(val)
		 self.head = temp1
		 temp1.next = temp
		 temp.prev = self.head 
		 self.size += 1

	def addafter(self,val1,val2):
	
		self.curnode = self.head
		while self.curnode.next != None:
		 if(self.curnode.value == val1):
		  break
		 else:
		  self.curnode = self.curnode.next
		n = dnode(val2)
		temp = self.curnode.getnext()
		self.curnode.setnext(n)
		self.curnode.next.setprev(self.curnode)
		self.curnode.next.setnext(temp)
		self.curnode.next.getnext().setprev(self.curnode.next)
		self.size += 1

	def addbefore(self,val1,val2):

		self.curnode = self.head
		while self.curnode.next != None:
		 if(self.curnode.value == val1):
		  break
		 else:
		  self.curnode = self.curnode.next
		n = dnode(val2)
		self.addafter(self.curnode.getprev().getvalue(),val2)
		self.size += 1
	
		
	def printlist(self):
	
		temp = self.head
		while temp.next != None:
		 print temp.getvalue()
		 temp = temp.getnext()

	def remove(self,val):
	
		self.curnode = self.head
		while self.curnode.next != None:
		 if(self.curnode.value == val):
		  break
		 else:
		  self.curnode = self.curnode.next
		self.curnode.getprev().setnext(self.curnode.getnext()) 
		self.curnode.getnext().setprev(self.curnode.getprev())
		

	def removeafter(self,val):

		self.curnode = self.head
		while self.curnode.next != None:
		 if(self.curnode.value == val):
		  break
		 else:
		  self.curnode = self.curnode.next
		self.remove(self.curnode.getnext().getvalue())

	def removebefore(self,val):

		self.curnode = self.head
		while self.curnode.next != None:
		 if(self.curnode.value == val):
		  break
		 else:
		  self.curnode = self.curnode.next
		self.remove(self.curnode.getprev().getvalue())


	def check(self):
		
		n=self.head
		n=n.next
		print n.next.value
		print n.prev.value
		print n.value



d=dlist()
d.add(1)
d.add(2)
d.add(3)
d.addatfirst(0)
d.addafter(0,9)
d.remove(9)
d.removeafter(1)
d.addbefore(1,10)
d.removebefore(3)
d.check()


	


