class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class queue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.front==None
    
    def enqueue(self,data):
        n=Node(data)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1


    def dequeue(self):
        if self.is_empty():
            raise IndexError("empty queue")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.item_count-=1
        
    def getfront(self):
        if self.is_empty():
            raise IndexError ("No data in queue")
        else:
            return self.front.item
        

    def getrear(self):
        if self.is_empty():
            raise IndexError ("No data in queue")
        else:
            return self.rear.item
        
    def size(self):
        return self.item_count
    
q1=queue()
q1.enqueue(2)
q1.enqueue(4)
q1.enqueue(6)
q1.enqueue(8)
print("front",q1.getfront(),"|rear",q1.getrear())
q1.dequeue()
q1.enqueue(10)
print("front",q1.getfront(),"|rear",q1.getrear())
q1.dequeue()
print("front",q1.getfront(),"|rear",q1.getrear())
q1.dequeue()
print("front",q1.getfront(),"|rear",q1.getrear())
q1.dequeue()
q1.enqueue(12)
print("front",q1.getfront(),"|rear",q1.getrear())
q1.dequeue()
q1.dequeue()
try:
    print("front",q1.getfront())
except IndexError as e:
    print(e)