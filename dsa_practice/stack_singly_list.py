class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class stack:
    def __init__(self,start=None):
        self.item=[]
        self.start=start
        self.item_count=0

    def is_empty(self):
        return self.start is None
    
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.item_count+=1

    def pop(self):
        if not self.is_empty():
            data=self.start.item
            self.start=self.start.next
            self.item_count-=1
            return data
        else:
            raise IndexError ("stack is empty ")
        
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            self.is_empty()

    def size(self):
        return self.item_count

s=stack()
s.push(2)
s.push(4)
s.push(8)
print("top " , s.peek())
print("remove " , s.pop())
print("top " , s.peek())
print("remove " , s.pop())
print("top " , s.peek())
print("remove " , s.pop())
print("top " , s.peek())

