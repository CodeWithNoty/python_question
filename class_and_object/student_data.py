class student:
    def __init__(self,idno, name, age, city ):
        self.name=name
        self.idno=idno
        self.age=age
        self.city=city

    def get(self):
        print(f" idno no of student :{self.idno}")
        print(f" name no of student :{self.name}")
        print(f" age no of student :{self.age}")
        print(f"enter city no of student :{self.city}")

    @staticmethod
    def take():
        print("thanks to you visit my profile")
        

obj=student("2345","noty",18,"chandigarh")
obj.take()
print("_________")
obj.get()
print("\n")

obj=student("2245","neeraj",19,"goa")
obj.take()
print("_________")
obj.get()