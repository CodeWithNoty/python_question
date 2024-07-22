from datetime import date

def cal(birthdate):
   today=date.today()
   today = today.year , today.month, today.day
   before=birthdate.year , birthdate.month, birthdate.day

   age =today-before
   print(age)

print(cal(date(2005,27,1)))
