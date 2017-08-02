class dnode:

    def __init__(self,val=None):
        self.value = val
        self.next = None
	self.prev = None

    def getprevalue(self):
        return self.prev.value

    def getnextvalue(self):
	return self.next.value

    def getvalue(self):
	return self.value

    def getnext(self):
        return self.next

    def getprev(self):
	return self.prev	

    def setdata(self,data):
        self.data = data

    def setnext(self,next):
        self.next = next

    def setprev(self,prev):
	self.prev = prev

	

