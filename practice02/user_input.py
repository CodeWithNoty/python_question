r=int(input("enter  a row :"))
c=int(input("enter  a coloumn :"))

matrix=[]

for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    matrix.append(a)


for i in range(r):
    for j in range(c):
        print(matrix[i][j],end=" ")
    print()
