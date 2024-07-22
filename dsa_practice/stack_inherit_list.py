from typing import SupportsIndex


class stack(list):
    def __init__(self):
        self.item=[]
        self.item_count=0

    def is_empty(self):
        return len(self.item)==0
    
    
    def push(self,data):
        self.item.append(data)
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError ("stack is empty")
        
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("stack is empty")
        
    def size(self):
        return self.item_count

s=stack()
s.push(3)
s.push( 6)
s.push(9)
print("top " , s.peek())
print("remove ", s.pop())
print("top " , s.peek())
print("remove ", s.pop())
print("top " , s.peek())
print("remove ", s.pop())
try:
    print("top " , s.peek())
except IndexError as e:
    print("stack is fully empty")
