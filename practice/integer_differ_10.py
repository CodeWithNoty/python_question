numebr=[i*10 for i in range(100)]
print(numebr)

for i in range(1,len(numebr)):
    if numebr[i]-numebr[i-1]!=10:
     result=False
     break

else:
       result=True

       print(result)
