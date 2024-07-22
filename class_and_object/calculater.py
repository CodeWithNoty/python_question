class calculater:

    def __init__(self,num):
          self.numebr=num

    @staticmethod
    def greet():
        print("the all formula here \n")

    def squre(self):
        print(f"the squre  of {self.numebr} is {self.numebr**2}")

    def cube(self):
        print(f"the cube of {self.numebr} is {self.numebr**3}")

    def squreroot(self):
        print(f"the squre root of {self.numebr} is {self.numebr**4}")
            
            
noty=calculater(4)
noty.greet()
noty.squre()
noty.cube()
noty.squreroot()