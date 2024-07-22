def num(n,idx=0):
    for i in n:
       mul= i[idx]*i[idx+1]
       print(i,mul)
    
print(num((1,5,7,8)))