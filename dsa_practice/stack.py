class stack:
    def __init__(self):
        self.item=[]
        self.item_count=0

    def is_empty(self):
        return len(self.item)==0
    
    def push(self,data):
        self.item.append(data)

    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            raise IndexError ("stack is empty ")
        
    def peek(self):
        if not self.is_empty():
          return self.item[-1]
        else:
            raise IndexError("stack is empty ")
        
    def size(self):
     return self.item_count

s=stack()
s.push(4)   
s.push(8)   
s.push(12)   
print("top ", s.peek())
print("remove", s.pop())
print("top ", s.peek())
print("remove", s.pop())
print("top ", s.peek())

      