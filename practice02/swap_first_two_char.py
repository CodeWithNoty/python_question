def num(a,b):
    str=a.replace(a[:2],b[:2])
    str1=b.replace(b[:2],a[:2])
    print(str," ",str1)
    
a='abc'
b='xyz'
print(num(a,b))