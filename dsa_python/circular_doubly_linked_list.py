class Node:
    def __init__(self, pre=None, item=None, next=None):
        self.pre = pre
        self.item = item
        self.next = next

class cdll:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None

    def insert_at_start(self, data):
        n = Node(item=data)
        if self.is_empty():
            n.next = n 
            n.pre = n
        else:
            n.next = self.start
            n.pre = self.start.pre
            self.start.pre.next = n
            self.start.pre = n
        self.start = n

    def insert_at_last(self, data):
        n = Node(item=data)
        if self.is_empty():
            n.next = n 
            n.pre = n
            self.start = n
        else:
            n.next = self.start
            n.pre = self.start.pre
            self.start.pre.next = n
            self.start.pre = n

    def search(self, data):
        temp = self.start
        if temp is None:
            return None
        if temp.item == data:
            return temp
        temp = temp.next
        while temp != self.start:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_item(self, temp, data):
        if temp is not None:
            n = Node(item=data)
            n.next = temp.next
            n.pre = temp
            temp.next.pre = n
            temp.next = n

    def print_list(self):
        temp = self.start
        if temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
            while temp != self.start:
                print(temp.item, end=' ')
                temp = temp.next
        print()

    def delete_first(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.pre.next=self.start.next
                self.start.next.pre=self.start.pre
                self.start=self.start.next
        
    def delete_last(self):
        if self.start is not None:
            if self.start.next==self.start:
                self.start=None
            else:
                self.start.pre.pre.next=self.start
                self.start.pre=self.start.pre.pre
        
    def delete_item(self,data):
        if self.start is not None:
                temp=self.start
                if temp.item==data:
                    self.delete_first()
                else:
                    temp=temp.next
                    while temp is not self.start:
                        if temp.item==data:
                            temp.next.pre=temp.pre
                            temp.pre.next=temp.next


# Example usage:
mylist = cdll()
mylist.insert_at_start(10)
mylist.insert_at_start(50)
mylist.insert_at_last(20)
mylist.insert_item(mylist.search(10),30)
mylist.delete_first()
mylist.delete_last()
# mylist.delete_item(10)
mylist.print_list()
