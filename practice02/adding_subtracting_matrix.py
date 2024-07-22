a = [[1,2],
    [3,4]]

b = [[4,5],
    [6,7]]

res=[[0,0],
  [0,0]]

ses=[[0,0],
  [0,0]]

for i in range(0,len(a)):
    for j in range(len(a[0])):
        res[i][j]=a[i][j]+b[i][j]
        ses[i][j]=a[i][j]-b[i][j]
for r in res:
    print("a+b",r)

for q in ses:
    print("a-b",q)