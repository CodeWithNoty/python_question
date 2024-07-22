class details:
    company="microsoft"
    def __init__(self,name,age,company):
        self.name=name
        self.age=age
        self.company=company
        print("progrramer details ")

    def jan(self):
        print(f"the name of employe :{self.name} ")
        print(f"the age of employe :{self.age} ")
        print(f"which company  of employe working :{self.company} ")

noty=details("neeraj ", 18, "google")

noty.jan()