l=[[1,2]]
l1=[[2,3]]
s=[[0,0]]

for i in range(len(l)):
    for j in range(len(l1)):
        s[i][j]=l[i][j] + l1[i][j]
        

for s in s:
    print(s)