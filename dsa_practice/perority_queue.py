class pq:
    def __init__(self):
        self.item=[]
    def is_empty(self):
        return len(self.item)==0
    def push(self,data,p):
        idx=0
        while idx < len(self.item) and self.item[idx][1]<p:
            idx+=1
        self.item.insert(idx,(data,p))

    def pop(self):
        if self.is_empty():
            raise IndexError("queue is empty ")
        return self.item.pop(0)[0]
    def size(self):
        return len(self.item)
p = pq()
p.push("neeraj", 6)
p.push("noty", 4)
p.push("nishi", 3)
p.push("parnidhi", 7)
p.push("nawab", 1)
p.push("lamen", 0)

while not p.is_empty():
    print(p.pop())
