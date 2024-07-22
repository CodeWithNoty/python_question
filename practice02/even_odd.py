# all=[1,2,3,4,5,6,7,8,9,10]
even=[]
odd=[]
for i in range(1,40):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("multiple by 2 =",even)
print("not multiple by 2 =",odd)