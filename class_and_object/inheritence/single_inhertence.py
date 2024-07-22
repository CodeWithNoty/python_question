class emp:
    company="google"

    def show(self):
        print("this is employe ")

class pro(emp):
    lan="python "

    def lan(self):
        print(f"the lang.. is {self.lan}")

    def showd(self):                     
        print("this is a programer ")

e=emp()
e.show()

p=pro()
p.showd() 
print(p.company) 
