def num(n):
    result=""
    for i in range(len(n)):
        if i%2==0:
            result=result+n[i]
    return result


print(num(('abcdef')))