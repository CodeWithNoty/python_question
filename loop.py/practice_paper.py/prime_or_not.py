n=int(input("enter a numebr :"))
prime=True

for i in range(2,n):
    if(n%i==0):
        prime=False
        break

if prime:
    print("prime :")

else:
    print("not :")
