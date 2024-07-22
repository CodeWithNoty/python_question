t=[(1,2,3),(-1,2,3),(1,-2,6)]
print(str(t))
res=[i for i in t if  all(j>=0 for j in i)]
print(str(res))

