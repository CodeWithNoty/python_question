class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class sll:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start is  None
    
    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n

    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
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

    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            
    def delete_last(self):
        
        if self.start is  None:
            return 
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None

            

    def print(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
        print()

mylist=sll()
mylist.insert_at_start(2)
mylist.print()
mylist.insert_at_start(5)
mylist.print()
mylist.delete_first()
mylist.print()
mylist.insert_at_last(8)
mylist.print()

node=mylist.search(2)
mylist.insert_item(node,4)
mylist.print()


mylist.delete_last()
mylist.print()