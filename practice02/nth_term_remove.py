def num(n,r):
    first=n[:r]
    last=n[r+1:]
    return first + last
print(num('python',3))
print(num('python',0))