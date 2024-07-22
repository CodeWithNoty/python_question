class deque:
    def __init__(self):
        self.item=[]

    def is_empty(self):
       return len(self.item)==0
    
    def insert_front(self,data):
        self.item.insert(0,data)

    def insert_rear(self,data):
        self.item.append(data)

    def delete_front(self):
        if self.is_empty():
           raise IndexError ("deque is empty")
        else:
         self.item.pop(0)

    def delete_rear(self):
        if self.is_empty():
           raise IndexError ("deque is empty")
        else:
         self.item.pop(0)

    def get_front(self):
        if self.is_empty():
           raise IndexError ("deque is empty")
        else:
         return self.item[0]
        
    def get_rear(self):
        if self.is_empty():
           raise IndexError ("deque is empty")
        else:
         return self.item[-1]
        
    def size(self):
       return len(self.item)
       
q1=deque()
q1.insert_front(4)
q1.insert_front(2)
q1.insert_rear(6)
q1.insert_rear(8)
print(q1.get_front(),q1.get_rear())
print(q1.delete_front())
