class emp:
    compny="youtube"

    def  __init__ (self,name,salary,subunit):
     self.name= name
     self.salary= salary
     self.subunit= subunit
    print("employe is created \n")

    def getdetales(self):
       print(f"the name of  empoloye :{self.name}\n")
       print(f"the salry of  empoloye :{self.salary}\n")
       print(f"the subunit of  empoloye :{self.subunit}\n")

    def getsalry(self):
        print(f"salaaray of this emp working in {self.compny} is {self.salary}")

   
    @staticmethod
    def greet():
        print("good morning ")

noty=emp("harry",100,"youtube")
# noty.salary=100000
# noty.getsalry() #emp.getsalary(noty)
# noty.greet()
noty.getdetales()