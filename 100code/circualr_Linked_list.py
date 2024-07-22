class Node:
    def __init__(self,item=None,next=None):
      
        self.item=item
        self.next=next

class cll:
    def __init__(self,last=None):
        self.last=last
    
    def is_empty(self):
        return self.last is None
    
    def insert_at_start(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
        
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n
            
        
    def search(self,data):
        if self.is_empty():
            return None
        temp=self.last.next
        while temp !=self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
    
    def insert_item(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n
        
    def print(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item, end=' ')
                temp = temp.next
            print(temp.item)

    def delete_at_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
             self.last=None
            else:
             self.last.next=self.last.next.next

    def delete_at_last(self):
        if not self.is_empty():
            if self.last.next==self.last:
             self.last=None
            else:
                temp=self.last
                while temp.next!=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp
        pass
    def delete_item():
        pass

mylist=cll()
mylist.insert_at_start(10)
mylist.print()
mylist.insert_at_last(30)
mylist.print()
mylist.insert_item(mylist.search(10),20)
mylist.print()
mylist.delete_at_first()
mylist.print()
mylist.delete_at_last()
mylist.print()
