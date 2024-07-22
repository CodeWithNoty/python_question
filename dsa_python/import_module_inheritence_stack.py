from singly_linked_list import *

class stack(sll):

    def __init__(self):
       super().__init__()
       self.item_count=0
    def is_empty(self):
        return super().is_empty()
    
    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
         self.delete()
         self.item_count-=1
        else:
           raise IndexError ("stack is empty")

    def peek(self):
       if not self.is_empty():
          return self.start.item
       else:
          raise IndexError ("stack is empty")
       

    def size(self):
       return self.item_count
    
    
s1=stack()
s1.push(2)
s1.push(4)
s1.push(6)
print("top element ",s1.peek())
