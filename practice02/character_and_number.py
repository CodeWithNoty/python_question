def num(n):
    n1=False
    n2=False
    for  i in n:
        if i.isalpha():
            n1=True
        if i.isdigit():
            n2=True
    return n1 and n2
print(num('neeraj1322'))
print(num('neeraj'))