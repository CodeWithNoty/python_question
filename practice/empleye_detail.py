class employe:
    def __init__ (self,name,age,idcard,city):
        self.name=name
        self.age=age
        self.idcard=idcard
        self.city=city

    def get(self):
        print(f"the name of worker : {self.name}\n")
        print(f"the age of worker : {self.age}\n")
        print(f"the idcard of worker : {self.idcard}\n")
        print(f"the city of worker : {self.city}\n")

class sal:
    def __init__ (self,number):
     self.number=number

    def get(self):
       print(f"the salary of the woerker : {self.number}\n")

    def con(self):
       self.result=self.number + 18000
       print(f"the increament of salary after 6 month : {self.result}")

e=employe("neeraj" , 19 ,2211628, "chandigharh ")
e.get()
s=sal(10000)
s.get()
s.con()
    


        