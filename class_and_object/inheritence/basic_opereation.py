class basic:
 def __init__(self,a,b):
    self.a=a
    self.b=b
        
class add(basic):
 def get(self):
    sum=self.a+self.b
    print(f"the sum is {self.a} and {self.b}:",sum)
    # print(sum)

 def sub(self):
    sub=self.a-self.b
    print(f"the subtraction is {self.a} and {self.b}:",sub)

 def mul(self):
  mul=self.a*self.b
  print(f"the multiplation is {self.a} and {self.b}:",mul)

b=add(4,3)
b.get()
print("\n")
b.sub()
print("\n")
b.mul()
        