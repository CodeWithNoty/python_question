class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class sll:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start is  None
    
    def insert_at_first(self,data):
        n=Node(data,self.start)
        self.start=n
        
    def insert_at_last(self,data):
        if self.is_empty():
            self.start=None
        else:
            temp=self.start
            n=Node(data,None)
            while temp.next is not None:
                n=temp.next
            temp.next=n

    def search(self,data):
        temp=self.start
        while temp is not None:
         if temp.item==data:
            return temp
         temp=temp.next
        return None

                
    def insert_item(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n

    def deletion_first(self):
        if  self.start is not None:
         self.start=self.start.next
        
    def deletion_last(self):
        if self.start is  None:
            return
        elif self.start.next is  None:
            self.start=None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

    def delete_item(self,temp):
        if temp is  None and temp.next.next is None:
            temp.next=temp.next.next
            
    def print(self):
        temp=self.start
        while temp  is not None:
                print(temp.item,end=' ')
                temp=temp.next

mylist=sll()
mylist.insert_at_first(10)
mylist.insert_at_last(20)
mylist.insert_item(mylist.search(10),15)
mylist.print()
print()


mylist.deletion_first()
mylist.deletion_last()
mylist.delete_item(mylist.search(15))
mylist.print()