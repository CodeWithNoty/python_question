class emp:
    compny="youtube"
    def getsalry(self):
        print(f"salaaray of this emp working in {self.compny} is {self.salary}")

    @staticmethod
    def greet():
        print("good morning ")

noty=emp()
noty.salary=100000
noty.getsalry() #emp.getsalary(noty)
noty.greet()