def fact(num):
    mul=1
    for i in range(1,5+1):
        mul=i*mul
        print(i)
        i=i+1
    print("factorial number :",mul)
fact(5)
