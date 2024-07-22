x=[
    [1,2],
    [3,4],
]
y=[
    [1,2],
    [3,4],
]



a=[
    [0,0],
    [0,0],
]
for i in range(0,len(a)):
    for j in range(len(a[0])):
        a[i][j]=x[i][j]+y[i][j]
    
for r  in a:
    print(r)