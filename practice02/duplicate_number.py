list=[1,22,33,22,4,3,1,3,5,22]
uni=[]
dup=[]
for i in list:
    if i not in uni:
        uni.append(i)
    elif i not in dup:
        dup.append(i)

print(uni)
print(dup)