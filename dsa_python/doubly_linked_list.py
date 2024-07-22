class Node:
    def __init__(self, pre=None, item=None, next=None):
        self.pre = pre
        self.item = item
        self.next = next

class dll:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None
    
    def insert_at_start(self, data):
        n = Node(None, data, self.start)
        if not self.is_empty():
            self.start.pre = n
        self.start = n

    def insert_at_last(self, data):
        temp = self.start
        if self.start is not None:
            while temp.next is not None:
                temp = temp.next
            n = Node(temp, data, None)
            temp.next = n
        # else:
        #     self.start = Node(None, data, None)

    def search(self, data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next
        return None
    
    def insert_after(self, temp, data):
        if temp is not None:
            n = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.pre = n
            temp.next = n

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item, end=' ')
            temp = temp.next
        print()

    def delete_start(self):
        if self.start is not None:
            self.start = self.start.next
            if self.start is not None:
                self.start.pre = None

    def delete_last(self):
        if self.start is None:
            pass
        # elif self.start.next is None:
        #     self.start = None
        else:
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.pre.next = None

    def delete(self, data):
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

# Example usage of the dll class
dll_obj = dll()
dll_obj.insert_at_start(10)
dll_obj.insert_at_start(20)
dll_obj.insert_at_last(30)
dll_obj.insert_at_last(40)

print("List after insertions:")
dll_obj.print_list()

dll_obj.delete_start()
print("List after deleting the start:")
dll_obj.print_list()

dll_obj.delete_last()
print("List after deleting the last:")
dll_obj.print_list()

dll_obj.insert_after(dll_obj.search(10), 25)
print("List after inserting 25 after 10:")
dll_obj.print_list()

dll_obj.delete(25)
print("List after deleting 25:")
dll_obj.print_list()
