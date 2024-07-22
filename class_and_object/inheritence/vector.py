class c2vector:
    def __init__ (self,i,j):
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class c3vector(c2vector):
    def __init__ (self,i,j,k):
        super().__init__(i,j)
        self.kcap=k
     
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"
    
c=c2vector(1,8)
d=c3vector(1,3,7)
print(c)
print(d)

