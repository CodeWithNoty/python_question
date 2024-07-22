def num(n):
    n=n.replace(',','c')
    n=n.replace('.',', ')
    n=n.replace('c','.')
    return(n)
n="14, 625, 498.002"
print((num(n)))



