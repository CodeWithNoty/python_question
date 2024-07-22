class employe:
    company="noty"
    salary=3000
    salarybonus=2000

    @property
    def total(self):
        return self.salary+self.salarybonus
    
    @total.setter
    def total(self,val):
        self.salary=val-self.salarybonus

    
e=employe()
print(e.total)
e.total=2300
print(e.salary)
print(e.salarybonus)

