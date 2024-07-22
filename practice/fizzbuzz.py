def num(n):
    if n%3==0:
        return "fizz"
    
    elif n%5==0:
        return "buzz"
    elif n%3==0 and n%5==0:
        return "fizzbuzz"
    
    else:
        return (str(n))
    
print(num(3))
print(num(15))
print(num(5))
print(num(30))
print(num(22))