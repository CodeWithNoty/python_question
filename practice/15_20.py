def num(x,y):
    sum=x+y
    print(sum)
    if sum  in range(15,20):
        print("sum is between 15-20") 
        return 20
    
    else:
        print("sum is not between 20 " )
        return sum
    
print(num(10,12)) 
print("\n")
print(num(10,7)) 