class Node:
    def __init__(self,item=None,pre=None,next=None):
        self.item=item
        self.pre=pre
        self.next=next

class deque:
    def __init__(self):
        self.front=None
        self.rear=None
        self.item_count=0

    def is_empty(self):
        return self.item_count==0
    
    def insert_front(self,data):
        n=Node(data,None,self.front)
        if self.is_empty():
            self.rear=n
        else:
            self.front.pre=n
        self.front=n
        self.item_count+=1

    def insert_rear(self,data):
        n=Node(data,self.rear,None)
        if self.is_empty():
            self.front=n
        else:
            self.rear.next=n
        self.rear=n
        self.item_count+=1

    def delete_front(self):
        if self.is_empty():
            raise IndexError (" empty")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.front=self.front.next
            self.front.pre=None
        self.item_count-=1

    def delete_rear(self):
        if self.is_empty():
            raise IndexError (" empty ")
        if self.front==self.rear:
            self.front=None
            self.rear=None
        else:
            self.rear=self.rear.pre
            self.rear.next=None
        self.item_count-=1

    def get_front(self):
        if self.is_empty():
            raise IndexError (" empty ")
        return self.front.item
    def get_rear(self):
        if self.is_empty():
            raise IndexError (" empty ")
        return self.rear.item
    
    def size(self):
        return self.item_count
    
d1=deque()
d1.insert_front(2)
d1.insert_front(1)
d1.insert_rear(3)
d1.insert_rear(4)
print(d1.get_front(),d1.get_rear())



            
