def star(n):
    for i in range(0,n):
        for j in range(i,n+1):
            print('*',end=' ')
        print()
star(5)
