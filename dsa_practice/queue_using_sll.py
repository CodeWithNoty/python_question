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
        return self.front is None

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
            raise IndexError("empty")
        elif self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
        self.item_count-=1


    def getfront(self):
        if self.is_empty():
           raise IndexError ("stack is empty")
        else:
            return self.front.item
    
    def getrear(self):
        if self.is_empty():
           raise IndexError ("stack is empty")
        else:
            return self.rear.item
        
    def size(self):
        return self.item_count
    
q=queue()
q.enqueue(2)
q.enqueue(4)
q.enqueue(6)
q.enqueue(8)
q.enqueue(12)
print("front",q.getfront())
print("rear",q.getrear())

        

    
