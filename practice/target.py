def twosum(num,target,count=0):
    for i in num:
     print(i)
    if i[count] +  i[count+3]==target:
        return i[count]
    else:
        print("not")
twosum([[1,2,3,4,5,6,7,8]],10)