def num(n):
    count=1
    for i in range(len(n)-1):
      count=  n[i]*n[i+1]
    return count
        
print(num([10,20,30,40]))