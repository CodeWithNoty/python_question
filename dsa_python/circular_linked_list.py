class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class cll:
    def __init__(self,last=None):
        self.last=last

    def is_empty(self):
        return self.last is  None
    
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
        return None
    
    def insert_after(self,temp,data):
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

    def delete_first(self):
        if not self.is_empty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next
        
    def delete_last(self):
        if not self.is_empty():
                if self.last.next==self.last:
                 self.last=None
                else:
                    temp=self.last.next
                    while temp.next!=self.last:
                        temp=temp.next
                    temp.next=self.last.next
                    self.last=temp
                    
    def delete(self,data):
        if not self.is_empty():
            if self.last.next == self.last:
                if self.last.item == data:
                    self.last = None
            else:
                if self.last.next.item == data:
                    self.delete_first()
                else:
                    temp = self.last.next
                    while temp.next != self.last:
                        if temp.next.item == data:
                            temp.next = temp.next.next
                            return
                        temp = temp.next
                    if self.last.item == data:
                        self.delete_last()
            
mylist=cll()

mylist.insert_at_start(10)
mylist.insert_at_start(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(20),60)
mylist.print()

mylist.delete_first()
mylist.delete_last()
mylist.delete(10)

mylist.print()          