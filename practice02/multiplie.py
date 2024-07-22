a=[
    [1,2,3],
    [4,5,6],
    [4,5,6],
]
b=[
    [3,9,5],
    [11,33,39],
    [49,23,10],
]

print(len(a))
l=[[0,0,0],
   [0,0,0],
   [0,0,0],
]
even=[]
odd=[]

for i in range(0,len(a)):
    for j in range(len(a[0])):
        l[i][j]=a[i][j]*b[i][j]
for r in l:
    print(r)
    for i in r:
     if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Multiple By 2 ===>",even)
print("multipaly by 3 And 2 ====>",odd)
