from snode import *
class slist():
	
	def __init__(self):

		 self.size = 0
		 self.head = node()
		 self.curnode = node()

	def add(self,item):

		 if(self.isempty() == True):
		  self.head = node(item)
		  self.size += 1
		 else:	  
		  self.curnode = self.head
		  while (self.curnode.next != None):
		   self.curnode = self.curnode.getnext()	  
		  self.curnode.next=node(item)
		  self.size += 1
	
	def addatfirst(self,val):

		 if(self.isempty() == True):
		  self.head = node(val)
		  self.size += 1
		 else:
		  temp = self.head
		  temp1 = node(val)
		  self.head = temp1
		  temp1.setnext(temp)
		  self.size += 1

	def addafter(self,val,item):

		 n = node(item)
		 cur = self.head
		 while cur.getnext() != None:
		  if (cur.getvalue() == val):
		   break
		  else:
		   pre = cur
		   cur = cur.getnext()
		 temp1 = cur.getnext()
		 cur.setnext(n)
		 n.setnext(temp1)
		 self.size += 1
		
	def addatlast(self,val):

		 last = self.head
		 for i in range(self.size-1):
		  last = last.getnext()
		 temp = node(val)
		 last.setnext(temp)
		 self.size += 1
		 
	def isempty(self):

		 if(self.size == 0):
		  return True
		 else:
		  return False
	
	def printlist(self):

		 temp = self.head
		 for i in range(self.size):
		  print temp.getvalue()
		  temp = temp.getnext()
	
	def remove(self,val):

		 temp=node()
		 temp = self.head
		 while (temp.getvalue() != val):
		  pre=temp
		  temp = temp.getnext() 	 
		 if (val == self.head.getvalue()):
		  self.head = self.head.getnext()
		 else:
		  pre.setnext(temp.getnext())
		 self.size -= 1 

	def removeatlast(self):

		last = self.head
	 	for i in range(self.size-1):
		 last = last.getnext()
		last.setnext(node())
		self.size -= 1

	def removeatfirst(self):
	
		self.head = self.head.getnext()
		self.size -= 1

	def removeafter(self,val):
		
		self.cur = self.head
		while self.cur.getnext() != None:
		 if (self.cur.getvalue() == val):
	  	  break
		 else:
		  pre = self.cur
		  self.cur = self.cur.getnext()
		 self.cur = self.cur.next.getnext()
		 self.size -= 1
	
	def length(self):
	
		print "Size = ",self.size
	
	def rettop(self):
		
		print "Top most value = ",(self.head.value)
	
e=slist()
e.add(1)
e.add(2)
e.add(3)
e.add(4)
e.addatfirst(6)
e.addatlast(10)
e.removeatlast()
e.printlist()
print "\n"
e.remove(1)
e.addafter(2,5)
e.printlist()
print "\n"
e.removeatfirst()
#e.removeafter(3)
print "\n"
e.printlist()
