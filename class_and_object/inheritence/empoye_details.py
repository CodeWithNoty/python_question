class basic:
    name="noty"
    age=19
    city="chandigarh"

    @staticmethod
    def bas():
       print("your basic information")
       print("*********************************")

    def ba(self):
       
       print(f"name : {self.name}")
       print(f"age: {self.age}")
       print(f"city : {self.city}")

class study(basic):
   classs="bca3"
   qaulification="programmer"
   parttime="job"
   place="mohali..gjimt"

   @staticmethod
   def stu():
       print("your study information")
       print("*********************************")

   def st(self):
      print(f"class : {self.classs}")
      print(f"qulification : {self.qaulification}")
      print(f"work : {self.parttime}")
      print(f"place : {self.place}")
      

class family(study,basic):
   member1= "father"
   member2= "mother"
   member3= "brother"
   member4= "sister"

   @staticmethod
   def fam():
       print("your family information")
       print("*********************************")

   def fa(self):
      print(f"1 : {self.member1}")
      print(f"2 : {self.member2}")
      print(f"3 : {self.member3}")
      print(f"4 : {self.member4}")

b=basic()
b.bas()
b.ba()
print("\n")

s=study()
s.stu()
s.st()
print("\n")

f=family()
f.fam()
f.fa()