# list=[1,2,2,3,34,5,6,5,7,5,3,5,2,8,]
# l=list.count(5)

# print(f"{l} is a {l} time")

def list(l,n):
    count=0
    for i in l:
      if i==n:
         count=count+1
    return count
      
l=([15, 6, 7, 10, 12, 20, 10, 28, 10])
n=10
print('{} has occurred {} times'.format(n,list(l,n)))
