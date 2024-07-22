n=int(input("enter a number"))
fact=1

for i in range(1,n+1):
    print(i)
    fact=i*fact
    i=i+1

print("factorial numebr -> ",fact)