class Area:
    def __init__ (self,pi,r):
        self.pi=pi
        self.r=r


    def get(self):
        print(f"=>the value of pi : {self.pi}")
        print(f"=>the value of radius : {self.r}")

    def con(self):
        self.area=self.pi * self.r
        print(f"=>:the area of circle : {self.area}\n")

class perimeter(Area):
    def con(self):
        self.per=self.pi * self.r * self.r
        print(f"=> the perimeter of circle {self.per}")

c=Area(22/7,23)
c.get()
c.con()

p=perimeter(22/7, 2)
p.con()