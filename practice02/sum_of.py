a=[
    [1,2,3],
    [4,5,6],
    # [4,5,6],
]
b=[
    [1,2,3],
    [4,5,6],
    # [4,5,6],
]
l=[[0,0,0],
   [0,0,0],
]
#    [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
        l[i][j]=a[i][j]*b[i][j]

for r in l:
      print(r)




