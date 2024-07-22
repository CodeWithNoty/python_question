even=[]
odd=[]
for i in range(1,100):
    if i%2==0:
        even.append(i)
    elif i%3==0:
        odd.append(i)
print("Even =",even)
print("\n")
print("Odd =",odd)