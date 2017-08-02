class node():
	
	def __init__(self,val=None):
	 self.value = val
	 self.next=None

	def setnext(self,n):
	 self.next = n
	 
	def setvalue(self,val):
	 self.value = val
	
	def getvalue(self):
	 return self.value
	
	def getnext(self):
	 return self.next
	 
