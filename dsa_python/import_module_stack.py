from singly_linked_list import *
class stack:
    def __init__(self):
        self.mylist=sll()
        self.item_count=0

    def is_empty(self):
       return self.mylist.is_empty()
    
    
    def push(self,data):
        self.mylist.insert_at_start(data)
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
         self.mylist.delete()
         self.item_count-=1

    def peek(self):
       if not self.is_empty():
          return self.mylist.start.item
       
    def size(self):
       return self.item_count
    
s1=stack()
s1.push(2)
s1.push(4)
s1.push(8)
print("top element is ", s1.peek())
s1.pop()
print("top element is ", s1.peek())
s1.pop()
print("top element is ", s1.peek())
s1.pop()
print("top element is ", s1.peek())
print()