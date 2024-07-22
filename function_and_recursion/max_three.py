a=int(input("enter a numebr :"))
b=int(input("enter a numebr :"))
c=int(input("enter a numebr :"))

def max(a,b,c):
    if(a>b & a>c):
        print("a is greater ")
        
    elif(b>a & b>c):
        print("b is greater ")

    else:
        print("c is greater ")

max(a,b,c)