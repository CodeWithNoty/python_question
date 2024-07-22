class queue:
    def __init__(self):
        self.item=[]

    def is_empty(self):
        return len(self.item)==0
    
    def enqueue(self,data):
        self.item.append(data)

    def dequeue(self):
        if not self.is_empty():
            self.item.pop(0)
        else:
            raise IndexError ("empty")
        
    def getfront(self):
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError ("Empty")
        
    def getrear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError ("Empty")
        
    def size(self):
        return self.item
        
q=queue()
q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
q.enqueue(8)
q.dequeue()
q.dequeue()
q.dequeue()
print("front ",q.getfront(),"rear",q.getrear())

        