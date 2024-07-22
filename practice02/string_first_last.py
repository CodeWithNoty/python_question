def num(n):
    if len(n)<=2:
        return ''
    return n[0:2] + n[-2:]
print(num("neeraj"))
print(num("noty"))
print(num("n"))