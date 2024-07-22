def num(n):
    lenght=len(n)
    if lenght>2:
        if n[-3:]=='ing':
            n+='ly'
        else:
            n+='ing'
    return n
print(num('ab'))
print(num('abc'))
print(num('string'))
