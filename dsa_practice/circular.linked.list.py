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
        if  self.is_empty():
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

    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n

    def search(self,data):
        if self.is_empty():
            return None
        temp = self.last.next
        while True:
            if temp.item == data:
                return temp
            temp = temp.next
            if temp == self.last.next:
                break
        return None
    
    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while True:
                print(temp.item, end=' ')
                temp = temp.next
                if temp == self.last.next:
                    break
            print()

c1=cll()
c1.insert_at_start(3)
c1.insert_after(c1.search(3),6)
c1.insert_at_last(9)
c1.print_list()


            


