class Node:
    def __init__(self,pre=None,item=None,next=None):
        self.pre=pre
        self.item=item
        self.next=next

class dll:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start is None
    
    def insert_at_first(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.pre=n
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

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_item(self,temp,data):
        if  temp is not None:
            n=Node(temp,data,temp.next)
            if temp.next is not None:
                temp.next.pre=n
            temp.next=n

    def delete_first(self):
        if self.start is not  None:
            self.start=self.start.next
            if self.start is not None:
             self.start.pre=None
    
    def delete_last(self):
        if  self.start is  None:
            pass
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.pre.next=None

    def delete_item(self,data):
        if self.start is None:
            return
        temp = self.start
        while temp is not None:
            if temp.item == data:
                if temp.pre is not None:
                    temp.pre.next = temp.next
                if temp.next is not None:
                    temp.next.pre = temp.pre
                if temp == self.start:  # Deleting the start node
                    self.start = temp.next
                return
            temp = temp.next

                

    def print(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
        print()

mylist=dll()
mylist.insert_at_first(20)
mylist.print()
mylist.insert_at_last(40)
mylist.print()
mylist.insert_at_last(80)
mylist.print()
mylist.insert_item(mylist.search(40),60)
mylist.print()
mylist.delete_first()
mylist.print()
mylist.delete_last()
mylist.print()
mylist.delete_item(40)
mylist.print()



