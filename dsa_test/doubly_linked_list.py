class Node:
    def __init__(self,pre=None,item=None,next=None):
        self.pre=pre
        self.item=item
        self.next=next

class dll:
    def __init__(self,start=None):
        self.start= start

    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
         self.start.pre=n
        self.start=n

    def insert_at_last(self,data):
        n=Node(None,data,None)
        if self.is_empty():
            self.start=n
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
            n.pre=temp

    def insert_after(self,temp,data):
        if temp is not None:
         n=Node(temp,data,temp.next)
         if temp.next is not None:
            temp.next.pre=n
        temp.next=n

    def search(self,data):
       temp=self.start
       while temp is not None:
        if temp.item==data:
           return temp
        temp=temp.next

    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end='')
            temp=temp.next
        print()

    def delete_start(self):
       if self.start is not  None:
           self.start=self.start.next
           self.start.pre=None

    def delete_last(self):
        if self.start is  None:
            return
        elif self.start.next is  None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.pre.next=None

    def delete_after(self,data):
     temp=self.search(data)
     if temp is None:
        return
     if temp.pre is not  None:
        temp.pre.next=temp.next
     if temp.next is not None:
        temp.next.pre=temp.pre
     if temp==self.start:
        self.start=temp.next

d=dll()
d.insert_at_start(3)
d.insert_at_last(9)
d.insert_after(d.search(3),6)
d.delete_start()
d.delete_last()
d.delete_after(d.search(3))
d.print_list()
           


