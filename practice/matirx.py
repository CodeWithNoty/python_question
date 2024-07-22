x=[[1,2,3],
[4,5,6],
[7,8,9]]

y=[[1,2,3],
[4,5,6],
[7,8,9]]

r=[[0,0,0],
[0,0,0],
[0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        r[i][j]=x[i][j]+y[i][j]

for r in r:
    print(r)