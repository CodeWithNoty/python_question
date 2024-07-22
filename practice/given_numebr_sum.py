#sum all given numebr 
def num(n,sum=0):
    for i in range(1,n+1,1):
        sum=sum+i
    return sum
#multiplay give numebr 
def mul(n,mul=1):
    for i in range(1,n+1,1):
        mul=mul*i
    return mul
    
#mutipication table
def table(n):
    for i in range(1,n+1):
     print(i)
     t=n*i
    return t
    
print(num(10))
print(mul(5))
print(table(2))