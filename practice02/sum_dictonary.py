def num(n):
    sum=0
    for i in n.values():
     sum=sum+i
    return sum
print(num({'a': 100, 'b': 200, 'c': 300}))