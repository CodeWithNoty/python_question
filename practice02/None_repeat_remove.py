list=[(None, None), (None, None), (3, 4), (12, 3), (None, )] 
print(str(list))
res=[]
for i in list:
    if (i.count(None)!=len(i)):
        res.append(i)
print("after ",str(res))
