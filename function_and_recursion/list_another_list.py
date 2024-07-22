def uniqe_list(l):
 l1=[]
 for a in l:
    if a not in l1:
     l1.append(a)
 return l1
 
print(uniqe_list([1,2,3,3,3,4,4,5,6]))
