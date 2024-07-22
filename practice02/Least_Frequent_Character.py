a=input("enter a string :")
print("original string :" +str(a))
all={}
for i in a:
    if i in all:
        all[i]+=1
    else:
        all[i]=1
res=min(all,key=all.get)
print("result "+str(res))