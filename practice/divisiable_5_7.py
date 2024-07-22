num1=int(input("enter a numeber"))
num2=int(input("enter a numeber"))
num3=int(input("enter a numeber"))
num4=int(input("enter a numeber"))

if(num1 > num4):
    f1=num1

else:
    f1=num4
if(num2 > num3):
    f2=num2

else:
    f2=num3

if(f1>f2):
    print(f1,"grater")

else:
    print(f2,"greater")