class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class sll:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start is None
    
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


    def insert_after(self,temp,data):
        n=Node(data,temp.next)
        if temp is not None:
            temp.next=n     

    def search(self,data):
        temp=self.start
        while temp is not None:
         if temp.item==data:
             return temp
        return None

    def print(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next
        print()

    def delete_first(self):
        if  self.start  is not None:
            self.start=self.start.next

    def delete_last(self):
        if self.start is None:
            return
        if self.start.next is None:
            self.start = None
        else:
            temp=self.start
            while temp.next.next is not None:
                temp=temp.next
            temp.next=None
        

    def delete_after(self, temp):
        if temp is not None and temp.next is not None:
            temp.next = temp.next.next

        

s=sll()
s.insert_at_start(3)
s.insert_at_last(9)
s.insert_after(s.search(3),6)
s.delete_first()
s.delete_last()
s.delete_after(s.search(3))
s.print()




