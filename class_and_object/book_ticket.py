class railway:

    def __init__(self,name,seats,fare):
        self.name=name
        self.fare=fare
        self.seats=seats

    def getstatus(self):
        print(f"the name of the railway :{self.name} ")
        print(f"total seats in available :{self.seats} ")
        print("*************")
        
    def getfare(self):
        print(f"the price of the ticket is :{self.fare}")

    def book(self):
        if (self.seats>2):
            print(f"your ticket is booked thanks your sets number is {self.seats}")
            self.seats- self.seats-1
        else:
            print("your ticket is no booked ")

obj=railway("india express 420",90,2)
obj.getstatus()
# obj.getfare()
obj.book()
obj.getstatus()
