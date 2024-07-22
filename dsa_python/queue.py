class queue:
    def __init__(self):
        self.item=[]
        # self.front=None
        # self.rear=None
        
    def is_empty(self):
        return len(self.item)==0

    def enqueue(self,data):
        self.item.append(data)

    def dequeue(self):
         if not self.is_empty():
          self.item.pop(0)
         else:
            IndexError("queue is underflow")

    def getfront(self):
        if not self.is_empty():
         return self.item[0]
        else:
            IndexError("queue is underflow")

    def getrear(self):
        if not self.is_empty():
         return self.item[-1]
        else:
            IndexError("queue is underflow")

    def size(self):
       return len(self.item)
        
q1=queue()
q1.enqueue(2)
q1.enqueue(4)
q1.enqueue(6)
q1.enqueue(8)

print("size of element ",q1.size())
print("2 4 6 8 ")
print("front",q1.getfront())
print("rear",q1.getrear())
q1.dequeue()
print("-------------------")

print("front",q1.getfront())
print("rear",q1.getrear())
q1.dequeue()
print("-------------------")

print("front",q1.getfront())
print("rear",q1.getrear())
q1.dequeue()
print("-------------------")

print("front",q1.getfront())
print("rear",q1.getrear())
q1.dequeue()
print("-------------------")

print("front",q1.getfront())
print("rear",q1.getrear())
q1.dequeue()
print("-------------------")
