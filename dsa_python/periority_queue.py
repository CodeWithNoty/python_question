class pq:
    def __init__(self):
        self.item = []

    def push(self, data, p):
        index = 0
        # Loop to find the correct position to insert the new element
        while index < len(self.item) and self.item[index][1] > p:
            index += 1
        self.item.insert(index, (data, p))

    def is_empty(self):
        return len(self.item) == 0

    def pop(self):
        if self.is_empty():
            raise IndexError("empty")
        return self.item.pop(0)[0]
    
    def size(self):
        return len(self.item)

# Example usage
p = pq()
p.push("neeraj", 6)
p.push("noty", 4)
p.push("nishi", 3)
p.push("parnidhi", 7)
p.push("nawab", 1)
p.push("lamen", 0)

while not p.is_empty():
    print(p.pop())
