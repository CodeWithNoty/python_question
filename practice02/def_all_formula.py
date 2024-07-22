class tr():
    def __init__(self,b,h):
        self.b=b
        self.h=h

    def area(self):
        area=1/2*(self.b*self.h)
        print(area)
class cr():
    def __init__(self,r,pi):
        self.r=r
        self.pi=pi

    def area(self):
        area=1/2*(self.pi* self.r *self.r)
        print(area)
class re():
    def __init__(self,b,h):
        self.b=b
        self.h=h

    def area(self):
        area=(self.b*self.h)
        print(area)

obj=tr(10,20)
obj.area()

obj=cr(3.14,10)
obj.area()

obj=re(10,20)
obj.area()