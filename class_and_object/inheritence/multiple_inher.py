class emp:
    company="google"
    ecode=123
    

class pro:
    company="youtube"
    level=0

    def upgrde(self):
        self.level = self.level+1

class child(pro,emp):
    name="rohit"

p=child()

p.upgrde()
print(p.company)