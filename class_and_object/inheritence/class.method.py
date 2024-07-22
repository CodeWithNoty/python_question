class emp:
    @staticmethod
    def before():
        print("before change ")
    name="noty"
    age=13
    salary=123

    @staticmethod
    def after():
        print("after change ")

    @classmethod
    def change(cls,nm):
        cls.name=nm

    @classmethod
    def changer(cls,ag):
        cls.age=ag

    @classmethod
    def changes(cls,sl):
        cls.salary=sl


e=emp()
e.before()
print(e.name)
print(e.age)
print(e.salary)
print("\n")

e.after()
e.change("neeraj")
e.changer(24)
e.changes(1200)
print(e.name)
print(e.age)
print(e.salary)
