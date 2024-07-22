l=[1,2,3,4,5,6,7,8,9,10]
b=[]

# for i in l:
#     if i%2==0:
#         b.append(i)
# print(b)

b=(i for i in l if i%2==0)
print(b)