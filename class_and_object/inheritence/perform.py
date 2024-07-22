class car:

    @staticmethod
    def what():
        print("=> what a function of tier in car")
        print("________________________________")

    def __init__(self,type,extra,price):
        self.type=type
        self.extra=extra
        self.price=price

    def fun(self):
        print(f"=> how many  of tier in car :{self.type}")
        print(f"=> how many extra  tier in car :{self.extra}")

    def pr(self):
        print(f"=> price of the 1 tier in car motar :{self.price}")
        sum=400*4
        print("=> four tier price :",sum)

class ger(car):
    

    @staticmethod
    def what():
        print("function of gier in car ")
        print("____________________________")
    def __init__(self,first,sec,third,fourth,fifth):
        self.first=first
        self.sec=sec
        self.third=third
        self.fourth=fourth
        self.fifth=fifth

    def fun(self):
        print(f"=> 1 ger in car speed : {self.first}")
        a=int(input("enter a numebr :"))
        if a <= self.first:
            print(" good drive , slow ")
        else:
            print(f'''if you drive more fast |{self.first}| speed than \naap abhi sikh rhe hai to aram se chalo\n''')
            print("_________________________________")
            
        print(f"=> 2 ger in car speed : {self.sec}")
        b=int(input("enter a numebr :"))
        if b <= self.sec:
            print("nice drive ")
        else:
            print(f" aaj apka 2 mahina hai \n to aaj app {self.sec} ki speed m chalao\n")
            print("__________________________")

        print(f"=> 3 ger in car speed : {self.third}")
        c=int(input("enter a numebr :"))
        if c <= self.third:
         print(" you drive not slow not fast") 
        else:
            print(f"abhi app {self.third} ki speed m hi chalao nhi to lene ke dene pad jenge\n")
            print("__________________________")

        print(f"=> 4 ger in car speed : {self.fourth}")
        d=int(input("enter a numebr :"))
        if d <= self.fourth:
            print(" you drive fast ")
        else:
            print("ab aap thoda sikh gye hai dekh ke chalana\n")
            print("__________________________")

        print(f"=> 5 ger in car speed : {self.fifth}")
        e=int(input("enter a numebr :"))
        if e <= self.fifth:
            print(" you drive very fast ")
        else:
            print(f"{self.fifth} {self.fourth} ki speed m hi chalana")
        
c=car(4,1,400)
c.what()
c.fun()
c.pr()
print("\n")

g=ger(40,60,120,300,400)
g.what()
g.fun()

# o=control("noty","neeraj", "dheeraj","kanchan", 350)
# o.con("noty")