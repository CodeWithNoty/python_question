class Node:
    def __init__(self, item=None ,  next=None):
        self.item=item
        self.next=next

class ssl:
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

    # def search(self,data):
    #     temp=self.start
    #     while temp.next is not None:
    #         if temp.item==data:
    #             return temp
    #         temp=temp.next
    #     return None
    
    def insert_after(self,temp, data):
        if temp is not None:
            n=Node(data , temp.next)
            temp.next=n

    def print(self):
        temp=self.start
        while temp is not  None:
            print(temp.item,end=' ')
            temp=temp.next

    def delete(self):
        if self.start is not None:
            self.start = self.start.next
    
    def delete_last(self):
        if self.start is None:
            return
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None 



mylist=ssl()
mylist.insert_at_start(0)
# mylist.insert_at_start(50)
# mylist.insert_at_start(40)
# mylist.insert_at_start(30)
# mylist.insert_at_start(20)
# mylist.insert_at_start(10)

mylist.print()
print()



mylist.insert_after(mylist.start, 15)
mylist.print()
print()

mylist.delete_last()
mylist.print()
print()
# mylist.search(10)
# mylist.print()
# print()