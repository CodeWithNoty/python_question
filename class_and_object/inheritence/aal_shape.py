class triangle:
 
 @staticmethod
 def inf():
    print("triangle formula ")
    print("---------------------")
 def tri(self,b,h):
  area =1/2*(b*h)
  print("area of triangle :",area)
  
 def perimeter(self,a,b,c):
    peri=a*b*c
    print("perimeter of triangle :",peri)
    
        

class rectangle:
 @staticmethod
 def inf():
    print("rectangle formula ")
    print("---------------------")
 def rec(self,l,b):
        area=l*b
        per=2*l*b
        print("area of rectangel :" , area)
        print("perimeter of rectangel :" , per)
        



t=triangle()
t.inf()
t.tri(2,3)
t.perimeter(2,3,4)
print("\n")

r=rectangle()
r.inf()
r.rec(2,3)
