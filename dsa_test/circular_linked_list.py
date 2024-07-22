class Node:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

class cll:
    def __init__(self,last=None):
        self.last=last

    def is_empty(self):
        return self.last is None
    
    def insert_at_first(self,data):
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

    def insert_item(self,temp,data):
       if temp is not None:
           n=Node(data,temp.next)
           temp.next=n
           if temp ==self.last:
               self.last=n

    def search(self,data):
          if  self.is_empty():
            return None
          temp=self.last.next
          while temp!=self.last:
            if temp.item==data:
                return temp
            temp=temp.next
            if temp.item==data:
                return temp
          return None
    
    def print_list(self):
     if not self.is_empty():
      temp=self.last.next
      while temp!=self.last:
         print(temp.item,end=' ')
         temp=temp.next
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
                while temp.next != self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp

    def delete_item(self,data):
            if self.is_empty():
             return
        
        # Case 1: List has only one node
            if self.last.next == self.last and self.last.item == data:
             self.last = None
             return
        
        # Case 2: Delete the first node
            if self.last.next.item == data:
             self.delete_first()
             return

        # Case 3: Delete a node that is not the first or last
            temp = self.last.next
            while temp.next != self.last:
             if temp.next.item == data:
                temp.next = temp.next.next
                return
            temp = temp.next
        
        # Case 4: Delete the last node
            if self.last.item == data:
             self.delete_last()

c=cll()
c.insert_at_first(2)
c.insert_at_last(8)
c.insert_item(c.search(2),4)
c.delete_first()
c.delete_last()
c.delete_item(4)
c.print_list()