def num(x,y,z):
    if x==y or y==z or x==z:
        sum=0
    else:
        sum=x+y+z
    return sum
print(num(1,2,3))
print(num(1,3,1))