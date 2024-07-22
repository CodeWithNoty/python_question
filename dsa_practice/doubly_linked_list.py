class Node:
    def __init__(self,pre=None,item=None,next=None) :
        self.pre=pre
        self.item=item
        self.next=next

class dll:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self,data):
        n=Node(None,data,self.start)
        if not self.is_empty():
            self.start.pre=n
        self.start=n 
     

    def insert_at_last(self,data):
        temp=self.start
        if self.start is not None:
            while temp.next is not  None:
                temp=temp.next
            n=Node(temp,data,None)
            temp.next=n
       
    
    def insert_item(self,temp,data):
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
            print(temp.item,end=' ')
            temp=temp.next
        print()

    def deletion_first(self):
        if self.start is not None:
            self.start=self.start.next
            self.start.pre=None
        
    def deletion_last(self):
      if self.start is None:
        return
      elif self.start.next is None:
        self.start = None
      else:
        temp=self.start
        while temp.next is not None:
            temp=temp.next
        temp.pre.next=None

    
    def deletion_item(self,data):
       temp=self.search(data)
       if temp is None:
        return
       if temp.pre is not  None:
        temp.pre.next=temp.next
       if temp.next is not None:
        temp.next.pre=temp.pre
       if temp==self.start:
        self.start=temp.next

          
mylist=dll()
mylist.insert_at_start(5)
mylist.print_list()

mylist.insert_at_last(15)
mylist.print_list()

mylist.insert_item(mylist.search(5),10)
mylist.print_list()

mylist.deletion_first()
mylist.print_list()

mylist.deletion_last()
mylist.print_list()

mylist.deletion_item(10)
mylist.print_list()