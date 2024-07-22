class stack:
    def __init__(self):
        self.item=[]

    def is_empty(self):
        return len(self.item)==0
    
    def push(self,data):
        self.item.append(data)

    def pop(self):
        if not  self.is_empty():
            return self.item.pop()
        else:
            raise IndexError("stack is empty") 
        
    def peek(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("stack is empty")
        
    def size(self):
        return len(self.item)
    
mylist=stack()
mylist.push(2)
mylist.push(4)
mylist.push(8)
print("top element is ",mylist.peek())
print("removed element is ",mylist.pop())
print("top element is ",mylist.peek())
print()
