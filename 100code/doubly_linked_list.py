class Node:
    def __init__(self,prev=None,item=None, next=None ):
        self.prev=prev
        self.item=item
        self.next=next

class dll:

    def __init__(self,start=None):
        self.start = start

    def is_empty(self):
        return self.start is  None

    def insert_at_first(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.prev=n
        self.start=n

    def insert_at_last(self,data):
        temp=self.start
        if self.start is not None:
            while temp.next is not None:
                temp=temp.next
            n=Node(temp,data,None)
            temp.next=n
        else:
            self.start=Node(None,data,None)

    def insert_middle(self,temp,data):
        if temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.pre=n
            temp.next=n

    def delete_at_first(self):
        if self.start is not  None:
            self.start=self.start.next
            if self.start is not None:
                self.start.pre=None

    def delete_at_last(self):
        if self.start is  None:
            pass
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None

    def print(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
        print()

mylist=dll()
mylist.insert_at_first(5)
mylist.print()

mylist.insert_at_last(15)
mylist.print()
mylist.insert_at_last(20)
mylist.print()

mylist.insert_middle(mylist.start,10)
mylist.print()

mylist.delete_at_first()
mylist.print()

mylist.delete_at_last()
mylist.print()
