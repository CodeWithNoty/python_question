class greate:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c


    @staticmethod
    def large():
        print("greater numerb of three ")
        print("______________________")

        
    def gre(self):
     print(f"1 first numerb :{self.a}")
     print(f"2 secound numerb :{self.b} ")
     print(f"3 third numebr :{self.c} ")

    def gr(self):
        if self.a > self.b & self.a > self.c:
            print(f"{self.a} is greater ")

        elif self.b > self.a & self.b > self.c:
            print(f"{self.b} is greater ")

        else :
            print(f"===>{self.c} is greater ")

obj=greate(6,20,14)
obj.large()
obj.gre()
# print("*\n")
obj.gr()