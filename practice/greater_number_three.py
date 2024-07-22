a=int(input("enter a first number :"))
b=int(input("enter a secound number :"))
c=int(input("enter a third number :"))

if (a>b & a>c):
    print("greater number :",a)

elif(b>a & b>c):
    print("greater number :",b)

else:
    print("greater number :",c)